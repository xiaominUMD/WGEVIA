from readData import ReadMCData
import sys
import numpy as np
import networkx as nx
import os

"""
Python script for output unweighted graphs with set threshold from weighted graph
Used for preparing unweighted graphs for visualization purpose
"""

def outjsonFullNodesNF(X, file):
    G = nx.from_numpy_matrix(X)
    EV = G.edges()
    De = G.degree()

    if (len(EV) == 0):
        # empty graph
        file.write("{\"edges\": [],\"features\": {}}")
    else:
        file.write("{\"edges\": [")
        i = 0
        for u, v in EV:
            i = i + 1
            if (i == len(EV)):
                file.write("[" + str(u) + ", " + str(v) + "]], ")
            else:
                file.write("[" + str(u) + ", " + str(v) + "], ")
        if (i == 0):
            print(file.name + " HAS NO EDGE")

        file.write("\"features\": []}")

        #self.nodeDegreeFullNodes(De, file)
        # self.nodeWeightSum(EI, file)
        # self.n2vFeatures(file)

T = 0.05 #pre calculated

reader = ReadMCData('04', 18200, '../mcDataset/csvsReal2/')  # name , MC count, path
reader.readX()

# reader.writeXcsv()
print("current Threshold: " + str(T) + "\n")

numOfEmptyG=0
for i in range(len(reader.X)):
    reader.X[i] = np.array(reader.X[i])
    reader.X[i] = reader.X[i].astype(np.float)
    reader.X[i] = (reader.X[i] > T).astype(int)
    top = np.max(reader.X[i])
    if top == 0:
        numOfEmptyG = numOfEmptyG + 1
os.system("cd ./json\nrm *")
jsonfolder = './json/'
for i in range(len(reader.X)):
    f = open(jsonfolder + "graph_"+str(i) + ".json", "w+")
    outjsonFullNodesNF(reader.X[i], f)
    f.close()
    print("finished graph :"+str(i))



print("done")