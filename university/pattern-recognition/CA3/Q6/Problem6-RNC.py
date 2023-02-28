from pandas import DataFrame, read_csv
import pandas as pd
import numpy as np

trainDataCsv = '../data/Reduced Fashion-MNIST/Train_Data.csv'
trainLabelCsv = '../data/Reduced Fashion-MNIST/Train_Labels.csv'
testDataCsv = '../data/Reduced Fashion-MNIST/Test_Data.csv'
testLabelCsv = '../data/Reduced Fashion-MNIST/Test_Labels.csv'

trainData = pd.read_csv(trainDataCsv, header=None)
trainData = np.array(trainData).astype(np.float64)
trainLabel = pd.read_csv(trainLabelCsv, header=None, usecols=[0])[0]
trainNumber = len(trainLabel)
testData = pd.read_csv(testDataCsv, header=None)
testData = np.array(testData).astype(np.float64)
testLabel = pd.read_csv(testLabelCsv, header=None, usecols=[0])[0]
testNumber = len(testLabel)

from sklearn.neighbors import RadiusNeighborsClassifier

r = 3000 # <------------------------------------

clf = RadiusNeighborsClassifier(radius = r)
# radius=1.0, weights=’uniform’, algorithm=’auto’
# leaf_size=30, p=2, metric=’minkowski’, outlier_label=None
# metric_params=None, n_jobs=None, **kwargs

from time import process_time

start = process_time()
clf.fit(trainData, trainLabel)
print('time of train :', process_time()-start)

start = process_time()
predicts = clf.predict(testData)
print('time of test :', process_time()-start)


from sklearn.metrics import accuracy_score

print("Accuracy : ", accuracy_score(testLabel, predicts))


import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix

def plot_confusion_matrix(y_true, y_pred, classes,
                          normalize=False,
                          title=None,
                          cmap=plt.cm.Blues):
    if not title:
        if normalize:
            title = 'Normalized confusion matrix'
        else:
            title = 'Confusion matrix, without normalization'

    cm = confusion_matrix(y_true, y_pred)
    if normalize:
        cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
        print("Normalized confusion matrix")
    else:
        print('Confusion matrix, without normalization')
    
    fig, ax = plt.subplots()
    im = ax.imshow(cm, interpolation='nearest', cmap=cmap)
    ax.figure.colorbar(im, ax=ax)
    ax.set(xticks=np.arange(cm.shape[1]),
           yticks=np.arange(cm.shape[0]),
           xticklabels=classes, yticklabels=classes,
           title=title,
           ylabel='True label',
           xlabel='Predicted label')

    plt.setp(ax.get_xticklabels(), rotation=45, ha="right", rotation_mode="anchor")

    fmt = '.2f' if normalize else 'd'
    thresh = cm.max() / 2.
    for i in range(cm.shape[0]):
        for j in range(cm.shape[1]):
            ax.text(j, i, format(cm[i, j], fmt),
                    ha="center", va="center",
                    color="white" if cm[i, j] > thresh else "black")
    fig.tight_layout()
    return ax


plot_confusion_matrix(testLabel, predicts, classes=range(10),
                      title='Confusion matrix, without normalization')
plot_confusion_matrix(testLabel, predicts, classes=range(10), normalize=True,
                      title='Normalized confusion matrix')

plt.show()