import sys
import os
from docGen import docGen
from graphFeatureGen import graphFeatureGen
from loadGraph import loadGraph
from represent import represent
from doDoc2Vec import doDoc2Vec

"""
main script for SG2V algorithm when run independently
inputs args:
Dim : output feature dimension
wlIter : iterations of feature extractor
inputFolderPath : path of dir contain input graphs
outputFile : file to save generated features for graphs
"""

Dim = int(sys.argv[1])
wlIter = int(sys.argv[2])
inputFolderPath = sys.argv[3]
outputFile = sys.argv[4]
learnRate = 0.025
downSampleRate = 0.0001
numOfGraph = len(os.listdir(inputFolderPath))

loader = loadGraph()
docGener = docGen()

for i in range(numOfGraph):
    graph,features = loader.load(inputFolderPath+"graph_"+str(i)+".json")
    graphDoc = graphFeatureGen(graph,features,wlIter)
    docGener.addDoc(graphDoc.wlIterations(),i)
    #print("\rgraph_"+str(i)+".json docgen finished")
print("docGen finished")
Doc2vec = doDoc2Vec(docGener.getDoc(),numOfGraph,Dim,downSampleRate,learnRate)
Doc2vec.run()
Doc2vec.saveRepresent()
outwriter = represent(Doc2vec.getRepresent(),numOfGraph,outputFile)
outwriter.output()
print("weighted sparsed graph2vec done")
