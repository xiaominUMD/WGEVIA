from readData import ReadMCData
import numpy as np
import sys
import csv
import os
import time
import networkx as nx
import multiprocessing
from multiprocessing import Pool
from swg2v.docGen import docGen
from swg2v.graphFeatureGen import graphFeatureGen
from swg2v.represent import represent
from swg2v.doDoc2Vec import doDoc2Vec

# enable parallel mode
parallel = True

def channelSG2V(reader,T,step,docGener,numOfGraph,idx):
    """
    thresholding input weighted sparse graphs with one threshold
    and generate features

    Inputs:
    reader : reader object contain loaded data sets
    T : current base threshod
    step : threshold step, threshold = T + step/2
    docGener : object to generate doc for Doc2Vec
    numOfGraph : number of graphs
    """
    avg_time = 0
    for i in range(numOfGraph):
        if sys.argv[9] == 'abs':
            #Abs
            absx = np.abs(reader.X[i])
        else:
            #NonAbs
            absx = reader.X[i]

        if sys.argv[8] == 'lessCut':
            #LessCut
            x = (absx > (T + step / 2)).astype(int)
        else:
            #RangeCut
            bindex1 = (absx > T)
            bindex2 = (absx < T + step)
            bindex3 = bindex1 & bindex2
            x = bindex3.astype(int)


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
        t_start = time.time()
        graphDoc = graphFeatureGen(G, features, wlIter)
        docGener.addDoc(graphDoc.wlIterations(), i)
        t_end = time.time()
        avg_time += (t_end-t_start)
    avg_time = avg_time/numOfGraph
    print("With "+str(T)+" Thres, Feature Extractor on one graph average used (s) : "+str(avg_time))
    if idx == 0:
        with open('../exp/result/mgeniaACC.csv', 'a') as csvfile:
            spamwriter = csv.writer(csvfile, delimiter=',')
            spamwriter.writerow(["Within "+str(idx)+" Channel, Feature Extractor on one graph average used (s) : "+str(avg_time)])

def oneChannelDocGen(i):
    """
    generate features for single channel of unweighted sparse graphs

    inputs:
    i : channel index
    """
    
    print("current ThresholdS: " + str(Ts[i]) +" in channel "+str(i))

    docGener = docGen()
    g2vfile = "g2v" + str(i) + ".csv"
    featureOut = g2vout + '/' + g2vfile
    #get Doc for current channel
    channelSG2V(reader, float(Ts[i]), step, docGener, numOfGraph,i)
    Doc2vec = doDoc2Vec(i,docGener.getDoc(), numOfGraph, Dim, downSampleRate, learnRate)
    del docGener
    #generate features using Doc by call Doc2Vec

    if sys.argv[6] == 'train':
        s = time.time()
        Doc2vec.run()
        e = time.time()
        print("Channel "+str(i)+" Doc2Vec Runtime(s): "+str(e-s))
        if i == 0:
            with open('../exp/result/mgeniaACC.csv', 'a') as csvfile:
                spamwriter = csv.writer(csvfile, delimiter=',')
                spamwriter.writerow(["Channel "+str(i)+" Doc2Vec Runtime(s): "+str(e-s)])

    elif sys.argv[6] == 'inference':
        Doc2vec.runWithTrainedModel()
    else:
        print("Error,please specify train or inference")

    outwriter = represent(Doc2vec.getRepresent(), numOfGraph, featureOut)
    del Doc2vec
    outwriter.output()
    del outwriter
    print("Doc2Vec done, SG2V done "+str(i))


def findRange(X):
    """
    helper function, Big arracy can not input to numpy directly
    """
    top = 0
    bot = 0
    for i in range(len(X)):
        X[i] = np.array(X[i])
        X[i] = X[i].astype(np.float)
        tmptop = np.max(X[i])
        tmpbot = np.min(X[i])
        if tmptop > top:
            top = tmptop
        if tmpbot < bot:
            bot = tmpbot
    return top,bot

#load inputs 
Threshold = sys.argv[1] 
jsonfolder = sys.argv[2] 
dim = sys.argv[3] 
wliter = sys.argv[4] 
modelNum = sys.argv[5]
g2vout = "../../multiChannelGen/channels/g2vFeatures"

if sys.argv[7] == 'posT':
    print("posT")
    posT = True
else:
    print("negT")
    posT = False

if sys.argv[8] == 'lessCut':
    print("lessCut")
else:
    print("rangeCut")

if sys.argv[9] == 'abs':
    print("abs")
else:
    print("nonabs")

#set hyper-parameters
Dim = int(dim)
wlIter = int(wliter)
learnRate = 0.025
downSampleRate = 0.0001

#count number of files, should be equal or larger than files existed
filenum = len(os.listdir('../../weightedGraphs/')) 
print("num of files: "+str(int(filenum)))
if filenum <= 2:
    print("ERROR: not enough input files")
else:
    if sys.argv[6] == 'train':
        #remove previous saved model from train mode
        os.system("cd ../trainedModel\nrm d2v*")

    reader = ReadMCData('04', int(filenum), '../../weightedGraphs/')
    reader.readX()
    print("done read X")
    #not necessary if user provided labelAll.csv
    #reader.readY()
    #print("done read Y")
    #not necessary if user provided labelAll.csv
    #reader.writeY()

    numOfGraph = len(reader.X)
    print("amount of input graphs: "+str(numOfGraph))
    print("finding top of all weights")
    top,bot = findRange(reader.X)
    print("got top "+str(top))

    Ts = []
    if posT != True:
        step = (float(top) - float(bot)) / (int(Threshold))  # negT
    else:
        step = float(top) / (int(Threshold))  # posT

    for i in range(int(Threshold)):
        if posT != True:
            Ts.append(float(bot) + i * step)  # negT
        else:
            Ts.append(i * step)  # posT

    #clean previous g2vi.csv files and json folder of previous run
    os.system("cd ../channels\nrm -rf [a-zA-Z]*[0-9]")
    os.system("cd ../channels/g2vFeatures\nrm g* c*")

    start = time.time()


    MODE = sys.argv[10]
    if parallel == True:
        #adjust mode when no enough memory for big data set
        if MODE == 'corenum':
            p = Pool(multiprocessing.cpu_count())
        elif MODE == 'channelnum':
            p = Pool(len(Ts))
        elif MODE == '4worker':
            p = Pool(int(sys.argv[11]))
        else:
            p = Pool(multiprocessing.cpu_count())
        p.map(oneChannelDocGen, range(len(Ts)))
    else:
        for i in range(len(Ts)):
            oneChannelDocGen(i)

    end = time.time()
    elapsedT = (end-start)
    print("WGEVIA finished in "+str(elapsedT)+" s")
    with open('../exp/result/mgeniaACC.csv', 'a') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=',')
        spamwriter.writerow(["WGEVIA finished in "+str(elapsedT)+" s"])

    #combine channel features
    for i in range(len(Ts)):
        if i > 0:
            os.system("cd ../channels/g2vFeatures\nsed -i 's/^[^,]*[0-9a-z]//' g2v"+str(i)+".csv")
        os.system("cd ../channels/g2vFeatures\nsed -i 's/\r//g' g2v"+str(i)+".csv\nsed -i 's/\t//g' g2v"+str(i)+".csv")
    os.system("cd ../channels/g2vFeatures\npaste g* > combinedFeature.csv")
    #classification using generated features
    of = "../exp/runtimeRecord/modelSave.csv"
    lof = "../exp/runtimeRecord/lastLoss.csv"
    os.system("python3 ./rc_datamining_dl_1d_cv.py ../channels/g2vFeatures/combinedFeature.csv "+of + " "+dim+" "+modelNum +" "+lof)
    os.system("echo classfication finished")
