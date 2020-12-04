import json
import csv
import numpy as np

class SampleGen:

    def __init__(self, size):
        self.size = size
    def graphGen(self):

        for i in range(self.size):
            f = open("../dataset/genSample/" + str(i) + ".json", "w+")

            if(i<self.size/2):
                nodes = np.random.choice(101, 5, replace=False)

                f.write("{\"edges\": [")
                f.write("["+str(nodes[0])+", "+str(nodes[1])+"]], ")

                f.write("\"features\": {")

                f.write("\"" + str(nodes[0]) + "\": \"" + str(1) + "\", ")
                f.write("\"" + str(nodes[1]) + "\": \"" + str(1) + "\", ")
                f.write("\"" + str(nodes[2]) + "\": \"" + str(0) + "\", ")
                f.write("\"" + str(nodes[3]) + "\": \"" + str(0) + "\", ")

                f.write("\"" + str(nodes[4]) + "\": \"" + str(0) + "\"}}")
            else:
                nodes = np.random.choice(101, 5, replace=False)

                f.write("{\"edges\": [")
                f.write("[" + str(nodes[0]) + ", " + str(nodes[1]) + "], ")
                f.write("[" + str(nodes[1]) + ", " + str(nodes[2]) + "], ")
                f.write("[" + str(nodes[2]) + ", " + str(nodes[3]) + "], ")
                f.write("[" + str(nodes[3]) + ", " + str(nodes[4]) + "]], ")

                f.write("\"features\": {")

                f.write("\"" + str(nodes[0]) + "\": \"" + str(1) + "\", ")
                f.write("\"" + str(nodes[1]) + "\": \"" + str(2) + "\", ")
                f.write("\"" + str(nodes[2]) + "\": \"" + str(2) + "\", ")
                f.write("\"" + str(nodes[3]) + "\": \"" + str(2) + "\", ")

                f.write("\"" + str(nodes[4]) + "\": \"" + str(1) + "\"}}")

            f.close()


    def labelgen(self):

        with open("../dataset/genSample/labelAll.csv", 'w', newline='') as csvfile:
            spamwriter = csv.writer(csvfile)
            for i in range(self.size):
                if(i<self.size/2):
                    spamwriter.writerow(str(1))
                else:
                    spamwriter.writerow(str(2))


sg = SampleGen(1200)
sg.graphGen()
sg.labelgen()
print('done')