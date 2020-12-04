import os
import sys
import numpy as np
import csv
from hyperopt import STATUS_OK
#the loss should come from validation data set

# 2 optimizable parameter. enter multiple element to use Bopt

multiRunInfo = "./result/runInfo.csv"

def objFunc(params,modelNo = '2'):
	#print paras:
	Tprint = params['numOfT']
	wliter = params['wliter']
	DimPrint = params['singleDim']
	print("Current run numOfT: "+str(Tprint)+" singleDim: "+str(DimPrint)+" wlIteration: "+str(wliter))
	numOfT = params.get('numOfT')
	singleDim = params.get('singleDim')
	#of lof need to be modified both in and outside
	lof = "./runtimeRecord/lastLoss.csv"
	record = "./result/mcsweACC.csv"
	os.system("cd ../src\npython3 g2vpre.py "+str(numOfT)+" json "+str(singleDim)+" "+str(wliter)+" "+modelNo+" "+sys.argv[1]+" "+sys.argv[2])
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
	recordstr = "acc: "+str(acc)+" lastlost: "+str(lastLoss)+" numOfT: "+str(Tprint)+" singleDim: "+str(DimPrint)+" wliter: "+str(wliter)
	newary.append(recordstr)
	with open(record, 'a', newline='') as csvfile:
	    spamwriter = csv.writer(csvfile)
	    for i in range(len(newary)):
	        spamwriter.writerow([newary[i]])
	csvfile.close()

	return {'loss': lastLoss, 'acc': acc, 'status': STATUS_OK}

from hyperopt import tpe
# Algorithm
tpe_algorithm = tpe.suggest

from hyperopt import Trials
# Trials object to track progress
bayes_trials = Trials()

from hyperopt import fmin
from hyperopt import hp

dstr = sys.argv[len(sys.argv)-1].split(',')
nTstr = sys.argv[len(sys.argv)-2].split(',')

nT = [int(i) for i in nTstr]
d = [int(i) for i in dstr]
print('Input nT is :'+str(nT))
print('Input d is :'+str(d))
# Define the search space
if sys.argv[1] == 'single':
	numOfT = [1]
else:
	numOfT = nT

singleDim = d
wliter = [4]



space = {
    'wliter': hp.choice('wliter',wliter),
    'numOfT': hp.choice('numOfT',numOfT),
    'singleDim': hp.choice('singleDim', singleDim),
}
# Optimize
run = [len(nT)*len(d)]
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
