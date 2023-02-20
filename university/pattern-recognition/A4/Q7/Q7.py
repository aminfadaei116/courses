import numpy as np
from MNIST_Loader import load_mnist
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
from math import floor
from numpy import linalg as LA
from sklearn.metrics import accuracy_score

# import sklearn
# print(sklearn.__version__)

data_train, label_train = load_mnist('Fashion-MNIST', kind='train')
data_test, label_test = load_mnist('Fashion-MNIST', kind='t10k')

from sklearn.decomposition import IncrementalPCA as PCA
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA

def CCR(method, n, clf=GaussianNB()) :
    trs = method(n_components=n)
    trs.fit(data_train, label_train)
    train = trs.transform(data_train)
    clf.fit(train, label_train)
    trs.fit(data_test, label_test)
    test = trs.transform(data_test)
    predicts = clf.predict(test)
    return accuracy_score(label_test, predicts)

pca, lda = [0], [0]
for n in range(1, 780,30) :
    pca.append(CCR(PCA, n))
    lda.append(CCR(LDA, n))

import matplotlib.pyplot as plt
x =np.linspace(start = 1, stop = 781, num = 27, dtype = int)
plt.plot(x,pca, color='b', label="PCA")
plt.plot(x,lda, color='g', label="LDA")
plt.title("CCR")
plt.grid()
plt.legend()
plt.xlabel("n_components")
plt.ylabel("accuracy")
plt.show()