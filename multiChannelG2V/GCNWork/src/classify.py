from src.readData import ReadFLData
from DataLoader import DataLoader
import numpy as np
import tensorflow as tf;
import keras
from keras.regularizers import l1_l2
from keras.regularizers import l2

LD = ReadFLData()
ld = DataLoader()
Xp = '../../graph2vec-master/features/microcircuits.csv'
Yp = '../dataset/csvs/labelAll.csv'
#Xp = '../../graph2vec-master/features/gentest.csv'
#Yp = '../dataset/genSample/labelAll.csv'

X,Y = LD.loadXY(Xp,Yp)
Y = Y.reshape((Y.shape[0],1))
XY = np.concatenate((X,Y),axis=1)
np.random.shuffle(XY);
X,Y = ld.splitXY(XY)

#CLASSIFICATION
train = 0.8;
val = 0;
test = 0.2;

# data preprocessing (split data into train, validation, test in 5:2.5:2.5)
sampleSize = X.shape[0];
X_train = X[np.arange(int(sampleSize * train)), :];
X_val = X[np.arange(int(sampleSize * train), int(sampleSize * (train + val)))];
X_test = X[np.arange(int(sampleSize * (train + val)), int(sampleSize * (train + val + test)))];
Y_train = Y[np.arange(int(sampleSize * train))];
Y_val = Y[np.arange(int(sampleSize * train), int(sampleSize * (train + val)))];
Y_test = Y[np.arange(int(sampleSize * (train + val)), int(sampleSize * (train + val + test)))];

# data ratio, 1's percent
train_ratio = np.sum(Y_train) / int(sampleSize * train);
if (val != 0):
    val_ratio = np.sum(Y_val) / int(sampleSize * val);
test_ratio = np.sum(Y_test) / int(sampleSize * test);
if (val != 0):
    print(train_ratio, val_ratio, test_ratio);
else:
    print(train_ratio, test_ratio);

model = 'nn'

if model == 'nn':
    Hs = [16,8,4]

    model = keras.Sequential([

        keras.layers.Dense(Hs[0], activation=tf.nn.relu, use_bias=True, kernel_regularizer=l2(0.001),
                           bias_regularizer=l2(0.001), name='fst'),
        keras.layers.Dense(Hs[1], activation=tf.nn.relu, use_bias=True, kernel_regularizer=l2(0.001),
                           bias_regularizer=l2(0.001), name='snd'),
        keras.layers.Dense(Hs[2], activation=tf.nn.relu, use_bias=True, kernel_regularizer=l2(0.001),
                           bias_regularizer=l2(0.001), name='trd'),
        keras.layers.Dropout(0.5, name='dropout'),

        keras.layers.Dense(2, activation=tf.nn.softmax, use_bias=True, kernel_regularizer=l2(0.0001),
                           bias_regularizer=l2(0.0001), name='fth')
    ]);

    model.compile(optimizer=tf.train.AdamOptimizer(),
                  loss='sparse_categorical_crossentropy',
                  metrics=['accuracy']);

    model.fit(X_train, Y_train, batch_size=32, epochs=100, shuffle=True);

    scores = model.evaluate(X_test, Y_test, verbose=0)

    acc_test = scores[1]

from sklearn import svm
if(model == 'svm'):
    clf = svm.SVC(gamma='scale', kernel='rbf')
    clf.fit(X_train, Y_train)
    preY = clf.predict(X_test)
    acc_test = (preY == Y_test).mean()

print(acc_test)