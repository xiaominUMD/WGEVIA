import numpy as np
import pandas as pd
from mpl_toolkits.mplot3d import Axes3D
from keras.datasets import mnist
import matplotlib.pyplot as plt
from readData import ReadFLData
import sys
import logging
logging.getLogger('tensorflow').disabled = True
from sklearn import decomposition

"""
Python scripts for visualization using 3d T-sne algorithm
"""

# Read input_data.
LD = ReadFLData()
Yp = '../labels/labelAllr2.csv'

import time
from sklearn.manifold import TSNE
#take input from cmd
for i in range(40):
    Xp = '../REAL2/g2vFeatures/g2v'+str(i)+'.csv' #input file with path

    X,Y = LD.loadXY(Xp,Yp)
    Y = Y.reshape((Y.shape[0],1))
    XY = np.concatenate((X,Y),axis=1)
    X,y = LD.splitXY(XY)
    fig = plt.figure(1, figsize=(4, 3))
    plt.clf()
    ax = Axes3D(fig, rect=[0, 0, .95, 1], elev=48, azim=134)
    #n_sne = 7000

    time_start = time.time()
    tsne = TSNE(n_iter=300,n_components=3)
    X = tsne.fit_transform(X)

    class1_sample = []
    class2_sample = []
    for i in range(len(X)):
        if int(y[i]) == 1:
            class1_sample.append(X[i])
        else:
            class2_sample.append(X[i])
    fig = plt.figure(figsize=(8, 8))
    ax = fig.add_subplot(111, projection='3d')
    plt.rcParams['legend.fontsize'] = 10
    class1_sample = np.array(class1_sample)
    class2_sample = np.array(class2_sample)

    c1=class1_sample[:, 0]
    ax.plot(class1_sample[:, 0], class1_sample[:, 1], class1_sample[:, 2] ,'.', markersize=8, color='blue', alpha=0.5 ,
            label='class1')
    ax.plot(class2_sample[:, 0], class2_sample[:, 1], class2_sample[:, 2] ,'.', markersize=8, alpha=0.5, color='red',
            label='class2')
    plt.title('Samples for class 1 and class 2')
    ax.legend(loc='upper right')

    plt.show()