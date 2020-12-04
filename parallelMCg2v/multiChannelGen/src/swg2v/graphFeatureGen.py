import hashlib

class graphFeatureGen(object):
    def __init__(self,graph,features,iter):
        self.allFeatures = features
        self.iter = iter
        self.features = features #sequenced features, natural ordering
        self.graph = graph
        self.featurescpy = []
        for each in features:
            self.featurescpy.append(each)

    def wlIterations(self):
        for i in range(self.iter):
            self.perWlIteration()
        return self.allFeatures

    def perWlIteration(self):
        featuresCurrIter = []
        for i in range(len(self.graph.nodes())):
            neighbors = self.graph.neighbors(i)
            feature = []
            for each in neighbors:
                feature.append(self.features[each])
            list = []
            if len(feature) != 0:
                list = [self.features[i]]+sorted(feature)
                features = "_".join(list)
                hash_object = hashlib.md5(features.encode())
                uniqueRepresent = hash_object.hexdigest()
                featuresCurrIter.append(uniqueRepresent)
                self.featurescpy[i] = uniqueRepresent
        try:
            self.allFeatures = self.allFeatures + featuresCurrIter
        except:
            print(self.allFeatures)
            print(featuresCurrIter)

        for i in range(len(self.features)):
            self.features[i] = self.featurescpy[i]