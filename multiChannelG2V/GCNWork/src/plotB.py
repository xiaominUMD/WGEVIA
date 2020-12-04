import matplotlib.pyplot as plt
import numpy as np
import csv

result_path = "/Users/xiaomin/Desktop/GCNWork/plotResults/"
file_name = "B5-10.png"
acc_test_his = [0.937231298366294, 0.942390369733448,0.938091143594153,0.938091143594153, 0.930352536543422, 0.936371453138435, 0.9518486672398968, 0.944110060189166, 0.938091143594153, 0.9492691315563199]
xAxis = np.arange(len(acc_test_his))
labels = [1,2,3,4,5,6,7,8,9,10]
plt.figure(figsize=(12, 6))
plt.plot(xAxis, acc_test_his, 'r--x')
plt.xticks(xAxis, labels)

plt.title('Bayesian opt Attempts (5 tries) vs Accuracy History\n Average Acc = 0.9405846947549442')
plt.xlabel('Max attempts')
plt.ylabel('Accuracy (X100 %)')
plt.ylim(bottom=0.5, top=1)
#plt.yticks(np.arange(0.5, 1.05, 0.05))

plt.tight_layout()
# plt.show();

plt.savefig(result_path + file_name)