import matplotlib.pyplot as plt
import numpy as np
import csv

result_path = "/Users/xiaomin/Desktop/GCNWork/plotResults/"
file_name = "R5-10.png"
acc_test_his = [0.8950988822012038, 0.938091143594153, 0.938950988822012, 0.944969905417025, 0.9363714531384351, 0.935511607910576, 0.943250214961307, 0.7970765262252795, 0.9054170249355116, 0.9484092863284609]
xAxis = np.arange(len(acc_test_his))
labels = [1,2,3,4,5,6,7,8,9,10]
plt.figure(figsize=(12, 6))
plt.plot(xAxis, acc_test_his, 'r--x')
plt.xticks(xAxis, labels)

plt.title('Random Attempts (5 tries) vs Accuracy History\n Average Acc = 0.9183147033533963')
plt.xlabel('Max attempts')
plt.ylabel('Accuracy (X100 %)')
plt.ylim(bottom=0.5, top=1)
#plt.yticks(np.arange(0.5, 1.05, 0.05))

plt.tight_layout()
# plt.show();

plt.savefig(result_path + file_name)