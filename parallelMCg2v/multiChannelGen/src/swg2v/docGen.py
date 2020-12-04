from gensim.models.doc2vec import TaggedDocument

class docGen(object):
	def __init__(self):
		self.docCollection = []

	def addDoc(self,graphFeatures,idx):
		self.docCollection.append(TaggedDocument(words = graphFeatures , tags = ["graph_" + str(idx)]))

	def getDoc(self):
		return self.docCollection
