import json
import networkx as nx

class loadGraph(object):
    """
    class : loadGraph
    load graph data from saved formated json files
    function:
    load : load graph data from input path
    """
    def __init__(self):
        pass

    def load(self,path):
        data = json.load(open(path))
        graph = nx.from_edgelist(data["edges"])
        H = nx.path_graph(len(data["features"]))
        graph.add_nodes_from(H)
        features = data["features"]
        return graph, features

