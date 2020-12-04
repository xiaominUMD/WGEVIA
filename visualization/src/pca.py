import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from readData import ReadFLData
from DataLoader import DataLoader

from sklearn import decomposition
from sklearn import datasets

"""
Python script for visualization using PCA
"""

LD = ReadFLData()
ld = DataLoader()
Yp = '../labels/labelAllr2.csv'
np.random.seed(5)

for i in range(40):
    Xp = '../REAL2/g2vFeatures/g2v' + str(i) + '.csv'  # input file with path

    X, Y = LD.loadXY(Xp, Yp)
    Y = Y.reshape((Y.shape[0], 1))
    XY = np.concatenate((X, Y), axis=1)
    X, y = ld.splitXY(XY)

    fig = plt.figure(1, figsize=(4, 3))
    plt.clf()
    ax = Axes3D(fig, rect=[0, 0, .95, 1], elev=48, azim=134)

    plt.cla()
    pca = decomposition.PCA(n_components=3)
    pca.fit(X)
    X = pca.transform(X)

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