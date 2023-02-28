import numpy as np 
import pandas as pd 
from sklearn.feature_selection import VarianceThreshold
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt
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
classes = {0:[], 1:[], 2:[], 3:[], 4:[], 5:[], 6:[], 7:[], 8:[], 9:[], "Rejection":[]}
classes2 = {0:[], 1:[], 2:[], 3:[], 4:[], 5:[], 6:[], 7:[], 8:[], 9:[], "Rejection":[]}
for i in range(0, len(Train_data)):
    classes[int(Train_label[i])].append(Train_data[i])
    classes2[int(Train_label[i])].append(Train_data[i])
    
for i in range(len(Test_data)):
    classes2[int(Test_label[i])].append(Test_data[i])


start = process_time()
estimated_mean = {}
estimated_var = {}

# Estimating mean
for i in range(n_class):
    tmp = np.zeros(data_dim)
    for d in classes[i]:
        tmp = np.add(tmp, d)
    tmp = np.multiply(tmp, (1/len(classes[i])))
    estimated_mean[i] = tmp

# Estimating var
for i in range(10):
    tmp = np.zeros((data_dim, data_dim))
    for d in classes[i]:
        sub = np.subtract(d, estimated_mean[i])
        sub = np.array([sub])
        sub1 = sub.T
        a = np.matmul(sub1, sub)
        tmp = np.add(tmp, a)
    tmp = np.multiply(tmp, (1/len(classes[i])))
    alpha = 0.019

    estimated_var[i] = np.add(np.multiply((1-alpha),tmp),np.multiply(np.multiply(alpha,np.identity(data_dim)), np.multiply(np.trace(tmp),1/data_dim)))


prior_knowledge = {}

for i in range(10):
    prior_knowledge[i] = len(classes[i]) / 10000


print('time of train :', process_time()-start)
def model(x, mu, cov, prior):
    ret = 1
    ret /= (2*np.pi)**(91)
    ret /= np.sqrt(np.linalg.det(cov))
    ret *= prior
    
    sub = np.array([x - mu])  
    sub1 = sub.T
    
    tmp = np.multiply(-0.5, np.matmul(sub, np.matmul(np.linalg.inv(cov), sub1)))
    tmp = np.exp(tmp)

    return np.multiply(ret, tmp)[0][0]


    
def estimate_label(data, landaS, landaR):
    scores = []
    all = 0
    for i in range(10):
        task = model(data, estimated_mean[i], estimated_var[i], prior_knowledge[i])
        scores.append(task)
        all += task
    j = scores.index(max(scores))
    if landaR*all<landaS*(all - model(data, estimated_mean[j], estimated_var[j], prior_knowledge[j])):
        return 10
    return scores.index(max(scores))


def confidence(data):
    scores = []
    for i in range(10):
        scores.append(model(data, estimated_mean[i], estimated_var[i], prior_knowledge[i]))
    scores = sorted(scores)
    return (scores[-1]-scores[-2])/scores[-1]

start = process_time()

estimated = []
i = 0
result = 0
landaS = 10
landaR = 0.8
confirmArray = [[[] for j in range(11)] for i in range(11)]
for d in Test_data:
    tmp = estimate_label(d, landaS, landaR)
    confirmArray[Test_label[i][0]][tmp].append(confidence(d))
    estimated.append(tmp)
    if Test_label[i] == tmp:
        result += 1
    i += 1

for i in range(11) :
    for j in range(11) :
        confirmArray[i][j] = sum(confirmArray[i][j])/len(confirmArray[i][j]) if len(confirmArray[i][j]) != 0 else 0    
    
print('time of Test :', process_time()-start)
    
    
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

print(100*result/len(Test_label))


def plot_matrix(cm,
                title=None,
                cmap=plt.cm.Blues):
    
    if not title:
        title = 'Confidence matrix'

    print(cm)

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