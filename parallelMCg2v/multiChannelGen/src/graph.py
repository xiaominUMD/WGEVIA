import networkx as nx
import matplotlib.pyplot as plt
from networkx.readwrite import json_graph
import json
import numpy as np

class graphMem:
    def __init__(self,X,T,step):
        x = np.array(X)
        x = x.astype(np.float)
        #print(x)
        self.Xb = (x > (T+step/2)).astype(int)
        self.G = nx.from_numpy_matrix(self.Xb)
        #print("graph in graph.py")
        #print(self.G.neighbors(0))
        self.max = np.max(self.Xb)
        self.nodeFeatures = []

    def outjsonFullNodesNF(self, file):
        List = nx.to_dict_of_lists(self.G)
        node0 = List[0]

        EV = self.G.edges()
        De = self.G.degree()

        file.write("{\"edges\": [")
        i = 0
        for u, v in EV:
            i = i + 1
            if (i == len(EV)):
                file.write("[" + str(u) + ", " + str(v) + "]], ")
            else:
                file.write("[" + str(u) + ", " + str(v) + "], ")
        if (i == 0):
            file.write("], ")
            print(file.name + " HAS NO EDGE")

        file.write("\"features\": [")

        self.nodeDegreeFullNodesNF(De, file)
        # self.nodeWeightSum(EI, file)
        # self.n2vFeatures(file)

    def nodeDegreeFullNodesNF(self,De,file):

        record = []
        for a, d in De:

            record.append([a,d])

        for j in range(len(record)):

            if (j == len(record)-1):
                if record[j][1] != 0:
                    file.write("\""+str(record[j][1])+"\"]}")
                else:
                    file.write("\""+"E"+str(record[j][0]) + "\"]}")
            else:
                if record[j][1] != 0:
                    file.write("\""+str(record[j][1])+"\", ")
                else:
                    file.write("\""+"E"+ str(record[j][0]) + "\", ")

class graph:
    def __init__(self,Xb,X,edgeInfo):
        self.G = nx.from_numpy_matrix(Xb)
        self.edgeInfo = edgeInfo
        self.max = np.max(Xb)
        self.X = X
        self.nodeFeatures = []

    def plot(self):
        nx.draw_networkx_nodes(self.G, pos=nx.spring_layout(self.G))
        nx.draw_networkx_edges(self.G, pos=nx.spring_layout(self.G))
        nx.draw_networkx_labels(self.G, pos=nx.spring_layout(self.G))
        plt.show()

    def json(self):
        data = json_graph.node_link_data(self.G)

        data2 = json_graph.adjacency_data(self.G)

        s = json.dumps(data)

    def outemb(self,file):
        for i in range(self.X.shape[0]):
            for j in range(self.X.shape[1]):
                if(self.X[i][j] != 0):
                    file.write(str(i)+" "+str(j)+" "+str(self.X[i][j])+'\n')


    def getNodeFeatures(self,fileHandler):
        
        line = fileHandler.readline()
        while True:
            line = fileHandler.readline()
    
            if not line :
                break;
            nodestring = line.strip()
            twoString = nodestring.split(" ",1)
            self.nodeFeatures.append((twoString[0],twoString[1]))

    #output networkx graph to json files for input to graph2vec
    def outjson(self,file):
        List = nx.to_dict_of_lists(self.G)
        node0 = List[0]

        EV = self.G.edges()
        De = self.G.degree()
        EI = self.edgeInfo


        if(self.max == 0):
            #empty graph
            file.write("{\"edges\": [],\"features\": {}}")
        else:
            for a, d in De:
                if d != 0:
                    EI[a] = EI[a]/1

            file.write("{\"edges\": [")
            i = 0
            for u, v in EV:
                i = i + 1
                if(i == len(EV)):
                    file.write("["+str(u)+", "+str(v)+"]], ")
                else:
                    file.write("["+str(u)+", "+str(v)+"], ")
            if(i == 0):
                print(file.name+" HAS NO EDGE")

            file.write("\"features\": {")
            
            self.nodeDegree(De,file)
            #self.nodeWeightSum(EI, file)
            #self.n2vFeatures(file)

    def outjsonFullNodes(self, file):
        List = nx.to_dict_of_lists(self.G)
        node0 = List[0]

        EV = self.G.edges()
        De = self.G.degree()
        EI = self.edgeInfo

        if (self.max == 0):
            # empty graph
            file.write("{\"edges\": [],\"features\": {}}")
        else:
            for a, d in De:
                EI[a] = EI[a] / 1

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

            file.write("\"features\": {")

            self.nodeDegreeFullNodes(De, file)
            # self.nodeWeightSum(EI, file)
            # self.n2vFeatures(file)

    def outjsonFullNodesNF(self, file):
        List = nx.to_dict_of_lists(self.G)
        node0 = List[0]

        EV = self.G.edges()
        De = self.G.degree()
        EI = self.edgeInfo

        if (self.max == 0):
            # empty graph
            file.write("{\"edges\": [],\"features\": []}")
        else:
            for a, d in De:
                EI[a] = EI[a] / 1

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

            file.write("\"features\": [")

            self.nodeDegreeFullNodesNF(De, file)
            # self.nodeWeightSum(EI, file)
            # self.n2vFeatures(file)

    def n2vFeatures(self,file):
        record = []
        for a, d in self.nodeFeatures:
            if(d != 0):
                record.append([a,d])

        for j in range(len(record)):

            if (j == len(record)-1):
                file.write("\""+record[j][0]+"\": \""+record[j][1]+"\"}}")
            else:
                file.write("\""+record[j][0]+"\": \""+record[j][1]+"\", ")

    def nodeDegree(self,De,file):

        record = []
        for a, d in De:
            if(d != 0):
                record.append([a,d])

        for j in range(len(record)):

            if (j == len(record)-1):
                file.write("\""+str(record[j][0])+"\": \""+str(record[j][1])+"\"}}")
            else:
                file.write("\""+str(record[j][0])+"\": \""+str(record[j][1])+"\", ")

    def nodeDegreeFullNodes(self,De,file):

        record = []
        for a, d in De:

            record.append([a,d])

        for j in range(len(record)):

            if (j == len(record)-1):
                if record[j][1] != 0:
                    file.write("\""+str(record[j][0])+"\": \""+str(record[j][1])+"\"}}")
                else:
                    file.write("\"" + str(record[j][0]) + "\": \"" + "E"+str(record[j][0]) + "\"}}")
            else:
                if record[j][1] != 0:
                    file.write("\""+str(record[j][0])+"\": \""+str(record[j][1])+"\", ")
                else:
                    file.write("\"" + str(record[j][0]) + "\": \"" +"E"+ str(record[j][0]) + "\", ")

    def nodeDegreeFullNodesNF(self,De,file):

        record = []
        for a, d in De:

            record.append([a,d])

        for j in range(len(record)):

            if (j == len(record)-1):
                if record[j][1] != 0:
                    file.write("\""+str(record[j][1])+"\"]}")
                else:
                    file.write("\""+"E"+str(record[j][0]) + "\"]}")
            else:
                if record[j][1] != 0:
                    file.write("\""+str(record[j][1])+"\", ")
                else:
                    file.write("\""+"E"+ str(record[j][0]) + "\", ")

    def nodeWeightSum(self, EI, file):
        record = []
        for i in range(len(EI)):

            if(EI[i] != 0):
                record.append([i,EI[i]])

        for j in range(len(record)):

            if (j == len(record)-1):
                file.write("\""+str(record[j][0])+"\": \""+str(record[j][1])+"\"}}")
            else:
                file.write("\""+str(record[j][0])+"\": \""+str(record[j][1])+"\", ")




