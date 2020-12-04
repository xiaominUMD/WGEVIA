import sys
import os
import DataLoader
import bigGraph
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from loadGraph import loadGraph

"""
Python script for generating aggregated graphs for visualization
"""

inputFolderPath = '../../MCSWE1.1origin/graphOut/json/'
labels = '../../MCSWE1.1origin/mcDataset/csvsReal2/labelAll.csv'
#outputFile = sys.argv[2]

numOfGraph = len(os.listdir(inputFolderPath))
ld = DataLoader.DataLoader()

loader = loadGraph()
Y = ld.loadData(labels)
numOfNode = 420
bg = bigGraph.bigGraph(numOfNode,Y)
for i in range(numOfGraph):
    graph,features = loader.load(inputFolderPath+"graph_"+str(i)+".json")
    bg.aggregate(graph,i)

g0,g1 = bg.avg()
s1 = np.sum(g0)
s2 = np.sum(g1)
print("graph labeled 0 has edges: "+str(s1))
print("graph labeled 1 has edges: "+str(s2))


G0 = nx.from_numpy_matrix(g0)
G1 = nx.from_numpy_matrix(g1)

nx.draw_circular(G0, with_labels = True,font_size = 6,node_size = 50,edge_color = 'g',node_color='y')
plt.savefig("../visOut/l0.png") # save as png
plt.show() # display

nx.draw_circular(G1, with_labels = True,font_size = 6,node_size = 50,edge_color = 'g',node_color='y')
plt.savefig("../visOut/l1.png") # save as png
plt.show() # display

print("done")