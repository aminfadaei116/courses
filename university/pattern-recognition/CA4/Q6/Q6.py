import numpy as np
from MNIST_Loader import load_mnist
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
from math import floor
from numpy import linalg as LA
from sklearn.metrics import accuracy_score

data_train, label_train = load_mnist('Fashion-MNIST', kind='train')
data_test, label_test = load_mnist('Fashion-MNIST', kind='t10k')

mean_train = []


classes = {0:[], 1:[], 2:[], 3:[], 4:[], 5:[], 6:[], 7:[], 8:[], 9:[]}
scatterI = {0:[], 1:[], 2:[], 3:[], 4:[], 5:[], 6:[], 7:[], 8:[], 9:[]}
for i in range (len(label_train)):
    classes[label_train[i]].append(data_train[i])
    
for i in range(10):
    mean_train.append(np.mean(classes[i], axis = 0))
    
    
for i in range(10):
    scatter = np.zeros([data_train.shape[1], data_train.shape[1]])
    for j in range(len(classes[i])):
        tmp = np.array([np.subtract(classes[i][j], mean_train[i])])
        tmp2 = tmp.T
        scatter += np.multiply(tmp, tmp2)
    scatterI[i] = (scatter)

scatterW = np.zeros([data_train.shape[1], data_train.shape[1]])
for i in range(10):
    scatterW = np.add(scatterW, scatterI[i])

meanAll = np.mean(data_train, axis = 0)

scatterB = np.zeros([data_train.shape[1], data_train.shape[1]])

for i in range(10):
    tmp = np.array([np.subtract(mean_train[i], meanAll)])
    tmp2 = tmp.T
    scatterB += np.multiply(tmp, tmp2)
    
invscatterW = np.linalg.inv(scatterW)

ScatterP = np.matmul(invscatterW, scatterB)

accuracyList = []
trace= []
for m in range(782,30,-30):
    argenValue, argenVector = LA.eigh(ScatterP)

    argenValue, argenVector = list(zip(*( sorted(zip(argenValue, argenVector)) )))
    argenValue = argenValue[::-1]
    argenVector = argenVector[::-1]
    for i in range(m):
        argenVector = np.delete(argenVector, (783-i), axis = 0)
        argenValue = np.delete(argenValue, (783-i), axis = 0)

    argenValue, argenVector = list(argenValue), np.array(list(argenVector))
    trace.append(sum(argenValue))

    newTrainData = (argenVector.dot((data_train - meanAll).T)).T
    newTestData = (argenVector.dot((data_test - np.mean(data_test, axis = 0)).T)).T

#############################################################################

    clf = GaussianNB()
# priors=None, var_smoothing=1e-09

    from time import process_time

    start = process_time()
    clf.fit(newTrainData, label_train)
    #print('LDA :')
    #print('time of train :', process_time()-start)

    start = process_time()
    predicts = clf.predict(newTestData)
    #print('time of test :', process_time()-start)
    accuracyList.append(accuracy_score(label_test,predicts))
    print("Accuracy : ", accuracy_score(label_test, predicts))

import matplotlib.pyplot as plt

x =np.linspace(start = 1, stop = 751, num = 26, dtype = int)
plt.plot(x,accuracyList)
plt.title("CCR")
plt.show()


plt.plot(x,trace)
plt.title("Separability measure")
plt.show()


clf2 = GaussianNB()

start = process_time()
clf2.fit(data_train, label_train)
print("Origin :")
print('time of train :', process_time()-start)

start = process_time()
predicts = clf2.predict(data_test)
print('time of test :', process_time()-start)

print("Accuracy : ", accuracy_score(label_test, predicts))


argenValue, argenVector = LA.eigh(ScatterP)
argenValue = argenValue[::-1]
sorted(argenValue).reverse()
plt.plot(((argenValue)))
plt.show()
