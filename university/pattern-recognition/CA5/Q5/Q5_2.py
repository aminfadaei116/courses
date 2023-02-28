import numpy as np
import matplotlib.pyplot as plt
import csv

from sklearn.metrics import confusion_matrix
from time import time
import pandas as pd 
from sklearn.metrics import accuracy_score
from sklearn.svm import LinearSVC
from sklearn import svm
from sklearn.model_selection import GridSearchCV

# Load dataset
Train_data = pd.read_csv('Train_Data.csv', header=None)
Train_label = pd.read_csv('Train_Labels.csv', header=None, dtype=int)

Test_data = pd.read_csv('Test_Data.csv', header=None)
Test_label = pd.read_csv('Test_Labels.csv', header=None, dtype=int)

t1 = time()
C_range = np.logspace(-2, 10, 13)
gamma_range = np.logspace(-9, 3, 13)
param_grid = dict(gamma=gamma_range, C=C_range)
svr = svm.SVC(kernel='rbf',decision_function_shape='ovo')
clf = GridSearchCV(svr, param_grid=param_grid)
clf.fit(Train_data, Train_label)
test_result = clf.predict(Test_data)
print("training time: ", time()-t1," s")




def plot_confusion_matrix(y_true, y_pred, 
                          normalize=False,
                          title=None,
                          cmap=plt.cm.Blues):
    """
    This function prints and plots the confusion matrix.
    Normalization can be applied by setting `normalize=True`.
    """
    if not title:
        if normalize:
            title = 'Normalized confusion matrix'
        else:
            title = 'Confusion matrix, without normalization'

    # Compute confusion matrix
    cm = confusion_matrix(y_true, y_pred)
    # Only use the labels that appear in the data

    if normalize:
        cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
        print("Normalized confusion matrix")
    else:
        print('Confusion matrix, without normalization')

    print(cm)

    fig, ax = plt.subplots()
    im = ax.imshow(cm, interpolation='nearest', cmap=cmap)
    ax.figure.colorbar(im, ax=ax)
    # We want to show all ticks...
    ax.set(xticks=np.arange(cm.shape[1]),
           yticks=np.arange(cm.shape[0]),
           # ... and label them with the respective list entries
           title=title,
           ylabel='True label',
           xlabel='Predicted label')

    # Rotate the tick labels and set their alignment.
    plt.setp(ax.get_xticklabels(), rotation=45, ha="right",
             rotation_mode="anchor")

    # Loop over data dimensions and create text annotations.
    fmt = '.2f' if normalize else 'd'
    thresh = cm.max() / 2.
    for i in range(cm.shape[0]):
        for j in range(cm.shape[1]):
            ax.text(j, i, format(cm[i, j], fmt),
                    ha="center", va="center",
                    color="white" if cm[i, j] > thresh else "black")
    fig.tight_layout()
    return ax


plot_confusion_matrix(Test_label, test_result, normalize=True)
plt.show()

print(accuracy_score(Test_label, test_result, normalize=True))