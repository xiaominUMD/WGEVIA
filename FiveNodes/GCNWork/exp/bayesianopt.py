import os
import sys
import numpy as np
import csv
from hyperopt import STATUS_OK
#the loss should come from validation data set


multiRunInfo = "./bayesianResult/multiRunInfoReal.csv"
def objFunc(params,modelNo = '2'):
	epochs = 100
	
	jsonfolder = "../dataset/jsonBaReal/"
	of = "../exp/runtime/notused.csv"
	lof = "../exp/runtime/test.csv"
	record = "bayesianResult/test.csv"



	#generate new graphs json file with threshold T
	os.system("cd ../src\n"+ 
		"python3 jonsongen.py "+str(params.get('T'))+" "+jsonfolder+" "+sys.argv[1]+" "+sys.argv[2])
	os.system("echo JSONGEN finished")
	#graph2vec
	jsonfolder = "../GCNWork/dataset/jsonBaReal/"
	outfile = "test.csv"
	os.system("cd ../../graph2vec-master/\n"+
		"python3 src/graph2vec.py --dimensions "+str(params.get('dim'))+" --epochs "+str(epochs)+" --input-path "+jsonfolder+" --output-path ./features/"+outfile+" --origin "+sys.argv[2])
	#custom g2v swg2v
	#os.system("popd\npushd /Users/xiaomin/Desktop/swg2v/src/\n"+
	#"python3 wsgraph2vec.py "+str(params.get('dim'))+ " 4 "+jsonfolder+" "+outfile)

	os.system("echo graph2vec finished")
	#classifier
	outfile = "test.csv"
	os.system("cd ../src\n"+
		"python3 rc_datamining_dl_1d_cv.py ../../graph2vec-master/features/"+outfile+" "+of + " "+str(params.get('dim'))+" "+modelNo +" "+lof)
	os.system("echo classfication finished")
	#custom swg2v
#	os.system("popd\npushd /Users/xiaomin/Desktop/GCNWork/src\n"+
#		"python3 rc_datamining_dl_1d_cv.py /Users/xiaomin/Desktop/swg2v/embedding/"+outfile+" "+of + " "+str(params.get('dim'))+" "+modelNo +" "+lof)
#	os.system("echo classfication finished")

	RE = {}
	newary = []



	indx = 0
	with open(lof) as csvfile:
		spamreader = csv.reader(csvfile, delimiter=',')
		for row in spamreader:
			RE[str(indx)] = row[0]
			indx = indx + 1
	csvfile.close()

	lastLoss = RE['0']
	acc = RE['1']
	Tprint = params['T']
	DimPrint = params['dim']
	 
	recordstr = "acc: "+str(acc)+" lastlost: "+str(lastLoss)+" T: "+str(Tprint)+" DimPrint: "+str(DimPrint)
	newary.append(recordstr)

	with open(record, 'a', newline='') as csvfile:
	    spamwriter = csv.writer(csvfile)
	    for i in range(len(newary)):
	        spamwriter.writerow([newary[i]])
	csvfile.close()


	return {'loss': lastLoss, 'acc': acc, 'status': STATUS_OK}

#loss = objFunc(0.15,16,'0')
#print(loss)


from hyperopt import tpe
# Algorithm
tpe_algorithm = tpe.suggest

from hyperopt import Trials
# Trials object to track progress
bayes_trials = Trials()

from hyperopt import fmin

from hyperopt import hp
# Define the search space

T = [0]
dim = [80]
space = {
    #'T': hp.uniform('T', 0.1, 0.25),
    'T': hp.choice('T', T),
    'dim': hp.choice('dim', dim),
}

# Optimize
run = [1]
#run = [1,2,3]
bayesianRecord = []

for maxAtp in run:
	best = fmin(fn = objFunc, space = space, algo = tpe.suggest, max_evals = maxAtp, trials = bayes_trials)
	recordLine = "Attempts "+str(maxAtp)+" T: "+str(best['T'])+" dim: "+str(best['dim'])
	bayesianRecord.append(recordLine)
	print(best)


with open(multiRunInfo, 'a', newline='') as csvfile:
    spamwriter = csv.writer(csvfile)
    for i in range(len(bayesianRecord)):
        spamwriter.writerow([bayesianRecord[i]])

csvfile.close()
