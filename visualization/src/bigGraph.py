import numpy as np

class bigGraph(object):
    """
    class : bigGraph
    gather graphs' edges into one weighted graph
    calculate possibility of edge occurrence and represent them as unweighted graph

    input parameters:
    numOfNodes : numbers of vertex in graph
    Y : graphs' labels
    """
    def __init__(self,numOfNodes,Y):
        self.nOn = numOfNodes
        self.aggrGl0 = np.zeros((numOfNodes,numOfNodes))
        self.aggrGl1 = np.zeros((numOfNodes,numOfNodes))
        self.Gl0Count = 0
        self.Gl1Count = 0
        self.aggrG = None
        self.Y = Y

    def aggregate(self,graph,idx):
        """
        function aggregate sum all edge occurrence to one single weighted graph
        """
        if (int)(self.Y[idx][0]) == 1:
            self.Gl1Count = self.Gl1Count + 1
            edges = graph.edges
            for v1,v2 in edges:
                self.aggrGl1[v1][v2] = self.aggrGl1[v1][v2] + 1
                self.aggrGl1[v2][v1] = self.aggrGl1[v2][v1] + 1

        else:
            self.Gl0Count = self.Gl0Count + 1
            edges = graph.edges
            for v1,v2 in edges:
                self.aggrGl0[v1][v2] = self.aggrGl0[v1][v2] + 1
                self.aggrGl0[v2][v1] = self.aggrGl0[v2][v1] + 1

    def avg(self):
        """
        function avg calculate probability and
        convert weighted graph of edge sum to unweighted graph of edge occurrence
        return :
        aggrGl0 : labeled 0 aggregated graph
        aggrGl1 : labeled 1 aggregated graph
        """
        self.aggrGl1 = self.aggrGl1/self.Gl1Count
        self.aggrGl0 = self.aggrGl0 / self.Gl0Count
        mean = np.sum(self.aggrGl1) + np.sum(self.aggrGl0)
        mean = mean/(2*self.nOn*self.nOn)
        max = np.max(self.aggrGl1)
        if max < np.max(self.aggrGl0):
            max = np.max(self.aggrGl0)

        #for REAL2
        self.aggrGl1 = (self.aggrGl1 > (mean+(max - mean)/4)).astype(int)
        self.aggrGl0 = (self.aggrGl0 > (mean+(max - mean)/4)).astype(int)
        #for REAL1
        #self.aggrGl1 = (self.aggrGl1 > mean).astype(int)
        #self.aggrGl0 = (self.aggrGl0 > mean).astype(int)


        return self.aggrGl0, self.aggrGl1