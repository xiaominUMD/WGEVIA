import json
import networkx as nx

class loadGraph(object):

    def __init__(self):
        pass;

    def load(self,path):
        data = json.load(open(path))
        graph = nx.from_edgelist(data["edges"])
        H = nx.path_graph(len(data["features"]))
        graph.add_nodes_from(H)
        features = data["features"]  #key as str          
        return graph, features

