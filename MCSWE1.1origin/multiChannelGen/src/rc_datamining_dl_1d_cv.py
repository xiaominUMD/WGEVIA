
# coding: utf-8

# In[1]:


# Import dependencies
from __future__ import absolute_import, division, print_function
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.metrics import balanced_accuracy_score
from sklearn.model_selection import KFold
from sklearn import preprocessing
import tensorflow as tf
import numpy as np
from tensorflow import keras
from scipy import stats
import os
from readData import ReadFLData
import sys
import time
import logging
logging.getLogger('tensorflow').disabled = True

# Read input_data.
LD = ReadFLData()

Yp = '../../weightedGraphs/labelAll.csv'

#take input from cmd
Xp = sys.argv[1] #input file with path

X,Y = LD.loadXY(Xp,Yp)
Y = Y.reshape((Y.shape[0],1))
XY = np.concatenate((X,Y),axis=1)
np.random.shuffle(XY)
X,Y = LD.splitXY(XY)

xxxTrain = X
yyyTrain = Y

#randomly shuffle Y for testing
#np.random.shuffle(yyyTrain)

K = 10                                  # K for K-fold
epochs_number = 100                     # The number of epochs
feature_length = xxxTrain.shape[1]        # The number of input features
model_bank = []
result_bank = []

# Model configuration
def model_define(n):
    # model 0
    if n == 0:
        model = keras.Sequential([
            keras.layers.Dense(256, input_shape=(feature_length,), activation=tf.nn.relu),
            keras.layers.Dense(2, activation=tf.nn.softmax),
        ])

    # model 1
    elif n == 1:
        model = keras.Sequential([
            keras.layers.Dense(128, input_shape=(feature_length,), activation=tf.nn.relu),
            keras.layers.Dense(2, activation=tf.nn.softmax),
        ])

    # model 2
    elif n == 2:
        model = keras.Sequential([
            keras.layers.Dense(128, input_shape=(feature_length,), activation=tf.nn.relu),
            keras.layers.Dense(64, input_shape=(feature_length,), activation=tf.nn.relu),
            keras.layers.Dense(2, activation=tf.nn.softmax),
        ])

    # model 3
    elif n == 3:
        model = keras.Sequential([
            keras.layers.Reshape((feature_length, 1)),
            keras.layers.Conv1D(filters=128, kernel_size=4, input_shape=(feature_length, 1), activation='relu'),
            keras.layers.Flatten(),
            keras.layers.Dropout(0.4),
            keras.layers.Dense(128, activation='relu'),
            keras.layers.Dense(64, activation='relu'),
            keras.layers.Dense(2, activation='softmax')
        ])
    return model

# K-fold cross validation configuration
input_data = xxxTrain
y = yyyTrain
kf = KFold(n_splits=K, shuffle=True)

import os
CNNsingleGPUscope = '0,1'
CNNsingleGPU = '/gpu:0'
os.environ["CUDA_VISIBLE_DEVICES"]=CNNsingleGPUscope
with tf.device(CNNsingleGPU):
    config = tf.ConfigProto()
    config.gpu_options.allow_growth = True
# Generate a session
    sess = tf.Session(config=config)
#in case dim 2 cant use cnn1d
    dim = int(sys.argv[3])
    modelNo = sys.argv[4]

    if(dim < 5):
    	modelc = 3
    else:
    	modelc = 4
    if(modelNo == 'all'):
        mrange = range(modelc)
        print("using model all")
    if(modelNo == '0'):
        mrange = [0]
        print("using model #0")
    if(modelNo == '1'):
        mrange = [1]
        print("using model #1")
    if(modelNo == '2'):
        mrange = [2]
        print("using model #2")
    #here
    if(modelNo == '3'):
        mrange = [3]
        print("using model #3")

    index = None
    stds = []
    stds_train = []
    for i in mrange:
        index = i
        # Delete previous result table if exists.
        try:
            del result_table
        except NameError:
            print('')

        # K-fold cross validation.
        train_times = []
        test_times = []
        for train_index, test_index in kf.split(y):

            # Divide data into data_train and data_test.
            data_train, data_test = input_data[train_index, :], input_data[test_index, :]
            y_train, y_test = y[train_index], y[test_index]

            # Normalization (Center and scale all variables to give them equal importance (mean:0, var:1))
            mean = np.mean(data_train, 0)
            std = np.std(data_train, 0)
            data_train = (data_train - mean) / std
            data_test = (data_test - mean) / std

            # Model initialization
            keras.backend.clear_session()
            # Generate a session
            sess = tf.Session()
            # KK.clear_session()
            try:
                del model
            except NameError:
                print('')

            model = model_define(i)

            # Model compilation.
            model.compile(optimizer='adam',
                         loss='sparse_categorical_crossentropy',
                         metrics=['accuracy'])

            # Model training.
            print("Start fit")
            start = time.time()
            his = model.fit(data_train, y_train, epochs=epochs_number,verbose=0)
            end = time.time()
            train_time = end - start
            print("train used (s): " + str(train_time))
            train_times.append(train_time)

            #train acc
            predict_train = model.predict(data_train)
            classes = predict_train.argmax(axis=-1)
            predict_trains = tf.argmax(predict_train, 1)
            train_bacc = balanced_accuracy_score(y_train, sess.run(predict_trains))
            stds_train.append(train_bacc)


            #evaluate
            #print(y_test)
            evalueRe = model.evaluate(data_test,y_test)
            evalueLoss = evalueRe[0]
            stds.append(evalueRe[1])
            # Prediction.

            print("Test start")
            start = time.time()
            predictions = model.predict(data_test)
            end = time.time()
            predict_time = (end-start)/len(data_test)
            print("test one sample used (s) : " + str(predict_time))

            test_times.append(predict_time)

            classes = predictions.argmax(axis=-1)
            prediction = tf.argmax(predictions, 1)

            #clean section
            keras.backend.clear_session()

            try:
                result_table[test_index] = sess.run(prediction)
            except NameError:
                result_table = np.zeros(input_data.shape[0])
                result_table[test_index] = sess.run(prediction)

        # Store the result in the result bank.
        result_bank.append(result_table)

    rec = []

    avg_train_time = np.average(train_times)
    avg_test_time = np.average(test_times)
    # Display the results
    # Class name specification.
    class_names = ['0', '1']
    count = index
    #print('File name:', file_name)
    for result in result_bank:
        print('model_', count)

        # Confusion matrix generation
        CF_matrix = confusion_matrix(y, result)

        # Classification report Generation
        class_report = classification_report(y, result, target_names=class_names)

        # Accuracy calculation
        acc = accuracy_score(y, result)
        bacc = balanced_accuracy_score(y, result)

        # Display the results
        print('\nConfusion Matrix')
        print(CF_matrix)
        print('\nClassification Report')
        print(class_report)
        print('\nAccuracy')
        print(acc)
        print("balanced ACC: "+str(bacc))
        S = "model " + str(count) + " Acc " + str(acc)
        rec.append(S)
        count = count + 1


    import csv
    of = sys.argv[2]

    #record model and Acc results
    with open(of, 'w') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=',')
        for i in range(len(rec)):
            spamwriter.writerow([rec[i]])
    #record last loss for bayesian optimization and acc
    lof = sys.argv[5]
    with open(lof, 'w') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=',')
        spamwriter.writerow([str(1-acc)])
        spamwriter.writerow([str(acc)])

    std = np.std(stds)
    std_train = np.std(stds_train)
    bacc_train = np.average(stds_train)
    #record last loss for bayesian optimization and acc
    with open('../exp/result/mgeniaACC.csv', 'a') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=',')
        spamwriter.writerow([rec[i]])
        spamwriter.writerow(['test std: '+str(std)])
        spamwriter.writerow(['train std: ' + str(std_train)])
        spamwriter.writerow(['test bacc: '+str(bacc)])
        spamwriter.writerow(['train bacc: ' + str(bacc_train)])

        spamwriter.writerow(['Average train time: ' + str(avg_train_time)])
        spamwriter.writerow(['Average test time: ' + str(avg_test_time)])
