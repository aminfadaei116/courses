import numpy as np 
import pandas as pd 
from sklearn.feature_selection import VarianceThreshold
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt
from numpy import linalg as LA
from time import process_time

# Load dataset
Train_data = pd.read_csv('../data/Reduced Fashion-MNIST/Train_Data.csv', header=None)
Train_label = pd.read_csv('../data/Reduced Fashion-MNIST/Train_Labels.csv', header=None, dtype=int)

Test_data = pd.read_csv('../data/Reduced Fashion-MNIST/Test_Data.csv', header=None)
Test_label = pd.read_csv('../data/Reduced Fashion-MNIST/Test_Labels.csv', header=None, dtype=int)

# Convert to matrix
Train_data = Train_data.values
Train_label = Train_label.values

Test_data = Test_data.values
Test_label = Test_label.values

Train_data = np.multiply(Train_data, 0.01)
Test_data = np.multiply(Test_data, 0.01)

n_class = 10
data_dim = Train_data.shape[1]


# Spliting datas based on their class
classes = {0:[], 1:[], 2:[], 3:[], 4:[], 5:[], 6:[], 7:[], 8:[], 9:[]}
classes2 = {0:[], 1:[], 2:[], 3:[], 4:[], 5:[], 6:[], 7:[], 8:[], 9:[]}
for i in range(0, len(Train_data)):
    classes[int(Train_label[i])].append(Train_data[i])
 
start = process_time()

def parzen(data1, data2,hn):
    tmp = LA.norm(np.subtract(data1, data2),2)
    return np.exp(-1/2 * tmp /hn)

def confidence(res):
    res = sorted(res)
    return (res[-1]-res[-2])/res[-1]


estimated = []
confirmArray = [[[] for j in range(10)] for i in range(10)] 
hn = 16
i = 0

for test in Test_data:
    res = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for j in range (len(Train_data)):
        tmp = parzen(test, Train_data[j], hn)
        res[Train_label[j][0]] += tmp
    estimate = res.index(max(res))
    estimated.append(estimate)
    confirmArray[Test_label[i][0]][estimate].append(confidence(res))
    i += 1
        
print('Time computing :', process_time()-start)

for i in range(10) :
    for j in range(10) :
        confirmArray[i][j] = sum(confirmArray[i][j])/len(confirmArray[i][j]) if len(confirmArray[i][j]) != 0 else 0    



def plot_confusion_matrix(y_true, y_pred, 
                          normalize=False,
                          title=None,
                          cmap=plt.cm.Blues):
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

    # print(cm)

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

plot_confusion_matrix(Test_label, estimated, normalize=True)
plt.show()

plot_confusion_matrix(Test_label, estimated)
plt.show()


result = 0
for i in range(len(Test_label)):
    if Test_label[i][0] == estimated[i]:
        result +=1
print(100*result/len(Test_label))


def plot_matrix(cm,
                title=None,
                cmap=plt.cm.Blues):
    
    if not title:
        title = 'Confidence matrix'

    # print(cm)

    fig, ax = plt.subplots()
    im = ax.imshow(cm, interpolation='nearest', cmap=cmap)
    ax.figure.colorbar(im, ax=ax)
    
    ax.set(xticks=np.arange(cm.shape[1]),
           yticks=np.arange(cm.shape[0]),
           title=title,
           ylabel='True label',
           xlabel='Predicted label')

    plt.setp(ax.get_xticklabels(), rotation=45, ha="right",
             rotation_mode="anchor")

    fmt = '.2f'
    thresh = cm.max() / 2.
    for i in range(cm.shape[0]):
        for j in range(cm.shape[1]):
            ax.text(j, i, format(cm[i, j], fmt),
                    ha="center", va="center",
                    color="white" if cm[i, j] > thresh else "black")
    fig.tight_layout()
    return ax

plot_matrix(np.array(confirmArray))
plt.show()