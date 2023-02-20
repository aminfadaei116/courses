import numpy as np
from MNIST_Loader import load_mnist
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
from math import floor
from numpy import linalg as LA
from sklearn.metrics import accuracy_score

def var(data_set, mean):
    res = np.zeros([data_set.shape[1],data_set.shape[1]])
    for i in range(data_set.shape[0]):
        temp = np.subtract(data_set[i], mean)
        temp = np.array([temp])
        temp1 = temp.T
        res += np.matmul(temp1, temp)
        
    return res/(data_set.shape[0])

data_train, label_train = load_mnist('Fashion-MNIST', kind='train')
data_test, label_test = load_mnist('Fashion-MNIST', kind='t10k')


classifier = GaussianNB()
classifier.fit(data_train, label_train)

fuck = classifier.predict(data_test)
print("with out PCA the accuracy is :",accuracy_score(fuck, label_test))

mean_train = np.mean(data_train, axis=0)
accuracyList = []
for m in range(782,780,-30):
    fuck = (var(data_train, mean_train))


    argenValue, argenVector = LA.eigh(fuck)

    V = list(zip(*( sorted(zip(argenValue, argenVector)) )))[1]
    Vrev = V[::-1]
    for i in range(m):
        Vrev = np.delete(Vrev, (783-i), axis = 0)
    
    train = []
    test = []


    for j in range(len(label_train)):
        train.append(np.matmul(Vrev, data_train[j]))

    for j in range(len(label_test)):
        test.append(np.matmul(Vrev, data_test[j]))

    classifier = GaussianNB()
    classifier.fit(train, label_train)

    fuck = classifier.predict(test)
    

    accuracyList.append(accuracy_score(fuck,label_test))
    print(accuracy_score(fuck, label_test))
    
    
import matplotlib.pyplot as plt
x =np.linspace(start = 1, stop = 751, num = 26, dtype = int)
plt.plot(x,accuracyList)
plt.title("CCR")
plt.grid()
plt.xlabel("number of features")
plt.ylabel("accuracy")
plt.show()

sorted(argenValue).reverse()
plt.plot(((argenValue)))
plt.show()



