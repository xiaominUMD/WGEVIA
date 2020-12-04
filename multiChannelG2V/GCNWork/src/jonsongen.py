from readData import ReadMCData
from convertBinaryGraph import ConvertBinaryGraph
from graph import graph
import sys
import os

#input format: -threshold FLOAT -jsonfolder STR
Threshold = float(sys.argv[1]) #0.15
jsonfolder = sys.argv[2] # "../dataset/json/"
embfolder = "../dataset/emb/"
n2vfeaturefolder = "../dataset/n2vFeatures/"

reader = ReadMCData('04', 9001, '../dataset/csvsReal/')
reader.readX()
reader.readY()
reader.writeY()
#reader.readXtest()
#reader.writeXcsv()
print("current Threshold: "+str(Threshold)+"\n")
convertor = ConvertBinaryGraph(Threshold) #0.15 the best so far
convertor.tonparyfloat(reader.X,reader.Y)
#convertor.Yratio()
convertor.storeNonZeros()
convertor.findTopRange()
convertor.emptyGraph()
#convertor.plotValueHistogram()
#convertor.originalMatrixplot(1000) #plot index 100 matrix
convertor.convert()
convertor.gatherEdgeInfoAbs()

#write each graph to json, create a dataset for graph2vec

os.system("cd /home/xiaomin/Desktop/node2vec/myGraph\nrm *")
os.system("cd /home/xiaomin/Desktop/node2vec/emb\nrm *")

for i in range(convertor.Xb.shape[0]):
    f= open(jsonfolder+str(i)+".json","w+")
    f1= open(embfolder+str(i)+".emb","w+")
    
    Gp = graph(convertor.Xb[i],convertor.X[i],convertor.edgeWeightSumPerNode[i])
    #Gp.plot()
    Gp.outemb(f1)
    f1.close()

    os.system("mv ../dataset/emb/"+str(i)+".emb /home/xiaomin/Desktop/node2vec/myGraph")
    os.system("cd /home/xiaomin/Desktop/node2vec\npython2 src/main.py --input myGraph/"+str(i)+".emb --output emb/"+str(i)+".emd --weighted")
    os.system("mv /home/xiaomin/Desktop/node2vec/emb/"+str(i)+".emd "+n2vfeaturefolder)

    f2 = open(n2vfeaturefolder+str(i)+".emd","r")
    Gp.getNodeFeatures(f2)
    f2.close()

    Gp.outjson(f)
    f.close()
    
    

print("done")
