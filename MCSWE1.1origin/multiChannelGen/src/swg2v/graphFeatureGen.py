import hashlib


class graphFeatureGen(object):
    """
    class : graphFeatureGen
    genrerate features for input unweighted sparse graph using SG2V algorithm
    input parameters:
    graph : the target graph
    features : the original features of the graph
    iter : iterations for feature extraction
    """
    def __init__(self,graph,features,iter):
        self.allFeatures = features
        self.iter = iter
        self.features = features #sequenced features, natural ordering
        self.graph = graph

    def wlIterations(self):
        """
        modified feature extractor based on WL graph kernel
        :return:
        allFeatures : generated features as an array
        """
        for i in range(self.iter):
            self.perWlIteration()
        return self.allFeatures

    def perWlIteration(self):
        """
        generate features for graph based on connections and zero degree nodes
        :return:
        """
        featuresCurrIter = []
        for i in range(len(self.graph.nodes())):
            neighbors = self.graph.neighbors(i)
            feature = []

            #generate features for connections
            for each in neighbors:
                feature.append(self.features[each])
            list = []
            if len(feature) == 0:

                # generate features for zero degree nodes
                if i != 0 and i != len(self.graph.nodes()) - 1:
                    for n in range(i - 1, i + 2):
                        if n != i:
                            list = list+[self.features[n]]
                elif i == 0:
                    list = list+[self.features[len(self.graph.nodes()) - 1]]
                    for n in range(i, i + 2):
                        if n != i:
                            list = list + [self.features[n]]
                elif i == len(self.graph.nodes()) - 1:
                    for n in range(i - 1, i):
                        if n != i:
                            list = list+ [self.features[n]]
                    list = list+ [self.features[0]]

            else:
                list = [self.features[i]]+sorted(feature)

            #gather features as a new feature string
            features = "_".join(list)

            #hash is used to keep uniqueness of feature and save memory space
            hash_object = hashlib.md5(features.encode())
            uniqueRepresent = hash_object.hexdigest()
            featuresCurrIter.append(uniqueRepresent)
        try:
            self.allFeatures = self.allFeatures + featuresCurrIter
        except:
            print(self.allFeatures)
            print(featuresCurrIter)
        
        self.features = featuresCurrIter
