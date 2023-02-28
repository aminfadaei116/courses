from sklearn.cluster import AgglomerativeClustering
import numpy as np
from sklearn.feature_selection import VarianceThreshold
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
from sklearn.feature_selection import VarianceThreshold
from sklearn.metrics import confusion_matrix
from numpy import linalg as LA
from sklearn.cluster import KMeans
from time import process_time


train_data = np.loadtxt('Train_Data.csv', dtype=np.float32, delimiter=',')
train_labels = np.loadtxt('Train_Labels.csv', dtype=np.int32, delimiter=',')
test_data = np.loadtxt('Test_Data.csv', dtype=np.float32, delimiter=',')
test_labels = np.loadtxt('Test_Labels.csv', dtype=np.int32, delimiter=',')
class_names = ['1', '2', '3']


# Feature Selection
all_data = np.vstack((train_data,test_data))
all_data_labels=np.hstack((train_labels,test_labels))
sel = VarianceThreshold(threshold=0.90*(1-0.90))
all_data = sel.fit_transform(all_data)
all_data_size, _ = all_data.shape
_, feature_size = all_data.shape

def distance(data1, data2):
    return LA.norm(np.subtract(data1, data2), 2)



def with_index(seq):
    for i in range(len(seq)):
        yield i, seq[i]

def replace_all(seq, obj, replacement):
    for i, elem in with_index(seq):
        if elem == obj:
            seq[i] = replacement
      
start = process_time()
     
mean = np.mean(all_data, axis = 0)
maxdata = np.max(all_data, axis = 0)
mindata = np.min(all_data, axis = 0)


data2 = {1:[], 2:[], 3:[]}
for i in range(100):
    clustering = []
    data = {1:[],2:[],3:[]}
    for j in range(all_data_size):
        maxim = [np.inf, 0, 0, 0]
        maxim[1] = distance(all_data[j], mindata)
        maxim[2] = distance(all_data[j], mean)
        maxim[3] = distance(all_data[j], maxdata)
        clustering.append(maxim.index(min(maxim)))
        data[maxim.index(min(maxim))].append(all_data[j])
    mindata = np.mean(data[1], axis = 0)
    mean = np.mean(data[2], axis = 0)
    maxdata = np.mean(data[3], axis = 0)

    if  len(data[1])==len(data2[1]) and len(data[2])==len(data2[2]) and len(data[3])==len(data2[3]):
        print("The K mean has ended in ", i, "stage")
        break
    data2 = data
    
    
tmp = clustering
replace_all(tmp,1,10)
replace_all(tmp,2,20)
replace_all(tmp,3,30)


replace_all(tmp,10,2)
replace_all(tmp,20,3)
replace_all(tmp,30,1)
    
    
print(accuracy_score(clustering, all_data_labels))

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


def distance(data1, data2):
    return LA.norm(np.subtract(data1, data2), 2)

plot_confusion_matrix(all_data_labels, clustering)

dist = {1:[], 2:[], 3:[]}

for i in range(all_data_size):
    dist[clustering[i]].append(distance(all_data[i], np.mean(data[clustering[i]],axis = 0)))

print("label 1 average distance",np.mean(dist[1]))
print("label 2 average distance",np.mean(dist[2]))
print("label 3 average distance",np.mean(dist[3]))


print("distance 1 and 2" , distance(np.mean(data[2], axis = 0), np.mean(data[1], axis =0)))
print("distance 3 and 2" , distance(np.mean(data[2], axis = 0), np.mean(data[3], axis =0)))
print("distance 1 and 3" , distance(np.mean(data[3], axis = 0), np.mean(data[1], axis =0)))


print('Time computing :', process_time()-start)