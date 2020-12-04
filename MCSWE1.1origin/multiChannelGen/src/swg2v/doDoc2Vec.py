from gensim.models.doc2vec import Doc2Vec
from gensim.test.utils import get_tmpfile


class doDoc2Vec(object):
    """
    class for doDoc2Vec that wraps Doc2Vec algorithm
    gather hyper-parameters for Doc2Vec and
    output saved generated features
    """
    def __init__(self,index,graphCollection,numOfGraph,Dim,downSamplingRate,learnRate):
        self.graphCollection = graphCollection
        self.Dim = Dim
        self.learnRate = learnRate
        self.downSamplingRate = downSamplingRate
        self.model = None
        self.graphsRepresent = []
        self.numOfGraph = numOfGraph
        self.index = index
        self.inferenceVector = None

    def run(self):
        """
        run Doc2Vec with input hyper-parameters
        save trained doc2vec model
        """
        self.model = Doc2Vec(self.graphCollection,
            vector_size=self.Dim,
            window=0,
            min_count=1,
            dm=0,
            sample=self.downSamplingRate,
            workers=1,
            epochs=100,
            alpha=self.learnRate)

        self.model.save('../trainedModel/d2vChannel'+str(self.index))
        self.saveRepresent()

    def runWithTrainedModel(self):
        """
        load trained doc2vec model
        run Doc2Vec inference with pre-trained model
        """

        model = Doc2Vec.load('../trainedModel/d2vChannel'+str(self.index))
        self.inferenceVector = []
        for i in range(self.numOfGraph):
            self.graphsRepresent.append(model.infer_vector(self.graphCollection[i].words))

    def saveRepresent(self):
        """
        save generated feature for graph i
        from Doc2Vec
        """
        for i in range(self.numOfGraph):
            self.graphsRepresent.append(list(self.model.docvecs["graph_"+str(i)]))

    def getRepresent(self):
        return self.graphsRepresent
