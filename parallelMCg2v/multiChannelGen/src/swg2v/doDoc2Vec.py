from gensim.models.doc2vec import Doc2Vec

class doDoc2Vec(object):
    def __init__(self,graphCollection,numOfGraph,Dim,downSamplingRate,learnRate):
        self.graphCollection = graphCollection
        self.Dim = Dim
        self.learnRate = learnRate
        self.downSamplingRate = downSamplingRate
        self.model = None
        self.graphsRepresent = []
        self.numOfGraph = numOfGraph

    def run(self):
        self.model = Doc2Vec(self.graphCollection,
            vector_size=self.Dim,
            window=0,
            min_count=1,
            dm=0,
            sample=self.downSamplingRate,
            workers=1,
            epochs=100,
            alpha=self.learnRate)

    def saveRepresent(self):
        for i in range(self.numOfGraph):
            self.graphsRepresent.append(list(self.model.docvecs["graph_"+str(i)]))

    def getRepresent(self):
        return self.graphsRepresent
