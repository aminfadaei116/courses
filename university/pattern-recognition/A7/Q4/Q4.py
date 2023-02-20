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
from sklearn.cluster import AffinityPropagation

def with_index(seq):
    for i in range(len(seq)):
        yield i, seq[i]

def replace_all(seq, obj, replacement):
    for i, elem in with_index(seq):
        if elem == obj:
            seq[i] = replacement
   
def distance(data1, data2):
    return LA.norm(np.subtract(data1, data2), 2)


def FindMin(data1, data2):
    tmp = []
    for i in range(len(data1)):
        for j in range(len(data2)):
            tmp.append(distance(data1[i], data2[j]))
    return min(tmp)
            
def FindMax(data1, data2):
    tmp = []
    for i in range(len(data1)):
        for j in range(len(data2)):
            if i==j or distance(data1[i], data2[j])==0: #to get rid of 0 distances 
                continue
            tmp.append(distance(data1[i], data2[j]))

    return min(tmp)

def SI(data, numCluster):
    inDis = []
    for i in range(1,numCluster+1):
        inDis.append(FindMax(data[i],data[i]))
        
    outDis = []
    
    for i in range(1, numCluster+1):
        for j in range(1, numCluster+1):
            if i == j:
                continue
            outDis.append(FindMin(data[i],data[j]))
        
    return min(outDis)/max(inDis)



train_data = np.loadtxt('Train_Data.csv', dtype=np.float32, delimiter=',')
train_labels = np.loadtxt('Train_Labels.csv', dtype=np.int32, delimiter=',')
test_data = np.loadtxt('Test_Data.csv', dtype=np.float32, delimiter=',')
test_labels = np.loadtxt('Test_Labels.csv', dtype=np.int32, delimiter=',')
class_names = ['1', '2', '3']

start = process_time()

# Feature Selection
all_data = np.vstack((train_data,test_data))
all_data_labels=np.hstack((train_labels,test_labels))
sel = VarianceThreshold(threshold=0.90*(1-0.90))
all_data = sel.fit_transform(all_data)
all_data_size, _ = all_data.shape
_, feature_size = all_data.shape


# use the method that you to see the result
clustering = AgglomerativeClustering(n_clusters=3).fit(all_data)
#clustering = AffinityPropagation(preference= -1200,damping=0.92).fit(all_data)
#clustering = KMeans(n_clusters=3, random_state=0).fit(all_data)

tmp = clustering.labels_
replace_all(tmp,0,10)
replace_all(tmp,1,20)
replace_all(tmp,2,30)


replace_all(tmp,10,1)
replace_all(tmp,20,3)
replace_all(tmp,30,2)

data = {1:[], 2:[], 3:[]}
dist = {1:[], 2:[], 3:[]}
for i in range(all_data_size):
    data[clustering.labels_[i]].append(all_data[i])
    

print(accuracy_score(clustering.labels_, all_data_labels))


#print(max([FindMax(data[1],data[1]),FindMax(data[2],data[2]),FindMax(data[3],data[3])]))

print("The SI parameter is:", SI(data, 3))



        
print('Time computing :', process_time()-start)
    
    

