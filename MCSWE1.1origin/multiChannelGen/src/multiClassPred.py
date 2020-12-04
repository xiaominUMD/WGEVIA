import pandas
from keras.models import Sequential
from keras.layers import Dense
from keras.wrappers.scikit_learn import KerasClassifier
from keras.utils import np_utils
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import KFold
from sklearn.preprocessing import LabelEncoder
from readData import ReadFLData
import numpy as np
from tensorflow import keras
import tensorflow as tf
from sklearn.pipeline import Pipeline

# Read input_data.
LD = ReadFLData()

Yp = '../../weightedGraphs/labelAll.csv'

#take input from cmd
Xp = '../../multiChannelGen/channels/g2vFeatures/combinedFeature.csv'

X,Y = LD.loadXY(Xp,Yp)
Y = Y.reshape((Y.shape[0],1))
XY = np.concatenate((X,Y),axis=1)
np.random.shuffle(XY)
X,Y = LD.splitXY(XY)
#np.random.shuffle(Y)
feature_length = X.shape[1]

# encode class values as integers
encoder = LabelEncoder()
encoder.fit(Y)
encoded_Y = encoder.transform(Y)
# convert integers to dummy variables (i.e. one hot encoded)
dummy_y = np_utils.to_categorical(encoded_Y)


# define baseline model
def baseline_model():
    # create model
    model = keras.Sequential([
        keras.layers.Dense(128, input_shape=(feature_length,), activation=tf.nn.relu),
        keras.layers.Dense(64, input_shape=(feature_length,), activation=tf.nn.relu),
        keras.layers.Dense(5, activation=tf.nn.softmax),
    ])
    # Compile model
    model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
    return model


estimator = KerasClassifier(build_fn=baseline_model, epochs=200, batch_size=32, verbose=1)
kfold = KFold(n_splits=10, shuffle=True)
results = cross_val_score(estimator, X, dummy_y, cv=kfold)
print("Baseline: %.2f%% (%.2f%%)" % (results.mean() * 100, results.std() * 100))