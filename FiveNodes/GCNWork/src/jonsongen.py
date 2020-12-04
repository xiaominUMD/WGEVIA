from readData import ReadMCData
from convertBinaryGraph import ConvertBinaryGraph
from graph import graph
import sys
import os

# input format: -threshold FLOAT -jsonfolder STR
Threshold = float(sys.argv[1])  # 0.15
jsonfolder = sys.argv[2]  # "../dataset/json/"

print("current Threshold: " + str(Threshold) + "\n")
convertor = ConvertBinaryGraph(0)  # 0.15 the best so far

if sys.argv[3] == '1':
    print("gen five nodes type 1")
    convertor.binaryAdjMatrixGen1(1000, 5)
if sys.argv[3] == '2':
    print("gen five nodes type 2")
    convertor.binaryAdjMatrixGen2(1000, 5)
if sys.argv[3] == '3':
    print("gen five nodes type 3")
    convertor.binaryAdjMatrixGen3(1000, 5)


writerowcount = 1
os.system("cd "+jsonfolder+"\nrm *")
for i in range(convertor.Xb.shape[0]):
    f = open(jsonfolder + str(i) + ".json", "w+") #for original g2v pattern
    Gp = graph(convertor.Xb[i])

    if sys.argv[4] == '1':
        Gp.outjsonFullNodes(f)
    if sys.argv[4] == '2':
        Gp.outjsonFullNodesNF(f)

    f.close()

print("done")