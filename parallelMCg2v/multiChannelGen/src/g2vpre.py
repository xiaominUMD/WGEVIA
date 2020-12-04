from readData import ReadMCData
import numpy as np
import sys
import os
import time
import networkx as nx
import multiprocessing
from multiprocessing import Pool

from swg2v.docGen import docGen
from swg2v.graphFeatureGen import graphFeatureGen
from swg2v.represent import represent
from swg2v.doDoc2Vec import doDoc2Vec

parallel = True
g2vsingle = False

def channelSG2V(reader,T,step,docGener,numOfGraph):
    for i in range(numOfGraph):
        x = (reader.X[i] > (T+step/2)).astype(int)
        G = nx.from_numpy_matrix(x)

        features = []
        De = G.degree()
        if len(G.edges) == 0:
            G = nx.from_edgelist([])
        else:
            for v,d in De:
                if d != 0:
                    features.append(str(v))
                else:
                    features.append('Z'+str(v))

        graphDoc = graphFeatureGen(G, features, wlIter)
        docGener.addDoc(graphDoc.wlIterations(), i)

def channelG2v(reader,T,step,docGener,numOfGraph,g2vsingle):
    if g2vsingle == 'single':
        print("single G2V")
        step = 0 #for G2V, need comment out for other methods
    for i in range(numOfGraph):
        x = (reader.X[i] > (T+step/2)).astype(int)
        G = nx.from_numpy_matrix(x)

        features = []
        De = G.degree()
        if len(G.edges) == 0:
            G = nx.from_edgelist([])
        else:
            for v,d in De:
                if sys.argv[7] == 'degree':
                    features.append(str(d))
                elif sys.argv[7] == 'index':
                    features.append(str(v))

        graphDoc = graphFeatureGen(G, features, wlIter)
        docGener.addDoc(graphDoc.wlIterations(), i)

def oneChannelDocGen(i):
    g2vsingle = sys.argv[6]
    if g2vsingle == 'single':
        Ts[i] = 0.196
    print("current ThresholdS: " + str(Ts[i]) + " in channel " + str(i))
    docGener = docGen()
    #print(docGener)
    g2vfile = "g2v" + str(i) + ".csv"
    featureOut = g2vout + '/' + g2vfile
    channelG2v(reader, float(Ts[i]), step, docGener, numOfGraph,g2vsingle)
    Doc2vec = doDoc2Vec(docGener.getDoc(), numOfGraph, Dim, downSampleRate, learnRate)
    del docGener
    Doc2vec.run()
    Doc2vec.saveRepresent()
    outwriter = represent(Doc2vec.getRepresent(), numOfGraph, featureOut)
    del Doc2vec
    outwriter.output()
    del outwriter
    print("Doc2Vec done, G2V done "+str(i))

#big array can not use numpy
def findTop(X):
    top = 0
    for i in range(len(X)):
        X[i] = np.array(X[i])
        X[i] = X[i].astype(np.float)
        tmp = np.max(X[i])
        if tmp > top:
            top = tmp
    return top

Threshold = sys.argv[1] #NUM
jsonfolder = sys.argv[2] # "../dataset/json"
dim = sys.argv[3] #dimention of g2v
wliter = sys.argv[4] #num of iteration modified wl kernel do
modelNum = sys.argv[5]

g2vout = "../../multiChannelGen/channels/g2vFeatures"

Dim = int(dim)
wlIter = int(wliter)
learnRate = 0.025
downSampleRate = 0.0001

filenum = len(os.listdir('../../weightedGraphs/')) #+300 since our microcircuit data set is not 0-9000, it has some non file, indexed 9000 with 8967 files
print("num of files: "+str(int(filenum/2)+1))
reader = ReadMCData('04', int((filenum+600)/2)+1, '../../weightedGraphs/')
reader.readX()
print("done read X")
#reader.readY()
print("done read Y")
#reader.writeY()

numOfGraph = len(reader.X)
print("amount of input graphs: "+str(numOfGraph))
print("finding top of all weights")
top = findTop(reader.X)
print("got top "+str(top))

Ts = []
step = float(top)/(int(Threshold))        #posT
for i in range(int(Threshold)):
    Ts.append(i*step) 			#posT

#clean previous g2vi.csv files and json folder of previous run
os.system("cd ../channels\nrm -rf [a-zA-Z]*[0-9]")
os.system("cd ../channels/g2vFeatures\nrm g* c*")

start = time.time()

if parallel == True:
    #too many process no enough memory for big data set
    #p = Pool(multiprocessing.cpu_count())
    p = Pool(len(Ts))
    #p= Pool(4)
    p.map(oneChannelDocGen, range(len(Ts)))
else:
    for i in range(len(Ts)):
        oneChannelDocGen(i)

end = time.time()
elapsedT = (end-start)
print("MCSWE finished in "+str(elapsedT)+" s")

#combine features
for i in range(len(Ts)):
    if i > 0:
        os.system("cd ../channels/g2vFeatures\nsed -i 's/^[^,]*[0-9a-z]//' g2v"+str(i)+".csv")
    os.system("cd ../channels/g2vFeatures\nsed -i 's/\r//g' g2v"+str(i)+".csv\nsed -i 's/\t//g' g2v"+str(i)+".csv")
os.system("cd ../channels/g2vFeatures\npaste g* > combinedFeature.csv")
#train model
of = "../exp/runtimeRecord/modelSave.csv"
lof = "../exp/runtimeRecord/lastLoss.csv"
os.system("python3 ./rc_datamining_dl_1d_cv.py ../channels/g2vFeatures/combinedFeature.csv "+of + " "+dim+" "+modelNum +" "+lof)
os.system("echo classfication finished")
