
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
from DataLoader import DataLoader
import sys

LD = ReadFLData()
ld = DataLoader()
#Xp = '../../graph2vec-master/features/microcircuits.csv'
#Yp = '../dataset/csvs/labelAll.csv'
Yp = '../dataset/simulatedLabel.csv'
#take input from cmd
Xp = sys.argv[1] #input file with path

X,Y = LD.loadXY(Xp,Yp)
Y = Y.reshape((Y.shape[0],1))
XY = np.concatenate((X,Y),axis=1)
X,Y = ld.splitXY(XY)
'''

#TEST delete later
X = convertor.X
X = X.reshape((X.shape[0],X.shape[1],X.shape[2],1))
'''

xxxTrain = X
yyyTrain = Y

#randomly shuffle Y for testing
#np.random.shuffle(yyyTrain)

K = 10                                  # K for K-fold
epochs_number = 100                     # The number of epochs
feature_length = xxxTrain.shape[1]        # The number of input features
model_bank = []
result_bank = []


# In[5]:
from keras import Sequential
from keras.layers import Dense
from keras.layers import Activation
from keras.layers import Conv1D,Conv2D
from keras.layers import Flatten
from keras.layers import MaxPooling1D,MaxPooling2D
from keras.layers import GlobalAveragePooling1D
from keras.layers import Reshape
from keras.constraints import NonNeg
from keras.layers.core import Dropout

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
            keras.layers.Conv1D(filters=512, kernel_size=4, input_shape=(feature_length, 1), activation='relu'),
            keras.layers.Flatten(),
            keras.layers.Dropout(0.4),
            keras.layers.Dense(256, activation='relu'),
            keras.layers.Dense(128, activation='relu'),
            keras.layers.Dense(2, activation='softmax')
        ])
    elif n ==4:
        model = Sequential()

        # convolution layer 1
        model.add(Conv2D(128, (4, 4), activation='relu', input_shape=(X[0].shape[0], X[0].shape[1], 1), name="conv1"))
        model.add(MaxPooling2D(pool_size=(4, 4)))
        model.add(Conv2D(64, (4, 4), activation='relu', name="conv2"))
        model.add(Dropout(0.5))

        # fully connected
        model.add(Flatten())
        model.add(Dense(32, activation='linear', use_bias=True, name="dense1"))
        model.add(Activation('relu'))
        model.add(Dropout(0.5))

        model.add(Dense(2, activation='softmax', use_bias=True, name='dense2'))
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

    if(modelNo == '0'):
        mrange = [0]

    if(modelNo == '1'):
        mrange = [1]

    if(modelNo == '2'):
        mrange = [2]

    if(modelNo == '3'):
        mrange = [3]

    if(modelNo == '4'):
        mrange = [4]

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
        for train_index, test_index in kf.split(y):

            # Divide data into data_train and data_test.
            data_train, data_test = input_data[train_index, :], input_data[test_index, :]
            y_train, y_test = y[train_index], y[test_index]

            print("total amount of labels in test dataset: "+str(len(y_test)))
            count = 0
            for each in y_test:
                if each == 1:
                    count = count + 1

            print("one label in test dataset: "+str(count))

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
            if (i != 4):
                model.compile(optimizer='adam',
                             loss='sparse_categorical_crossentropy',
                             metrics=['accuracy'])

            # for CNN2D model
            if(i == 4):
                model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
                Y_trainConv = np.zeros((y_train.shape[0], 2));
                Y_trainConv[np.arange(y_train.shape[0]), y_train.astype(int)] = 1;
                y_train = Y_trainConv
                # Y_trainConv = Y_trainConv.astype(int);
                Y_testConv = np.zeros((y_test.shape[0], 2));
                Y_testConv[np.arange(y_test.shape[0]), y_test.astype(int)] = 1;
                y_test = Y_testConv



            # Model training.
            his = model.fit(data_train, y_train, epochs=epochs_number,verbose=0)
            #train acc
            predict_train = model.predict(data_train)
            classes = predict_train.argmax(axis=-1)
            predict_trains = tf.argmax(predict_train, 1)
            train_bacc = balanced_accuracy_score(y_train, sess.run(predict_trains))
            stds_train.append(train_bacc)


            #evaluate
            evalueRe = model.evaluate(data_test,y_test)
            evalueLoss = evalueRe[0]
            stds.append(evalueRe[1])
            # Prediction.
            predictions = model.predict(data_test)
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
    with open('../exp/result/fiveNodesACC.csv', 'a') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=',')
        spamwriter.writerow([rec[i]])
        spamwriter.writerow(['test std: '+str(std)])
        spamwriter.writerow(['train std: ' + str(std_train)])
        spamwriter.writerow(['test bacc: '+str(bacc)])
        spamwriter.writerow(['train bacc: ' + str(bacc_train)])

