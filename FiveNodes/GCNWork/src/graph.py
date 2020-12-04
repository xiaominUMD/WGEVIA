import networkx as nx
import matplotlib.pyplot as plt
from networkx.readwrite import json_graph
import json
import numpy as np

class graph:
    def __init__(self,Xb):
        self.G = nx.from_numpy_matrix(Xb)
        self.max = np.max(Xb)
        self.Xb = Xb
        self.nodeFeatures = []
        self.reorderedEdge = np.full((100,1),-1)
        self.newNodeMap = np.full((100,1),-1)
        self.gnncount = 1

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


        if (self.max == 0):
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

            file.write("\"features\": {")

            self.nodeDegreeFullNodesM1(De, file)
            #self.nodeDegree(De, file)
            # self.nodeWeightSum(EI, file)
            # self.n2vFeatures(file)

    def outjsonFullNodesNF(self, file):
        List = nx.to_dict_of_lists(self.G)
        node0 = List[0]

        EV = self.G.edges()
        De = self.G.degree()

        if (self.max == 0):
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

            file.write("\"features\": {")

            self.nodeDegreeFullNodes(De, file)
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
                    file.write("\""+str(record[j][0])+"\": \""+str(record[j][0])+"\"}}")
                else:
                    file.write("\"" + str(record[j][0]) + "\": \"" + "Z"+str(record[j][0]) + "\"}}")
            else:
                if record[j][1] != 0:
                    file.write("\""+str(record[j][0])+"\": \""+str(record[j][0])+"\", ")
                else:
                    file.write("\"" + str(record[j][0]) + "\": \"" +"Z"+ str(record[j][0]) + "\", ")

    def nodeDegreeFullNodesNF(self,De,file):

        record = []
        for a, d in De:

            record.append([a,d])

        for j in range(len(record)):

            if (j == len(record)-1):
                if record[j][1] != 0:
                    file.write("\""+str(record[j][1])+"\"]}")
                else:
                    file.write("\""+"Z"+str(record[j][0]) + "\"]}")
            else:
                if record[j][1] != 0:
                    file.write("\""+str(record[j][1])+"\", ")
                else:
                    file.write("\""+"Z"+ str(record[j][0]) + "\", ")


    def nodeDegreeFullNodesM1(self,De,file):

        record = []
        for a, d in De:
            record.append([a,d])

        for j in range(len(record)):

            if (j == len(record)-1):
                file.write("\""+str(record[j][0])+"\": \""+str(record[j][1])+"\"}}")

            else:
                file.write("\""+str(record[j][0])+"\": \""+str(record[j][1])+"\", ")

    def nodeDegreeFullNodesIdea4(self,De,file):

        record = []
        for a, d in De:

            record.append([a,d])

        for j in range(len(record)):

            if (j == len(record)-1):
                if record[j][1] != 0:
                    file.write("\""+str(record[j][0])+"\": \""+str(record[j][1])+"\"}}")
                else:
                    file.write("\"" + str(record[j][0]) + "\": \"" + "E" + "\"}}")
            else:
                if record[j][1] != 0:
                    file.write("\""+str(record[j][0])+"\": \""+str(record[j][1])+"\", ")
                else:
                    file.write("\"" + str(record[j][0]) + "\": \"" +"E" + "\", ")



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

    def ToGNNinputNumOfGraph(self,file,numOfGraphs):
        file.write(str(numOfGraphs)+"\n")

    def reorderEdge(self):
        EV = self.G.edges()
        count = 0
        for u, v in EV:
            if(self.reorderedEdge[u] == -1):
                self.reorderedEdge[u] = count
                self.newNodeMap[count] = u
                count = count + 1
            if(self.reorderedEdge[v] == -1):
                self.reorderedEdge[v] = count
                self.newNodeMap[count] = v
                count = count + 1


    def getedgeCount(self,index):
        count = 0;
        for each in self.Xb[index[0]]:
            if each > 0:
                count = count+1

        return count

    def NumOfNodeHavingEdge(self):
        count = 0
        for each in self.Xb:
            if np.max(each) > 0:
                count = count + 1
        return count


    #generating formatted input to power-GNN(MIT)
    def ToGNNinput(self,file,labelfile):
        numOfNodesHavingEdge = self.NumOfNodeHavingEdge()
        self.reorderEdge()
        labelOfThisG = labelfile.readline()
        file.write(str(numOfNodesHavingEdge)+' '+labelOfThisG)
        for i in range(numOfNodesHavingEdge):
            edgeCount = self.getedgeCount(self.newNodeMap[i])
            tmpAry = self.Xb[self.newNodeMap[i][0]]
            connectedTo = np.where( tmpAry == 1)[0]
            file.write("0 "+str(edgeCount)+' ')#write node tag, edgecount
            for j in range(edgeCount):
                file.write(str(self.reorderedEdge[connectedTo[j]][0]) + ' ')
            file.write('\n')

 #generating formatted input to power-GNN(MIT)
    def ToGNNinput100(self,file,labelfile,wrc):
        numOfNodesHavingEdge = len(self.G.nodes)

        labelOfThisG = labelfile.readline()
        if len(self.G.edges) != 0:
            file.write(str(numOfNodesHavingEdge)+' '+labelOfThisG)
            wrc = wrc+1
            for i in range(numOfNodesHavingEdge):
                edgeCount = self.getedgeCount([i])
                tmpAry = self.Xb[i]
                connectedTo = np.where( tmpAry == 1)[0]
                file.write("0 "+str(edgeCount)+' ')#write node tag, edgecount
                wrc = wrc + 1
                for j in range(edgeCount):
                    file.write(str(connectedTo[j]) + ' ')

                file.write('\n')
                print(wrc)

        return wrc




