import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from keras.datasets import mnist
from readData import ReadFLData
from DataLoader import DataLoader
from sklearn import metrics
import sys
import logging
logging.getLogger('tensorflow').disabled = True

"""
Python script for visualization of one channel's feature
"""

# Read input_data.
LD = ReadFLData()
ld = DataLoader()
Yp = '../labels/labelAllr2.csv'
#Yp = 'labelAlls.csv'

import time
from sklearn.manifold import TSNE
#take input from cmd

Xp = '../singleFeatures/g2vt0.csv' #input file with path

X,Y = LD.loadXY(Xp,Yp)
Y = Y.reshape((Y.shape[0],1))
XY = np.concatenate((X,Y),axis=1)
X,Y = ld.splitXY(XY)

#n_sne = 7000

time_start = time.time()
tsne = TSNE(n_iter=300,n_components=2)
tsne_results = tsne.fit_transform(X)

print ('t-SNE done! Time elapsed: {} seconds'.format(time.time()-time_start))

label = Y
silhScore = metrics.silhouette_score(tsne_results, label, metric='sqeuclidean')
print("the silhouette score is: " + str(silhScore))


# Create the figure
fig = plt.figure( figsize=(8,8) )
ax = fig.add_subplot(1, 1, 1, title='TSNE' )
# Create the scatter
ax.scatter(
    x=tsne_results[:,0],
    y=tsne_results[:,1],
    c=label,
    cmap=plt.cm.get_cmap('Paired'),
    alpha=0.4)
plt.savefig('../plotReal2/combinedREAL2.png')
plt.show()
