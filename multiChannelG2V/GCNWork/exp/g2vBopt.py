import os
import sys
import numpy as np
import csv
from hyperopt import STATUS_OK
#the loss should come from validation data set


multiRunInfo = "./bayesianResult/infoDimG2vReal.csv"
def objFunc(params,modelNo = '2'):
	#print paras:
	Tprint = params['numOfT']
	DimPrint = params['singleDim']
	print("Current run numOfT: "+str(Tprint)+" singleDim: "+str(DimPrint))

	simuOrReal = 'simu'
	numOfT = params.get('numOfT')
	singleDim = params.get('singleDim')
	#of lof need to be modified both in and outside
	of = "./runtime/notused.csv"
	lof = "./runtime/lastLossBAYESn2vreal.csv"
	record = "./bayesianResult/DimG2vReal.csv"

	os.system("cd ../src\npython3 g2vpre.py "+str(numOfT)+" json "+simuOrReal+" "+str(singleDim)+" "+sys.argv[1])

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
	 
	recordstr = "acc: "+str(acc)+" lastlost: "+str(lastLoss)+" numOfT: "+str(Tprint)+" singleDim: "+str(DimPrint)
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

if sys.argv[1] == 'single':
	numOfT = [1]
else:
	numOfT = [40]
#numOfT = [2]
singleDim = [80]
space = {
    #'numOfT': hp.uniform('T', 0,1),
    'numOfT': hp.choice('numOfT',numOfT),
    'singleDim': hp.choice('singleDim', singleDim),
}

# Optimize
run = [1]
#run = [1,2,3]
bayesianRecord = []

for maxAtp in run:
	best = fmin(fn = objFunc, space = space, algo = tpe.suggest, max_evals = maxAtp, trials = bayes_trials)
	recordLine = "Attempts "+str(maxAtp)+" numOfT: "+str(best['numOfT'])+" singleDim: "+str(best['singleDim'])
	bayesianRecord.append(recordLine)
	print(best)


with open(multiRunInfo, 'a', newline='') as csvfile:
    spamwriter = csv.writer(csvfile)
    for i in range(len(bayesianRecord)):
        spamwriter.writerow([bayesianRecord[i]])

csvfile.close()
