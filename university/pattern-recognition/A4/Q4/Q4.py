import numpy as np
from MNIST_Loader import load_mnist
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
from math import floor


data_train, label_train = load_mnist('Fashion-MNIST', kind='train')
data_test, label_test = load_mnist('Fashion-MNIST', kind='t10k')
featureNumber = len(data_test[0])

def setDims(arr) :
    dim1, dim2 = arr.shape
    return arr.T.reshape(dim2, dim1, 1)

swapedDimsTrain = setDims(data_train)
swapedDimsTest = setDims(data_test)


def makePrev(arr, indexes) :
    prev = np.array([[]]*arr.shape[1])
    for index in indexes :
        prev = np.concatenate((prev, arr[index]), axis=1)
    return prev
    
def addPrev(arr, indexes=[]) :
    prev = makePrev(arr, indexes)
    if len(prev)>0 : return np.concatenate((arr, np.tile(prev, (featureNumber,1,1))), axis=2)
    else : return arr

lambdaLearn = lambda t: GaussianNB(priors=None, var_smoothing=1e-03).fit(t, label_train)

lambdaTest = lambda g,t: accuracy_score(label_test, g.predict(t))

def maxIndex(arr) :
    return np.where(arr == np.amax(arr))[0][0]

getFloor = lambda t : floor(t)

featureIndex = np.array([])
accuracyList = []
for i in range(60) :
    learnedAgents = np.array(list(map(lambdaLearn, addPrev(swapedDimsTrain, featureIndex))))
    accuracy = np.array(list(map(lambdaTest, learnedAgents, addPrev(swapedDimsTest, featureIndex))))
    if i > 0 : accuracy[featureIndex] = -np.Infinity
    featureIndex = np.append(featureIndex, [maxIndex(accuracy)])
    featureIndex = np.array(list(map(getFloor, featureIndex)))
    accuracyList.append(accuracy[featureIndex[-1]])
    print(featureIndex[-1], ':', accuracyList[-1])
    
import matplotlib.pyplot as plt
plt.plot(accuracyList)
plt.title("CCR")
plt.grid()
plt.xlabel("number of features")
plt.ylabel("accuracy")
plt.show()