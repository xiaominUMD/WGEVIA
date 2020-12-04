import csv 

class represent(object):
    """
    class : represent
    output representation to file
    input parameters:
    graphsRepresen : collection of generated features for graphs
    numOfGraph : number of input graphs
    file : target file to save

    function:
    output : save data to file
    """
    def __init__(self,graphsRepresent,numOfGraph,file):
        self.graphsRepresent = graphsRepresent
        self.numOfGraph = numOfGraph
        self.file = file

    def output(self):
        with open(self.file, 'w+', newline='') as csvfile:
            spamwriter = csv.writer(csvfile)
            spamwriter.writerow(['sparse weighted graph embedding,'])
            for i in range(self.numOfGraph):
                spamwriter.writerow([i]+self.graphsRepresent[i]) #output file has no index, all indexs are in order
        csvfile.close()
