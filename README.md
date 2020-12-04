# WGEVIA
WGEVIA is a new graph embedding algorithm for microcircuits in computational neuroscience or  
any weighted graphs that share similar characteristics. The WGEVIA software packge contains WGEVIA  
graph embedding; it also includes standard deep learning models for classification based on  
generated graph embedding features.  

For details of WGEVIA algorithm, please refer to the WGEVIA paper:  
link  

If you find that WGEVIA is useful to your research, please cite the published paper:  
WGEVIA: Graph Level Embedding for Microcircuit Data  

Any issues or questions about software can raise issue on Github or contact the author of WGEVIA paper.  

## WGEVIA main software:
The WGEVIA software is under ./MCSWE1.1origin sub-directory.

### Package requirements and installation with pip:  
WGEVIA is written in Python 3. To run the software, Phyton 3.6 should be installed with  
required python packages. Installation commands for required packages are listed as follows:   
```
pip3 install numpy  
pip3 install sklearn  
pip3 install tensorflow==1.14.0  
pip3 install hyperopt  
pip3 install networkx  
pip3 install scipy  
pip3 install gensim  
pip3 install hashlib  
```

### Inputs, outputs, and file format:
### Inputs:
Inputs required by WGEVIA software are a set of weighted graph data G = {g_1, g_2,...,g_m}. g_k is a weighted adjacency matrix.    
Totally m+1 files are needed. m is the number of graphs. All weighted graphs' adjacency matrix should be saved in m CSV files with naming data#.csv

A set of graphs' labels L = {l_1, l_2,...,l_m} is used in the classification stage of WGEVIA for supervised learning tasks. The label file is not needed 
if users utilize WGEVIA to generate embedding features for input graphs. All labels for weighted graphs should be put in file labelAll.csv.  
The indexing of labels in labelALl.csv file should be consistent with indexing of graph files data#.csv. For instance, the third label in 
labelAll.csv is the label for the graph saved in data3.csv.  

Before runing the software, copy all graph files and the label file to the following directory:   
./MCSWE1.1origin/weightedGraphs

#### Input file format:
Example files of data#.csv and labelAll.csv are in the following directory:    
./MCSWE1.1origin/weightedGraphs  

### Outputs:
WGEVIA will output the generated graph embedding features as a CSV file. It will also report the classification results based on those generated graph 
features. 

Generated embedding features will be saved in the following file:  
./MCSWE1.1ORIGIN/multiChannelGen/channels/g2vFeatures/combinedFeatures.csv  

Classification result based on generated graph features will be saved in the following file:  
./MCSWE1.1ORIGIN/multiChannelGen/exp/result/DimG2v.csv  

### Hyper-parameter optimization with Bayesian Optimization:
Modify Tn, d, wliter in file:  
./MCSWE1.1ORIGIN/multiChannelGen/exp/g2vBopt.py   
to examine different Tn and d options.  
Hyper-parameters need to be consistent for a projecting mode with new data following a train mode for building a new model.  

Tn : number of total channel thresholds  
d : single output feature dimension of one channel  
wliter:  number of iteration the feature extractor runs 

Set Tn, d and wliter to array of multiple value and Bayesian optimization will show the best combination.   
The default setting is Tn=10 d=8 wliter=4  

### Run WGEVIA algorithm with classification using MLP machine learning model
WGEVIA can be used in two modes:  
Train mode: when user don't have a Trained WGEVIA model and want to build a WGEVIA model and generate embedding features for given graphs at the same time.  
Projecting mode: when user wants to use trained WGEVIA model with old graphs and want to project new graphs data into embedding feature without modifying trained WGEVIA model. A Projecting mode have to be used after completely runing a Train mode with same hyper-parameters.    
A MLP model is used to check embedding quality for both Train and Projecting mode. So labels for graphs are required as input for both modes.  
```
cd .
python3 main.py [opcode]
```
opcode:  
	WGEVIAfastTrain : run WGEVIA method in Train mode parallel with a process pool of channel amount  
	WGEVIAfastProject : run WGEVIA method in Projecting mode parallel with a process pool of channel amount  
	WGEVIAcoreTrain : run WGEVIA method in Train mode parallel with a process pool of CPU core amount  
	WGEVIAcoreProject : run WGEVIA method in Projecting mode parallel with a process pool of CPU core amount  	
	WGEVIAmemTrain # : run WGEVIA method in Train mode parallel with a process pool of # workers  
	WGEVIAmemProject # : run WGEVIA method in Projecting mode parallel with a process pool of # workers  

example:
```
python3 main.py --opcode WGEVIAfastTrain --nT 10 --d 8 --w 4
python3 main.py --opcode WGEVIAfastProject --nT 10 --d 8 --w 4
python3 main.py --opcode WGEVIAcoreTrain --nT 10 --d 8 --w 4
python3 main.py --opcode WGEVIAcoreProject --nT 10 --d 8 --w 4
python3 main.py --opcode WGEVIAmemTrain --workers 4 --nT 10 --d 8 --w 4
python3 main.py --opcode WGEVIAmemProject --workers 4 --nT 10 --d 8 --w 4
```
WGEVIAfast* is recommended if your data set is not large and your CPU RAM amount is enough.  
WGEVIAmem* with small # is recommended if for the case of "out of memory" issue with WGEVIAfast or WGEVIAcore options.  
For Project mode, keep hyper-parameter nT, d, and w the same with corresponding Train mode. Project mode need to be executed after a Train mode which stores trained Doc2vec model  

## Comparison experiments
All experiments for the WGEVIA paper are packaged in current directory.  
The Graph2vec(G2V) and PowerGNN methods used for experiments are developed by other researchers and  
can be found in following links:  
Graph2vec : https://github.com/benedekrozemberczki/graph2vec   
PowerGNN : https://github.com/weihua916/powerful-gnns   

If user wants to use these two software directly, please download software from those link and follow instructions there.  
We put codes here only aim to provide repeatability of experiments, and inputs are fixed to the experiments mentioned in  
WGEVIA paper. Related experiments are wrapped in main.py, and can be executed with required package installed.    

### Additional requirements:
```
pip3 install torch  
pip3 install tqdm
```

### How to run experiments mentioned in WGEVIA paper:
```
cd .
python3 main.py [opcode]
```
opcode:  
	1: five node case a (01 vs 01,34) using G2V  
	2: five node case b (01 vs 34) using G2V  
	3: five node case c (0102 vs 0103) using G2V  
	4: five node case a (01 vs 01,34) using SG2V  
	5: five node case b (01 vs 34) using SG2V  
	6: five node case c (0102 vs 0103) using SG2V  
	7: five node case a (01 vs 01,34) using powerGNN  
	8: five node case b (01 vs 34) using powerGNN  
	9: five node case c (0102 vs 0103) using powerGNN  
	origin_10: WGEVIA on SIMU   
	origin_12: WGEVIA on REAL  
	13: G2V on SIMU   
	15: G2V on REAL  
	16: powerGNN on SIMU  
	18: powerGNN on REAL  
	21: Multi-channel G2V on REAL 
	22: MUlti-channel G2V (index label) on REAL 
	23: Multi-channel G2V on SIMU  
    24: MUlti-channel G2V (index label) on SIMU  
example:
```
python3 main.py --opcode 1

python3 main.py --opcode origin_10 --nT 10 --d 8 --w 4
python3 main.py --opcode origin_12 --nT 10 --d 8 --w 4

python3 main.py --opcode 13
python3 main.py --opcode 15

python3 main.py --opcode 16
python3 main.py --opcode 18

python3 main.py --opcode 21 --nT 10 --d 8
python3 main.py --opcode 22 --nT 10 --d 8
python3 main.py --opcode 23 --nT 10 --d 8
python3 main.py --opcode 24 --nT 10 --d 8
```
