import csv
lof = "../exp/runtimeRecord/lastLoss.csv"
record = "../exp/result/mcsweACC.csv"
RE = {}
newary = []
indx = 0
with open(lof) as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',')
    for row in spamreader:
        RE[str(indx)] = row[0]
        indx = indx + 1
csvfile.close()
lastLoss = RE['0']
acc = RE['1']
recordstr = "acc: "+str(acc)
newary.append(recordstr)
with open(record, 'a', newline='') as csvfile:
    spamwriter = csv.writer(csvfile)
    for i in range(len(newary)):
        spamwriter.writerow([newary[i]])
csvfile.close()
