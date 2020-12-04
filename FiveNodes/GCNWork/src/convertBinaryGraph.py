import numpy as np
import numpy as np
import matplotlib.pyplot as plt

class ConvertBinaryGraph:
    """
    convert weighted graph to binary graph
    @author Xiaomin Wu
    @date 09162019
    """

    def __init__(self, threshold):
        self.threshold = threshold
        self.X = None
        self.Y = None
        self.Xb = None
        self.edgeWeightSumPerNode = None
        self.nonZeros = []

        self.bottom = None
        self.top = None

    def tonparyfloat(self, X, Y):
        self.X = np.array(X)
        self.Y = np.array(Y)
        self.X = self.X.astype(np.float)
        self.Y = self.Y.astype(np.int)

    def findTopRange(self):
        maxEachPic = []
        for pic in self.X:
            if(np.max(pic) != 0):
                maxEachPic.append(np.max(pic))

        self.bottom = np.min(self.X)
        self.top = np.min(maxEachPic)
        print(str(self.top)+ ' '+str(self.bottom)+"\n")

    def storeNonZeros(self):
        for pic in self.X:
            for row in pic:
                for value in row:
                    if value != 0:
                        self.nonZeros.append(value);

    def plotValueHistogram(self):
        self.nonZeros = np.array(self.nonZeros)
        max = self.nonZeros.max()
        min = self.nonZeros.min()
        for bins in [10,15,20,25,30]:
            plt.figure(figsize=(20,10))
            plt.hist(self.nonZeros, bins=bins)
            plt.title("Histogram of edge weights with "+str(bins)+" bins")
            #plt.show()
            plt.savefig("/Users/xiaomin/Desktop/GCNWork/dataHistogram/histogram"+str(bins)+"bins")



    def gatherEdgeInfo(self):
        self.edgeWeightSumPerNode = np.sum(self.X, axis=1)
        print('edges weigts sumed\n')

    def gatherEdgeInfoAbs(self):
        self.edgeWeightSumPerNode = np.sum(np.abs(self.X), axis=1)
        print('abs edges weigts sumed\n')

    def convert(self):
        #self.Xb = np.abs(self.X)
        self.Xb = (self.X > self.threshold).astype(int)

    def originalMatrixplot(self, path):

        for i in range(len(self.X)):
            plt.imshow(self.X[i])
            if(i == 0):
                plt.colorbar()
            plt.title('label: '+str(self.Y[i]))
            plt.savefig(path+str(i)+".png")

    def emptyGraph(self):
        count = 0
        for pic in self.X:
            if np.max(pic)==0:
                print(str(count) + "th graph has no positive edges\n")
                count = count + 1
        return count

    def Yratio(self):
        count0 = 0
        count1 = 0
        for eachY in self.Y:
            if eachY == 1:
                count1 = count1 + 1
            else:
                count0 = count0 + 1

        print("Dataset has "+str(count1)+" 1 label; "+str(count0)+" 0 label\n")

    # for simulate graph, test algorithm
    def binaryAdjMatrixGen1(self, numOfGraph, numOfnode):
        #half labeled 0 half labeled 1
        graphs = []



        file = open("../dataset/simulatedLabel.csv","w")
        for i in range(numOfGraph):
            if i <numOfGraph/2:
                # generating 0-labeled graph
                G = np.zeros((numOfnode, numOfnode))
                #seed = np.random.choice(numOfnode - 5,1)[0]
                seed = 0
                G[seed][seed+1] = 1
                #G[seed+1][seed+2] = 1
                #G[seed+2][seed+3] = 1
                #G[seed][seed + 3] = 1

                graphs.append(G)
                # generating labels
                file.write("0\n")
            else:
                G = np.zeros((numOfnode, numOfnode))
                #seed = np.random.choice(numOfnode - 1, 1)[0]
                seed = 0

                G[seed][seed + 1] = 1
                #G[seed][seed + 2] = 1
                #G[seed + 2][seed + 3] = 1
                G[seed + 3][seed + 4] = 1

                graphs.append(G)

                file.write("1\n")

        self.Xb = graphs
        self.Xb = np.array(self.Xb)
        file.close()

    def binaryAdjMatrixGen2(self, numOfGraph, numOfnode):
        #half labeled 0 half labeled 1
        graphs = []



        file = open("../dataset/simulatedLabel.csv","w")
        for i in range(numOfGraph):
            if i <numOfGraph/2:
                # generating 0-labeled graph
                G = np.zeros((numOfnode, numOfnode))
                #seed = np.random.choice(numOfnode - 5,1)[0]
                seed = 0
                G[seed][seed+3] = 1
                #G[seed+1][seed+2] = 1
                #G[seed+2][seed+3] = 1
                #G[seed][seed + 3] = 1

                graphs.append(G)
                # generating labels
                file.write("0\n")
            else:
                G = np.zeros((numOfnode, numOfnode))
                #seed = np.random.choice(numOfnode - 1, 1)[0]
                seed = 0

                #G[seed][seed + 1] = 1
                #G[seed][seed + 2] = 1
                #G[seed + 2][seed + 3] = 1
                G[seed + 1][seed + 4] = 1

                graphs.append(G)

                file.write("1\n")

        self.Xb = graphs
        self.Xb = np.array(self.Xb)
        file.close()

    def binaryAdjMatrixGen3(self, numOfGraph, numOfnode):
        #half labeled 0 half labeled 1
        graphs = []



        file = open("../dataset/simulatedLabel.csv","w")
        for i in range(numOfGraph):
            if i <numOfGraph/2:
                # generating 0-labeled graph
                G = np.zeros((numOfnode, numOfnode))
                #seed = np.random.choice(numOfnode - 5,1)[0]
                seed = 0
                G[seed][seed+1] = 1
                #G[seed+1][seed+2] = 1
                #G[seed+2][seed+3] = 1
                G[seed][seed + 3] = 1

                graphs.append(G)
                # generating labels
                file.write("0\n")
            else:
                G = np.zeros((numOfnode, numOfnode))
                #seed = np.random.choice(numOfnode - 1, 1)[0]
                seed = 0

                G[seed][seed + 1] = 1
                G[seed][seed + 2] = 1
                #G[seed + 2][seed + 3] = 1
                #G[seed + 3][seed + 4] = 1

                graphs.append(G)

                file.write("1\n")

        self.Xb = graphs
        self.Xb = np.array(self.Xb)
        file.close()



