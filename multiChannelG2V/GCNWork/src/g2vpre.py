from readData import ReadMCData
from convertBinaryGraph import ConvertBinaryGraph
from graph import graph
import sys
import os

def genJSONwithThreshold(convertor,T, jsonfolder,step):
    
    #convertor.Yratio()
    #convertor.storeNonZeros()
    
    #convertor.emptyGraph()
    #convertor.plotValueHistogram()
    #convertor.originalMatrixplot(1000) #plot index 100 matrix
    
    #convertor.convertRangeT(T,step)
    convertor.convertLessT(T,step)
    convertor.gatherEdgeInfoAbs()

    #write each graph to json, create a dataset for graph2vec

    for i in range(convertor.Xb.shape[0]):
        f = open(jsonfolder+str(i)+".json","w+")
        Gp = graph(convertor.Xb[i],convertor.X[i],convertor.edgeWeightSumPerNode[i])
        #Gp.outjson(f)
        Gp.outjsonFullNodes(f)
        f.close()
        
    print("Threshold " + str(T) + " subGraph generated\n")

#input format: -threshold FLOAT -jsonfolder STR
Threshold = sys.argv[1] #NUM
jsonfolder = sys.argv[2] # "../dataset/json"
dataset = sys.argv[3] #simu or real
dim = sys.argv[4] #dimention of g2v
g2vout = "../../GCNWork/dataset/multiG2V/g2vFeatures/"

if dataset == 'simu':
    reader = ReadMCData('04', 1201, 'cd ../../../MCSWE1.1origin/mcDataset/csvs/')
if dataset == 'real':
    reader = ReadMCData('04', 9001, 'cd ../../../MCSWE1.1origin/mcDataset/csvsReal1/')

reader.readX()
reader.readY()
reader.writeY()
#reader.readXtest()
#reader.writeXcsv()
convertor = ConvertBinaryGraph(0) #0.15 the best so far
convertor.tonparyfloat(reader.X,reader.Y)
convertor.findTopRange()

top = convertor.allTop
Ts = []
step = float(top)/(int(Threshold))
for i in range(int(Threshold)):
    Ts.append(i*step)

#clean previous g2vi.csv files and json folder of previous run
os.system("cd ../dataset/multiG2V\nrm -rf [a-zA-Z]*[0-9]")
os.system("cd ../dataset/multiG2V/g2vFeatures\nrm g* c*")

for i in range(len(Ts)):
    if sys.argv[5] == 'single':
        Ts[i] = 0.196
        step = 0
    print("current ThresholdS: "+str(Ts[i])+" of top: "+str(top)+"\n")
    jsfd = jsonfolder+str(i)
    os.system("cd ../dataset/multiG2V\nmkdir "+jsfd)
    jsfd = "../../GCNWork/dataset/multiG2V/"+jsfd + '/'
    genJSONwithThreshold(convertor, float(Ts[i]), jsfd,step)
    g2vfile = "g2v"+str(i)+".csv"
    os.system("python3 ../../graph2vec-master/src/graph2vec.py --dimensions "+dim+" --epochs 100 --input-path "+jsfd+" --output-path "+g2vout+g2vfile)
    os.system("echo graph2vec finished")

#combine features
for i in range(len(Ts)):
    if i > 0:
        os.system("cd ../dataset/multiG2V/g2vFeatures\nsed -i 's/^[^,]*[0-9a-z]//' g2v"+str(i)+".csv")
os.system("cd ../dataset/multiG2V/g2vFeatures\npaste g* > combinedFeature.csv")
#train model
of = "../exp/runtime/notused.csv"
lof = "../exp/runtime/lastLossBAYESn2vreal.csv"
os.system("python3 ./rc_datamining_dl_1d_cv.py ../dataset/multiG2V/g2vFeatures/combinedFeature.csv "+of + " "+dim+" "+'2' +" "+lof)
os.system("echo classfication finished")
