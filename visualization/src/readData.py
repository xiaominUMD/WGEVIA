import csv
import sys
import numpy as np


class ReadMCData:
    """
    class for reading microcircuit data from csv files
    aims to read csv files contain MC matrix and corresponding labels
    and output: 
            X --- Vector of 2D array
            Y --- corresponding labels
    """

    def __init__(self, name, mcAmount, path):
        self.X = []
        self.Y = []
        self.name = name
        self.size = mcAmount
        self.path = path
        self.Xin = []   #data X used for classfication model
        self.Yl = [] #data y used for classfication models
        self.xtest = []

    def readY(self):
        """
        function to read Y from bunch of formated label#.csv file
        """
        for i in range(self.size):

            filename = 'label' + str(i) + '.csv'
            try:
                with open(self.path + filename) as csvfile:
                    spamreader = csv.reader(csvfile, delimiter=',')
                    next(spamreader)
                    for row in spamreader:
                        self.Y.append(row[1])

            except:
                #print("Unexpected error:", sys.exc_info())
                #print('invalid file: ' + filename +'\n')
                continue

    def writeY(self):
        """
        function to write a labelAll.csv file contain all labels
        """
        filename = 'labelAll.csv'
        with open(self.path + filename, 'w', newline='') as csvfile:
            spamwriter = csv.writer(csvfile)
            for i in range(len(self.Y)):
                spamwriter.writerow(self.Y[i])

    def readX(self):
        """
        read X from input graph files
        data#.csv file for each graph
        one data#.csv file contains an adj matrix for that graph
        """
        for i in range(self.size):
            innerX = []
            filename = 'data' + str(i) + '.csv'
            try:
                with open(self.path + filename) as csvfile:
                    spamreader = csv.reader(csvfile, delimiter=',')
                    next(spamreader)
                    for row in spamreader:
                        innerX.append(row[1:len(row)])

            except:
                #print("Unexpected error:", sys.exc_info())
                #print('invalid file: ' + filename +'\n')
                continue

            self.X.append(innerX)

    #used for visualize input
    def readXsingle(self,idx):
        """
        read X from input graph files
        data#.csv file for each graph
        one data#.csv file contains an adj matrix for that graph
        """

        innerX = []
        filename = 'data' + str(idx) + '.csv'

        with open(self.path + filename) as csvfile:
            spamreader = csv.reader(csvfile, delimiter=',')
            next(spamreader)
            for row in spamreader:
                innerX.append(row[1:len(row)])



        self.X.append(innerX)

    def readXtest(self):
        """
        read X for test set
        """
        for i in range(self.size):
            innerX = []
            filename = 'ftest' + str(i) + '.csv'
            #print('\n'+self.path+filename)
            try:
                with open(self.path + filename) as csvfile:
                    spamreader = csv.reader(csvfile, delimiter=',')
                    next(spamreader)
                    for row in spamreader:
                        innerX.append(row[1])

            except:
                #print("Unexpected error:", sys.exc_info())
                #print('invalid file: ' + filename +'\n')
                continue

            self.xtest.append(innerX)

    def writeX(self):
        """
        function to write a dataAll.csv file contain all data
        """
        filename = 'dataAll.csv'
        with open(self.path + filename, 'w', newline='') as csvfile:
            spamwriter = csv.writer(csvfile)
            for i in range(len(self.X)):
                spamwriter.writerow(self.X[i])

    def writeXcsv(self):
        """
        for test set, write featuretest.csv file contain data and labels
        """
        self.xtest = np.array(self.xtest)
        self.xtest = self.xtest.astype(np.float)

        filename = 'featuretest.csv'
        with open(self.path + filename, 'w') as csvfile:
            spamwriter = csv.writer(csvfile, delimiter=',')
            for i in range(len(self.xtest)):
                ary = []
                j = 2
                while(j<13):
                    ary.append(self.xtest[i][j])
                    j = j +1
                ary.append(self.Y[i])
                spamwriter.writerow(ary)


class ReadFLData:
    """
    class contain function for loading data to machine learning model
    functions:
    loadData : load data in sepecific path
    loadXT : wrapper over loadData
    splitXY : split X and Y 
    """
    def loadData(self, path,tag):
        data = []
        with open(path, 'r') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
            if(tag == 'x'):
                next(spamreader)
            for row in spamreader:
                if (tag == 'x'):
                    data.append(row[0].split(',')[1:len(row[0])])
                else:
                    data.append(row[0])
            data = np.array(data);

        data = np.array(data)

        if (tag == 'x'):
            data = data.astype(np.float)
        else:
            data = data.astype(np.int)
        return data


    def loadXY(self, X_path, Y_path):
        X = self.loadData(X_path,'x');
        Y = self.loadData(Y_path,'y');
        return X, Y;

    def splitXY(self, XY):
        X = XY[:,np.arange(XY.shape[1] - 1)];
        Y = XY[:,XY.shape[1]-1];
        
        return X,Y;
