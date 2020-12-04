# libraries
import matplotlib.pyplot as plt
import numpy as np
import csv

class DensityMapPlot:

    def __init__(self):
        self.model_0 = {}
        self.model_1 = {}
        self.model_2 = {}
        self.model_3 = {}
        self.matrix_0 = None
        self.matrix_1 = None
        self.matrix_2 = None
        self.matrix_3 = None

        #Tary = np.linspace(0.1, 0.25, num=31)


        Tary = [0.028, 0.056, 0.084, 0.112, 0.14, 0.168, 0.196, 0.224, 0.252]
        #self.T = Tary.tolist()
        self.T = Tary
        self.Dim = [2, 16, 32, 64, 96, 128]
        self.Dim_model_3 = [16, 32, 64, 96, 128]
        self.epoch = None


    def readResultFile(self,file):

        #open file:
        with open(file) as csvfile:
            spamreader = csv.reader(csvfile, delimiter=' ')
            for row in spamreader:
                if row[5] == '2' and row[4] == '0.23':
                    print('here')

                self.epoch = row[6]
                if row[1] == '0':
                    self.model_0[row[4]+' '+row[5]] = float(row[3])
                if row[1] == '1':
                    self.model_1[row[4] + ' '+row[5]] = float(row[3])
                if row[1] == '2':
                    self.model_2[row[4] + ' '+row[5]] = float(row[3])
                if row[1] == '3':
                    self.model_3[row[4] + ' '+row[5]] = float(row[3])

        csvfile.close()

    def matrixGen(self):
        matrix_0 = np.random.randint(0,1,(len(self.T),len(self.Dim)))
        matrix_0 = matrix_0.astype(float)
        for i in range(len(self.T)):

            for j in range(len(self.Dim)):
                sindx = str(self.T[i])+' '+str(self.Dim[j])
                value = self.model_0[sindx]

                matrix_0[i][j] = value

        matrix_1 = np.random.randint(0,1,(len(self.T), len(self.Dim_model_3)))
        matrix_1 = matrix_1.astype(float)
        for i in range(len(self.T)):
            for j in range(len(self.Dim_model_3)):
                sindx = str(self.T[i])+' '+str(self.Dim_model_3[j])
                value = self.model_1[sindx]
                matrix_1[i][j] = value
        ''' 
        matrix_2 = np.random.randint(0,1,(len(self.T),len(self.Dim)))
        matrix_2 = matrix_2.astype(float)
        for i in range(len(self.T)):
            for j in range(len(self.Dim)):
                sindx = str(self.T[i])+' '+str(self.Dim[j])
                value = self.model_2[sindx]
                matrix_2[i][j] = value

        matrix_3 = np.random.randint(0,1,(len(self.T),len(self.Dim_model_3)))
        matrix_3 = matrix_3.astype(float)
        for i in range(len(self.T)):
            for j in range(len(self.Dim_model_3)):
                sindx = str(self.T[i])+' '+str(self.Dim_model_3[j])
                value = self.model_3[sindx]
                matrix_3[i][j] = value
        '''
        self.matrix_0 = matrix_0
        self.matrix_1 = matrix_1
        #self.matrix_2 = matrix_2
        #self.matrix_3 = matrix_3




    def plotDenseMap(self,savepath,modelIndx):
        if modelIndx == '0':
            matrix = self.matrix_0
            T = self.T
            Dim = self.Dim
        if modelIndx == '1':
            matrix = self.matrix_1
            T = self.T
            Dim = self.Dim_model_3
        if modelIndx == '2':
            matrix = self.matrix_2
            T = self.T
            Dim = self.Dim
        if modelIndx == '3':
            matrix = self.matrix_3
            T = self.T
            Dim = self.Dim_model_3

        import matplotlib.pyplot as plt
        fig, ax = plt.subplots(figsize=(8,16))
        im = ax.imshow(matrix,cmap='plasma')
        plt.colorbar(im, ax=ax)
        plt.xticks(np.arange(len(Dim)), Dim)
        Tt = np.around(T,decimals=3)
        plt.yticks(np.arange(len(T)), Tt)
        plt.title('graph2vec epoch '+self.epoch+' model_'+modelIndx+' \nACC relates to feature Dim and Edge Threshold T\nMax Acc: '+str(np.around(np.max(matrix),decimals=4)))
        plt.xlabel('graph2vec generated feature Dim')
        plt.ylabel('Threshold T for picking edges')
        plt.ylim(bottom=-0.5, top=len(T)-0.5)
        #plt.annotate('Max Acc' + str(np.around(np.max(self.matrix_0),decimals=4)),xy = (1,5))
        for y_index in np.arange(len(T)):
            for x_index in np.arange(len(Dim)):
                label = matrix[y_index][x_index]
                label = np.around(label,decimals=3)
                ax.text(x_index, y_index, label, color='black', ha='center', va='center')
        #plt.show()
        filename = 'graph2vec epoch '+self.epoch+' model_'+modelIndx
        plt.savefig(savepath+filename + '.png')



#execute
dmp = DensityMapPlot();
dmp.readResultFile("/Users/xiaomin/Desktop/GCNWork/exp/resultcsv/resultEpoch100.csv")
dmp.matrixGen()
dmp.plotDenseMap('/Users/xiaomin/Desktop/GCNWork/plotResults/','0')
dmp.plotDenseMap('/Users/xiaomin/Desktop/GCNWork/plotResults/','1')
'''
dmp.plotDenseMap('/Users/xiaomin/Desktop/GCNWork/plotResults/','2')
dmp.plotDenseMap('/Users/xiaomin/Desktop/GCNWork/plotResults/','3')
'''
'''
dmp = DensityMapPlot();
dmp.readResultFile("/Users/xiaomin/Desktop/GCNWork/exp/copy_resultcsv/resultEpoch150.csv")
dmp.matrixGen()
dmp.plotDenseMap('/Users/xiaomin/Desktop/GCNWork/plotResults/','0')
dmp.plotDenseMap('/Users/xiaomin/Desktop/GCNWork/plotResults/','1')
dmp.plotDenseMap('/Users/xiaomin/Desktop/GCNWork/plotResults/','2')
dmp.plotDenseMap('/Users/xiaomin/Desktop/GCNWork/plotResults/','3')

dmp = DensityMapPlot();
dmp.readResultFile("/Users/xiaomin/Desktop/GCNWork/exp/copy_resultcsv/resultEpoch200.csv")
dmp.matrixGen()
dmp.plotDenseMap('/Users/xiaomin/Desktop/GCNWork/plotResults/','0')
dmp.plotDenseMap('/Users/xiaomin/Desktop/GCNWork/plotResults/','1')
dmp.plotDenseMap('/Users/xiaomin/Desktop/GCNWork/plotResults/','2')
dmp.plotDenseMap('/Users/xiaomin/Desktop/GCNWork/plotResults/','3')

dmp = DensityMapPlot();
dmp.readResultFile("/Users/xiaomin/Desktop/GCNWork/exp/copy_resultcsv/resultEpoch250.csv")
dmp.matrixGen()
dmp.plotDenseMap('/Users/xiaomin/Desktop/GCNWork/plotResults/','0')
dmp.plotDenseMap('/Users/xiaomin/Desktop/GCNWork/plotResults/','1')
dmp.plotDenseMap('/Users/xiaomin/Desktop/GCNWork/plotResults/','2')
dmp.plotDenseMap('/Users/xiaomin/Desktop/GCNWork/plotResults/','3')

dmp = DensityMapPlot();
dmp.readResultFile("/Users/xiaomin/Desktop/GCNWork/exp/copy_resultcsv/resultEpoch300.csv")
dmp.matrixGen()
dmp.plotDenseMap('/Users/xiaomin/Desktop/GCNWork/plotResults/','0')
dmp.plotDenseMap('/Users/xiaomin/Desktop/GCNWork/plotResults/','1')
dmp.plotDenseMap('/Users/xiaomin/Desktop/GCNWork/plotResults/','2')
dmp.plotDenseMap('/Users/xiaomin/Desktop/GCNWork/plotResults/','3')

'''
