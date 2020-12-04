from readData import ReadMCData
from convertBinaryGraph import ConvertBinaryGraph
from graph import graph
import sys

convertor = ConvertBinaryGraph(0)  # 0.15 the best so far

convertor.binaryAdjMatrixGen(100,50)

# write each graph to json, create a dataset for graph2vec
labelFile = open('../dataset/simulatedLabel.csv', "r")
gnnInFile = open('./simuGnnIn.txt', "a")

for i in range(len(convertor.Xb)):

    Gp = graph(convertor.Xb[i], [], None)
    if i == 0:
        Gp.ToGNNinputNumOfGraph(gnnInFile, len(convertor.Xb))
    # Gp.ToGNNinput(gnnInFile,labelFile)
    Gp.ToGNNinput100(gnnInFile, labelFile)

labelFile.close()
gnnInFile.close()

print("done")