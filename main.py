import sys
import os
import argparse
import csv
import datetime

parser = argparse.ArgumentParser()
parser.add_argument('--nT', action="store", default='10',type=str)
parser.add_argument('--d', action="store", default='8',type=str)
parser.add_argument('--w', action="store", default='4',type=str)
parser.add_argument('--opcode', action="store", default='8',type=str)
parser.add_argument('--workers', action="store", default='4',type=str)

args = parser.parse_args()

#five nodes
if args.opcode == '1':
	with open('./FiveNodes/GCNWork/exp/result/fiveNodesACC.csv', 'a') as csvfile:
		spamwriter = csv.writer(csvfile, delimiter=',')
		spamwriter.writerow([datetime.datetime.now()])
		spamwriter.writerow(['five node case a (01 vs 01,34) using G2V , opcode 1, d = 80 '])

		csvfile.close()
	os.system("cd FiveNodes/GCNWork/exp\nTF_CPP_MIN_LOG_LEVEL=\"3\" python3 -W ignore bayesianopt.py 1 1")
	os.system("cd FiveNodes/GCNWork/src/\nbash modelrun3.bash\nbash modelrun1.bash\nbash modelrun0.bash")


elif args.opcode == '2':
	with open('./FiveNodes/GCNWork/exp/result/fiveNodesACC.csv', 'a') as csvfile:
		spamwriter = csv.writer(csvfile, delimiter=',')
		spamwriter.writerow(['five node case b (01 vs 34) using G2V , opcode 2, d = 80 '])

		csvfile.close()
	os.system("cd FiveNodes/GCNWork/exp\nTF_CPP_MIN_LOG_LEVEL=\"3\" python3 -W ignore bayesianopt.py 2 1")
	os.system("cd FiveNodes/GCNWork/src/\nbash modelrun3.bash\nbash modelrun1.bash\nbash modelrun0.bash")

elif args.opcode == '3':
	with open('./FiveNodes/GCNWork/exp/result/fiveNodesACC.csv', 'a') as csvfile:
		spamwriter = csv.writer(csvfile, delimiter=',')
		spamwriter.writerow(['five node case c (0102 vs 0103) using G2V , opcode 3, d = 80 '])

		csvfile.close()
	os.system("cd FiveNodes/GCNWork/exp\nTF_CPP_MIN_LOG_LEVEL=\"3\" python3 -W ignore bayesianopt.py 3 1")
	os.system("cd FiveNodes/GCNWork/src/\nbash modelrun3.bash\nbash modelrun1.bash\nbash modelrun0.bash")

elif args.opcode == '4':
	with open('./FiveNodes/GCNWork/exp/result/fiveNodesACC.csv', 'a') as csvfile:
		spamwriter = csv.writer(csvfile, delimiter=',')
		spamwriter.writerow(['five node case a (01 vs 01,34) using SG2V , opcode 4, d = 80 '])

		csvfile.close()
	os.system("cd FiveNodes/GCNWork/exp\nTF_CPP_MIN_LOG_LEVEL=\"3\" python3 -W ignore bayesianopt.py 1 2")
	os.system("cd FiveNodes/GCNWork/src/\nbash modelrun3.bash\nbash modelrun1.bash\nbash modelrun0.bash")

elif args.opcode == '5':
	with open('./FiveNodes/GCNWork/exp/result/fiveNodesACC.csv', 'a') as csvfile:
		spamwriter = csv.writer(csvfile, delimiter=',')
		spamwriter.writerow(['five node case b (01 vs 34) using SG2V , opcode 5, d = 80 '])

		csvfile.close()
	os.system("cd FiveNodes/GCNWork/exp\nTF_CPP_MIN_LOG_LEVEL=\"3\" python3 -W ignore bayesianopt.py 2 2")
	os.system("cd FiveNodes/GCNWork/src/\nbash modelrun3.bash\nbash modelrun1.bash\nbash modelrun0.bash")

elif args.opcode == '6':
	with open('./FiveNodes/GCNWork/exp/result/fiveNodesACC.csv', 'a') as csvfile:
		spamwriter = csv.writer(csvfile, delimiter=',')
		spamwriter.writerow(['five node case c (0102 vs 0103) using SG2V , opcode 6, d = 80 '])

		csvfile.close()
	os.system("cd FiveNodes/GCNWork/exp\nTF_CPP_MIN_LOG_LEVEL=\"3\" python3 -W ignore bayesianopt.py 3 2")
	os.system("cd FiveNodes/GCNWork/src/\nbash modelrun3.bash\nbash modelrun1.bash\nbash modelrun0.bash")


elif args.opcode == '7':
	os.system("cd powerful-gnns\npython3 main.py --dataset FN010134")

elif args.opcode == '8':
	os.system("cd powerful-gnns\npython3 main.py --dataset FN0134")

elif args.opcode == '9':
	os.system("cd powerful-gnns\npython3 main.py --dataset FN01020103")

#	10: MCSWE on SIMU
elif args.opcode == '10':
	with open('./mgenia_dataflow/exp/result/mgeniaACC.csv', 'a') as csvfile:
		spamwriter = csv.writer(csvfile, delimiter=',')
		spamwriter.writerow(['MGENIA on SIMU, opcode 10 nT: ' + str(args.nT)+' d: '+str(args.d)+' w: '+str(args.w)])

		csvfile.close()
	os.system("cd mgenia_dataflow/weightedGraphs\nrm d*\nrm l*\ncp ../../MCSWE1.1origin/mcDataset/csvs/* .")
	os.system("cd mgenia_dataflow/exp\nTF_CPP_MIN_LOG_LEVEL=\"3\" python3 -W ignore g2vBopt.py train posT lessCut nonAbs channelnum "+args.nT+" "+args.d+" "+args.w)
	os.system("cd mgenia_dataflow/src/util\nbash modelrun3.bash\nbash modelrun1.bash\nbash modelrun0.bash")

elif args.opcode == 'origin_10':
	with open('./MCSWE1.1origin/multiChannelGen/exp/result/mgeniaACC.csv', 'a') as csvfile:
		spamwriter = csv.writer(csvfile, delimiter=',')
		spamwriter.writerow(['MGENIA origin on SIMU, opcode origin_10 nT: ' + str(args.nT)+' d: '+str(args.d)+' w: '+str(args.w)])

		csvfile.close()
	os.system("cd MCSWE1.1origin/weightedGraphs\nrm d*\nrm l*\ncp ../mcDataset/csvs/* .")
	os.system("cd MCSWE1.1origin/multiChannelGen/exp\nTF_CPP_MIN_LOG_LEVEL=\"3\" python3 -W ignore g2vBopt.py train posT lessCut nonAbs channelnum "+args.nT+" "+args.d+" "+args.w)
	os.system("cd MCSWE1.1origin/multiChannelGen/src\nbash modelrun3.bash\nbash modelrun1.bash\nbash modelrun0.bash")

#	12: MCSWE on REAL
elif args.opcode == '12':
	with open('./mgenia_dataflow/exp/result/mgeniaACC.csv', 'a') as csvfile:
		spamwriter = csv.writer(csvfile, delimiter=',')
		spamwriter.writerow(['MGENIA on REAL, opcode 12 nT: ' + str(args.nT)+' d: '+str(args.d)+' w: '+str(args.w)])

		csvfile.close()
	os.system("cd mgenia_dataflow/weightedGraphs\nrm d*\nrm l*\ncp ../../MCSWE1.1origin/mcDataset/csvsReal2/data* .\ncp ../../MCSWE1.1origin/mcDataset/csvsReal2/label* .")
	os.system("cd mgenia_dataflow/exp\nTF_CPP_MIN_LOG_LEVEL=\"3\" python3 -W ignore g2vBopt.py train posT lessCut nonAbs 4worker 4 "+args.nT+" "+args.d+" "+args.w)
	os.system("cd mgenia_dataflow/src/util\nbash modelrun3.bash\nbash modelrun1.bash\nbash modelrun0.bash")

elif args.opcode == 'origin_12':
	with open('./MCSWE1.1origin/multiChannelGen/exp/result/mgeniaACC.csv', 'a') as csvfile:
		spamwriter = csv.writer(csvfile, delimiter=',')
		spamwriter.writerow(['MGENIA origin on REAL, opcode origin_12 nT: ' + str(args.nT)+' d: '+str(args.d)+' w: '+str(args.w)])

		csvfile.close()
	os.system("cd MCSWE1.1origin/weightedGraphs\nrm d*\nrm l*\ncp ../mcDataset/csvsReal2/data* .\ncp ../mcDataset/csvsReal2/label* .")
	os.system("cd MCSWE1.1origin/multiChannelGen/exp\nTF_CPP_MIN_LOG_LEVEL=\"3\" python3 -W ignore g2vBopt.py train posT lessCut nonAbs 4worker 4 "+args.nT+" "+args.d+" "+args.w)
	os.system("cd MCSWE1.1origin/multiChannelGen/src\nbash modelrun3.bash\nbash modelrun1.bash\nbash modelrun0.bash")

# 	13: G2V on SIMU
elif args.opcode == '13':
	with open('./multiChannelG2V/GCNWork/exp/result/g2vACC.csv', 'a') as csvfile:
		spamwriter = csv.writer(csvfile, delimiter=',')
		spamwriter.writerow([datetime.datetime.now()])
		spamwriter.writerow(['G2V on SIMU , opcode 13'])

		csvfile.close()
	os.system("cd multiChannelG2V/GCNWork/exp\nTF_CPP_MIN_LOG_LEVEL=\"3\" python3 -W ignore g2vBopt.py single")
	os.system("cd multiChannelG2V/GCNWork/src/\nbash modelrun3.bash\nbash modelrun1.bash\nbash modelrun0.bash")

#	15: G2V on REAL
elif args.opcode == '15':
	with open('./parallelMCg2v/multiChannelGen/exp/result/mgeniaACC.csv', 'a') as csvfile:
		spamwriter = csv.writer(csvfile, delimiter=',')
		spamwriter.writerow(['G2V on REAL, opcode 15 nT: ' + str(args.nT)+' d: '+str(args.d)])

		csvfile.close()
	os.system("cd parallelMCg2v/weightedGraphs\nrm d*\nrm l*\ncp ../../MCSWE1.1origin/mcDataset/csvsReal2/data* .\ncp ../../MCSWE1.1origin/mcDataset/csvsReal2/label* .")
	os.system("cd parallelMCg2v/multiChannelGen/exp\nTF_CPP_MIN_LOG_LEVEL=\"3\" python3 -W ignore g2vBopt.py single degree "+args.nT+" "+args.d)
	os.system("cd parallelMCg2v/multiChannelGen/src\nbash modelrun3.bash\nbash modelrun1.bash\nbash modelrun0.bash")

#	16: powerGNN on SIMU
elif args.opcode == '16':
	os.system("cd powerful-gnns\nTF_CPP_MIN_LOG_LEVEL=\"3\" python3 -W ignore main.py --dataset SIMU")

#	18: powerGNN on REAL
elif args.opcode == '18':
	os.system("cd powerful-gnns\nTF_CPP_MIN_LOG_LEVEL=\"3\" python3 -W ignore main.py --dataset REAL2")

#	21: Multi-channel G2V on REAL
elif args.opcode == '21':
	with open('./parallelMCg2v/multiChannelGen/exp/result/mgeniaACC.csv', 'a') as csvfile:
		spamwriter = csv.writer(csvfile, delimiter=',')
		spamwriter.writerow(['Multi-Channel G2V on REAL, opcode 21 nT: ' + str(args.nT)+' d: '+str(args.d)])

		csvfile.close()
	os.system("cd parallelMCg2v/weightedGraphs\nrm d*\nrm l*\ncp ../../MCSWE1.1origin/mcDataset/csvsReal2/data* .\ncp ../../MCSWE1.1origin/mcDataset/csvsReal2/label* .")
	os.system("cd parallelMCg2v/multiChannelGen/exp\nTF_CPP_MIN_LOG_LEVEL=\"3\" python3 -W ignore g2vBopt.py multi degree "+args.nT+" "+args.d)
	os.system("cd parallelMCg2v/multiChannelGen/src\nbash modelrun3.bash\nbash modelrun1.bash\nbash modelrun0.bash")

#	22: MUlti-channel G2V (index label) on REAL
elif args.opcode == '22':
	with open('./parallelMCg2v/multiChannelGen/exp/result/mgeniaACC.csv', 'a') as csvfile:
		spamwriter = csv.writer(csvfile, delimiter=',')
		spamwriter.writerow(['Multi-Channel G2V (index label) on REAL, opcode 22 nT: ' + str(args.nT)+' d: '+str(args.d)])

		csvfile.close()
	os.system("cd parallelMCg2v/weightedGraphs\nrm d*\nrm l*\ncp ../../MCSWE1.1origin/mcDataset/csvsReal2/data* .\ncp ../../MCSWE1.1origin/mcDataset/csvsReal2/label* .")
	os.system("cd parallelMCg2v/multiChannelGen/exp\nTF_CPP_MIN_LOG_LEVEL=\"3\" python3 -W ignore g2vBopt.py multi index "+args.nT+" "+args.d)
	os.system("cd parallelMCg2v/multiChannelGen/src\nbash modelrun3.bash\nbash modelrun1.bash\nbash modelrun0.bash")

#	23: Multi-channel G2V on SIMU
elif args.opcode == '23':
	with open('./parallelMCg2v/multiChannelGen/exp/result/mgeniaACC.csv', 'a') as csvfile:
		spamwriter = csv.writer(csvfile, delimiter=',')
		spamwriter.writerow(['Multi-Channel G2V on SIMU, opcode 23 nT: ' + str(args.nT)+' d: '+str(args.d)])

		csvfile.close()
	os.system("cd parallelMCg2v/weightedGraphs\nrm d*\nrm l*\ncp ../../MCSWE1.1origin/mcDataset/csvs/* .")
	os.system("cd parallelMCg2v/multiChannelGen/exp\nTF_CPP_MIN_LOG_LEVEL=\"3\" python3 -W ignore g2vBopt.py multi degree "+args.nT+" "+args.d)
	os.system("cd parallelMCg2v/multiChannelGen/src\nbash modelrun3.bash\nbash modelrun1.bash\nbash modelrun0.bash")

#	24: MUlti-channel G2V (index label) on SIMU
elif args.opcode == '24':
	with open('./parallelMCg2v/multiChannelGen/exp/result/mgeniaACC.csv', 'a') as csvfile:
		spamwriter = csv.writer(csvfile, delimiter=',')
		spamwriter.writerow(['Multi-Channel G2V (index label) on SIMU, opcode 24 nT: ' + str(args.nT)+' d: '+str(args.d)])

		csvfile.close()
	os.system("cd parallelMCg2v/weightedGraphs\nrm d*\nrm l*\ncp ../../MCSWE1.1origin/mcDataset/csvs/data* .\ncp ../../MCSWE1.1origin/mcDataset/csvs/label* .")
	os.system("cd parallelMCg2v/multiChannelGen/exp\nTF_CPP_MIN_LOG_LEVEL=\"3\" python3 -W ignore g2vBopt.py multi index "+args.nT+" "+args.d)
	os.system("cd parallelMCg2v/multiChannelGen/src\nbash modelrun3.bash\nbash modelrun1.bash\nbash modelrun0.bash")

#functions
elif args.opcode == 'WGEVIAmemTrain':
	with open('./MCSWE1.1origin/multiChannelGen/exp/result/mgeniaACC.csv', 'a') as csvfile:
		spamwriter = csv.writer(csvfile, delimiter=',')
		spamwriter.writerow(['opcode WGEVIAmemTrain: ' + str(args.nT)+' d: '+str(args.d)+' w: '+str(args.w)])

		csvfile.close()
	os.system("cd MCSWE1.1origin/multiChannelGen/exp\nTF_CPP_MIN_LOG_LEVEL=\"3\" python3 -W ignore g2vBopt.py train posT lessCut nonAbs 4worker "+args.workers+" "+args.nT+" "+args.d+" "+args.w)
	os.system("cd MCSWE1.1origin/multiChannelGen/src\nbash modelrun3.bash\nbash modelrun1.bash\nbash modelrun0.bash")

elif args.opcode == 'WGEVIAmemProject':
	with open('./MCSWE1.1origin/multiChannelGen/exp/result/mgeniaACC.csv', 'a') as csvfile:
		spamwriter = csv.writer(csvfile, delimiter=',')
		spamwriter.writerow(['opcode WGEVIAmemProject: ' + str(args.nT)+' d: '+str(args.d)+' w: '+str(args.w)])

		csvfile.close()
	os.system("cd MCSWE1.1origin/multiChannelGen/exp\nTF_CPP_MIN_LOG_LEVEL=\"3\" python3 -W ignore g2vBopt.py inference posT lessCut nonAbs 4worker "+args.workers+" "+args.nT+" "+args.d+" "+args.w)
	os.system("cd MCSWE1.1origin/multiChannelGen/src\nbash modelrun3.bash\nbash modelrun1.bash\nbash modelrun0.bash")

elif args.opcode == 'WGEVIAcoreTrain':
	with open('./MCSWE1.1origin/multiChannelGen/exp/result/mgeniaACC.csv', 'a') as csvfile:
		spamwriter = csv.writer(csvfile, delimiter=',')
		spamwriter.writerow(['opcode WGEVIAcoreTrain: ' + str(args.nT)+' d: '+str(args.d)+' w: '+str(args.w)])

		csvfile.close()
	os.system("cd MCSWE1.1origin/multiChannelGen/exp\nTF_CPP_MIN_LOG_LEVEL=\"3\" python3 -W ignore g2vBopt.py train posT lessCut nonAbs corenum "+args.nT+" "+args.d+" "+args.w)
	os.system("cd MCSWE1.1origin/multiChannelGen/src\nbash modelrun3.bash\nbash modelrun1.bash\nbash modelrun0.bash")

elif args.opcode == 'WGEVIAcoreProject':
	with open('./MCSWE1.1origin/multiChannelGen/exp/result/mgeniaACC.csv', 'a') as csvfile:
		spamwriter = csv.writer(csvfile, delimiter=',')
		spamwriter.writerow(['opcode WGEVIAcoreProject: ' + str(args.nT)+' d: '+str(args.d)+' w: '+str(args.w)])

		csvfile.close()
	os.system("cd MCSWE1.1origin/multiChannelGen/exp\nTF_CPP_MIN_LOG_LEVEL=\"3\" python3 -W ignore g2vBopt.py inference posT lessCut nonAbs corenum "+args.nT+" "+args.d+" "+args.w)
	os.system("cd MCSWE1.1origin/multiChannelGen/src\nbash modelrun3.bash\nbash modelrun1.bash\nbash modelrun0.bash")

elif args.opcode == 'WGEVIAfastTrain':
	with open('./MCSWE1.1origin/multiChannelGen/exp/result/mgeniaACC.csv', 'a') as csvfile:
		spamwriter = csv.writer(csvfile, delimiter=',')
		spamwriter.writerow(['opcode WGEVIAfastTrain: ' + str(args.nT)+' d: '+str(args.d)+' w: '+str(args.w)])

		csvfile.close()
	os.system("cd MCSWE1.1origin/multiChannelGen/exp\nTF_CPP_MIN_LOG_LEVEL=\"3\" python3 -W ignore g2vBopt.py train posT lessCut nonAbs channelnum "+args.nT+" "+args.d+" "+args.w)
	os.system("cd MCSWE1.1origin/multiChannelGen/src\nbash modelrun3.bash\nbash modelrun1.bash\nbash modelrun0.bash")

elif args.opcode == 'WGEVIAfastProject':
	with open('./MCSWE1.1origin/multiChannelGen/exp/result/mgeniaACC.csv', 'a') as csvfile:
		spamwriter = csv.writer(csvfile, delimiter=',')
		spamwriter.writerow(['opcode WGEVIAfastProject: ' + str(args.nT)+' d: '+str(args.d)+' w: '+str(args.w)])

		csvfile.close()
	os.system("cd MCSWE1.1origin/multiChannelGen/exp\nTF_CPP_MIN_LOG_LEVEL=\"3\" python3 -W ignore g2vBopt.py inference posT lessCut nonAbs channelnum "+args.nT+" "+args.d+" "+args.w)
	os.system("cd MCSWE1.1origin/multiChannelGen/src\nbash modelrun3.bash\nbash modelrun1.bash\nbash modelrun0.bash")

elif args.opcode == 'mgenia_dataflow':
	os.system("cd mgenia_dataflow/weightedGraphs\nrm d*\nrm l*\ncp ../../MCSWE1.1origin/mcDataset/csvs/* .")
	os.system("cd mgenia_dataflow/exp\nTF_CPP_MIN_LOG_LEVEL=\"3\" python3 -W ignore g2vBopt.py train posT lessCut nonAbs channelnum")

else:
	print("ERROR: not a proper opcode, Please check README.md for instructions")



#deleted experiments:
'''
elif args.opcode == '20':
	os.system("cd parallelMCg2v/weightedGraphs\nrm d*\nrm l*\ncp ../../MCSWE1.1origin/mcDataset/csvsReal/* .")
	os.system("cd parallelMCg2v/multiChannelGen/exp\nTF_CPP_MIN_LOG_LEVEL=\"3\" python3 -W ignore g2vBopt.py multi degree")

elif args.opcode == '17':
	os.system("cd powerful-gnns\nTF_CPP_MIN_LOG_LEVEL=\"3\" python3 -W ignore main.py --dataset REAL1")

elif args.opcode == '14':
	os.system("cd parallelMCg2v/weightedGraphs\nrm d*\nrm l*\ncp ../../MCSWE1.1origin/mcDataset/csvsReal/* .")
	os.system("cd parallelMCg2v/multiChannelGen/exp\nTF_CPP_MIN_LOG_LEVEL=\"3\" python3 -W ignore g2vBopt.py single degree")

elif args.opcode == '12':
	os.system("cd MCSWE1.1origin/weightedGraphs\nrm d*\nrm l*\ncp ../mcDataset/csvsReal2/* .")
	os.system("cd MCSWE1.1origin/multiChannelGen/exp\nTF_CPP_MIN_LOG_LEVEL=\"3\" python3 -W ignore g2vBopt.py train posT lessCut nonAbs 4worker 4")

elif args.opcode == '23':
	os.system("cd MCSWE1.1origin/weightedGraphs\nrm d*\nrm l*\ncp ../mcDataset/csvsReal/* .")
	os.system("cd MCSWE1.1origin/multiChannelGen/exp\nTF_CPP_MIN_LOG_LEVEL=\"3\" python3 -W ignore g2vBopt.py train posT lessCut nonAbs corenum")

elif args.opcode == '24':
	os.system("cd MCSWE1.1origin/weightedGraphs\nrm d*\nrm l*\ncp ../mcDataset/csvsReal/* .")
	os.system("cd MCSWE1.1origin/multiChannelGen/exp\nTF_CPP_MIN_LOG_LEVEL=\"3\" python3 -W ignore g2vBopt.py train posT lessCut abs channelnum")

elif args.opcode == '25':
	os.system("cd MCSWE1.1origin/weightedGraphs\nrm d*\nrm l*\ncp ../mcDataset/csvsReal/* .")
	os.system("cd MCSWE1.1origin/multiChannelGen/exp\nTF_CPP_MIN_LOG_LEVEL=\"3\" python3 -W ignore g2vBopt.py train negT lessCut nonAbs channelnum")

elif args.opcode == '26':
	os.system("cd MCSWE1.1origin/weightedGraphs\nrm d*\nrm l*\ncp ../mcDataset/csvsReal/* .")
	os.system("cd MCSWE1.1origin/multiChannelGen/exp\nTF_CPP_MIN_LOG_LEVEL=\"3\" python3 -W ignore g2vBopt.py train negT rangeCut nonAbs channelnum")

elif args.opcode == '27':
	os.system("cd MCSWE1.1origin/weightedGraphs\nrm d*\nrm l*\ncp ../mcDataset/csvsReal/* .")
	os.system("cd MCSWE1.1origin/multiChannelGen/exp\nTF_CPP_MIN_LOG_LEVEL=\"3\" python3 -W ignore g2vBopt.py train posT rangeCut nonAbs channelnum")

elif args.opcode == '28':
	os.system("cd MCSWE1.1origin/weightedGraphs\nrm d*\nrm l*\ncp ../mcDataset/csvsReal/* .")
	os.system("cd MCSWE1.1origin/multiChannelGen/exp\nTF_CPP_MIN_LOG_LEVEL=\"3\" python3 -W ignore g2vBopt.py train posT rangeCut abs channelnum")
	
elif args.opcode == '11':
	os.system("cd MCSWE1.1origin/weightedGraphs\nrm d*\nrm l*\ncp ../mcDataset/csvsReal3/* .")
	os.system("cd MCSWE1.1origin/multiChannelGen/exp\nTF_CPP_MIN_LOG_LEVEL=\"3\" python3 -W ignore g2vBopt.py train posT lessCut nonAbs corenum")
'''