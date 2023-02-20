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


def with_index(seq):
    for i in range(len(seq)):
        yield i, seq[i]

def replace_all(seq, obj, replacement):
    for i, elem in with_index(seq):
        if elem == obj:
            seq[i] = replacement
            


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

start = process_time()

clustering = KMeans(n_clusters=3, random_state=0).fit(all_data)

tmp = clustering.labels_
replace_all(tmp,0,10)
replace_all(tmp,1,20)
replace_all(tmp,2,30)



replace_all(tmp,10,3)#for k-mean put replace_all(tmp,10,1)
replace_all(tmp,20,1)#for k-mean put replace_all(tmp,10,3)
replace_all(tmp,30,2)



    
    
print(accuracy_score(clustering.labels_, all_data_labels))


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

plot_confusion_matrix(all_data_labels, clustering.labels_)



data = {1:[], 2:[], 3:[]}
dist = {1:[], 2:[], 3:[]}
for i in range(all_data_size):
    data[clustering.labels_[i]].append(all_data[i])
    
for i in range(all_data_size):
    dist[clustering.labels_[i]].append(distance(all_data[i], np.mean(data[clustering.labels_[i]],axis = 0)))

print("label 1 average distance",np.mean(dist[1]))
print("label 2 average distance",np.mean(dist[2]))
print("label 3 average distance",np.mean(dist[3]))


print("distance 1 and 2" , distance(np.mean(data[2], axis = 0), np.mean(data[1], axis =0)))
print("distance 3 and 2" , distance(np.mean(data[2], axis = 0), np.mean(data[3], axis =0)))
print("distance 1 and 3" , distance(np.mean(data[3], axis = 0), np.mean(data[1], axis =0)))

print('Time computing :', process_time()-start)
