import matplotlib.pyplot as plt
import numpy as np
import csv

result_path = "/Users/xiaomin/Desktop/GCNWork/plotResults/"
file_name = "BayesianAtpPlot.png"
acc_test_his = [0.939810834049871, 0.939810834049871, 0.939810834049871, 0.9475494411006019,0.9509888220120378,0.9509888220120378,0.9509888220120378,0.9509888220120378,0.9509888220120378,0.9518486672398968]
xAxis = np.arange(len(acc_test_his))
labels = [5,10,15,20,25,30,35,40,45,50]
plt.figure(figsize=(12, 6))
plt.plot(xAxis, acc_test_his, 'r--x', label='test_acc')
plt.xticks(xAxis, labels)

plt.title('Bayesian opt Attempts vs Accuracy History')
plt.xlabel('Max attempts')
plt.ylabel('Accuracy (X100 %)')
plt.ylim(bottom=0.5, top=1)
#plt.yticks(np.arange(0.5, 1.05, 0.05))

plt.tight_layout()
plt.legend()
# plt.show();

plt.savefig(result_path + file_name + 'Greedy' + '.png')