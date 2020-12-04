import csv
import numpy as np

class DataLoader(object):
    '''
    class DataLoader
    author: Xiaomin Wu
    Functions:
    __init__(self,path): the constructor, path will be the csv file path start from the directory of this program file
    loadData(self): load data from csv file. return X,Y. X contain input data in shape (N,D). Y contain output label standard in shape (N,1). 
        here N means number of sample, D means dimentions. 
    '''
    
    def __initial__(self):
        pass
        
    def loadData(self,path):
        data = []
       
        with open(path, 'r') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
            #i = 0
            for row in spamreader:
                #if(i!=0):
                data.append(list(map(float,row[0].split(','))))
                #i =i+1
            data = np.array(data)
                         
            #return data<.csv>[rows][columns]
            
            
        return data

    
    #data loader for TRACES_1004_1_1 and BEHAVIOR_1004_1_1 CSV
    def loadXY(self,X_path,Y_path):
        X = self.loadData(X_path)
        Y = self.loadData(Y_path)
        X = X.T
        Y = Y[:,2] #use only first behaviral variable
        
        return X,Y
    
    def extractOne(self,X,Y,label):
        N = X.shape[0]
        D = X.shape[1]
        ExtractResult = []
        Y = Y.reshape(N,1)
        xy = np.concatenate((X,Y), 1)
        
        for row in range(N):
            last = xy[row][D]
            if (last == label):
                ExtractResult.append(np.array(xy[row]))
        
        ExtractResult = np.array(ExtractResult)
        return ExtractResult, len(ExtractResult)
        
    def extractFiles(self,PathAry,label):
        i = 0
        extract = []
        while(i != len(PathAry)):
            trace = PathAry[i]
            behavior = PathAry[i+1]
            i = i +2
            
            X,Y = self.loadXY(trace, behavior)
            exre,length = self.extractOne(X, Y,label)
            extract.append(exre)
            print("Extract ",length,"data with label:",label,"from file:",trace,"\n")
        
        result = None
        if(len(extract) - 1 == 0):
            result = extract[0]
        else:
            for j in range(len(extract) - 1):
                extract[j+1] = np.concatenate((extract[j],extract[j+1]),0)
                result = extract[j+1]
            
        return result, len(result)
    
    def extractFileSeries(self,str1,s,e,label):
        pathAry =[]
        for i in range(s,e):
            pathAry.append(''.join(['TRACES_',str1,'_',str(i+1),'.csv']))
            pathAry.append(''.join(['BEHAVIOR_',str1,'_',str(i+1),'.csv']))

        a,b = self.extractFiles(pathAry,label)
        return a,b
    
    def extractBalanceData(self,str1,s,e,focus):
        a,mask = self.extractFileSeries(str1, s,e, focus)
        c = None
        if(focus == 1):
            c,_ = self.extractFileSeries(str1, s,e, 0)
        else:
            c,_ = self.extractFileSeries(str1, s,e, 1)
        np.random.shuffle(c)
        b = c[0:mask]
        re = np.concatenate((a,b),0)
        
        return re, len(re)
    
    def extractBalanceDataShuffled(self,str1,s,e,focus):
        data,length = self.extractBalanceData(str1, s,e, focus)
        for i in range(10):
            np.random.shuffle(data)
       
        return data,length
    
    def combineTwo(self,X,Y):
        re = np.concatenate((X,Y),0)
        
        return re
    
    def splitXY(self, XY):
        X = XY[:,np.arange(XY.shape[1] - 1)]
        Y = XY[:,XY.shape[1]-1]
        
        return X,Y
        

