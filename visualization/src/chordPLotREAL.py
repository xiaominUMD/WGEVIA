from readData import ReadMCData
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import DataLoader
import random

for i in range(100,101):
    try:
        idx = 11136#random.randrange(0, 1201)
        reader = ReadMCData('04', 0, '../../MCSWE1.1origin/mcDataset/csvsReal2/')
        reader.readXsingle(idx) #read data2.csv
        labels = '../../MCSWE1.1origin/mcDataset/csvsReal2/labelAll.csv'
        ld = DataLoader.DataLoader()
        data = reader.X[0]
        Y = ld.loadData(labels)

        adjMatrix = np.array(data)
        adjMatrixFloat = adjMatrix.astype(np.float)
        adjMatrixAbs = abs(adjMatrixFloat)

        minimum = np.min(adjMatrixFloat)
        maximum = np.max(adjMatrixFloat)

        adjMatrix = (abs(adjMatrixFloat) != 0).astype(int)

        G = nx.from_numpy_matrix(adjMatrix)
        pos = nx.circular_layout(G)
        edge_wts = [5 * ((adjMatrixFloat[edge[0], edge[1]]-minimum)/(maximum - minimum)) for edge in G.edges()]
        #edge_clr = [((adjMatrixFloat[edge[0], edge[1]]-minimum)/(maximum - minimum)) for edge in G.edges()]
        edge_clr = [adjMatrixFloat[edge[0], edge[1]] for edge in G.edges()]


        plt.figure()
        sc = nx.draw_networkx_nodes(G, pos = pos, node_list = G.nodes(),node_size = 1)
        #ss = nx.draw_networkx_edges(G, pos = pos,edge_color= edge_clr , width=1,edge_vmin= -1 ,edge_vmax = 1)
        ss = nx.draw_networkx_edges(G, pos=pos, edge_color=edge_clr, width=1)

        plt.colorbar(ss)
        plt.title("graph label : "+str(int(Y[idx][0])))

        plt.show()
        #plt.savefig("../visOut/microcircuit"+str(idx)+".png")  # save as png
        print("graph label : "+str(Y[idx]))
        print("max: "+str(maximum))
        print("min: "+str(minimum))
        '''
        nx.draw_circular(G, with_labels = False,font_size = 6,node_size = 1,node_color='y',edge_wts = edge_wts,edge_clr=edge_clr)
        plt.savefig("../visOut/l0.png") # save as png
        plt.show() # display
        '''
    except:
        print("no such file")