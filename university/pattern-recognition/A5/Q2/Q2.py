import numpy as np 
import sklearn
import pandas
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt 
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn import svm
from sklearn.metrics import accuracy_score
clf = svm.SVC(gamma='scale')

def plot_datas(data, label):
    fig = plt.figure()
    ax = Axes3D(fig)
    c1, c2 = split_classes(data, label)
    
    ax.scatter(xs=c1[:, 0], ys=c1[:, 1], zs=c1[:, 2] )
    ax.scatter(xs=c2[:, 0], ys=c2[:, 1], zs=c2[:, 2] )
    plt.show()


## Non linear mapping
def sqrt_func(c1):
    return np.sqrt(np.divide(1, np.abs(np.subtract(c1[0], c1[1]) )) )
def exp_func(c1):
    return np.exp(np.multiply(-1, np.abs(np.subtract(c1[0], c1[1]) )) )
def exp_func1(c1):
    return np.tanh(np.multiply(1,np.subtract(c1[0], c1[1])))
#    return np.exp(np.multiply(1, (np.subtract(c1[0], c1[1]) )) )

def split_classes(data, label):
    class1 = []
    class2 = []
    for d, l in zip(data, label):
        if l == 1:
            class1.append(d)
        elif l == 2:
            class2.append(d)
    return np.array(class1), np.array(class2)

def from_2d_to_3d(data):
    converted_data = []
    for i in data:
        converted_data.append([i[0], i[1], sqrt_func(i)]) # if we want ro change the function you only need to change this part
    return converted_data

# def kernel(x1, x2):

pca = PCA(n_components=2)


data = pandas.read_csv('haberman.data', header=None)

labels = data[3]
labels = labels.values
# print(labels)
data = data.drop(3, axis=1)
data = data.values
# print(data.describe)

principalComponents = pca.fit_transform(data)
principalDf = pandas.DataFrame(data = principalComponents)


c1, c2 = split_classes(principalDf.values, labels)
# print(c1)
# print(c1[:, 1])


# before training

# print(principalDf.describe)

# increase dimension

new_data = from_2d_to_3d(principalDf.values)
plot_datas(new_data,labels)

# print(new_data)
def get_sign(weights, point):
    sign = np.add(weights[0] , sum(np.multiply(np.array(point[1:]), weights[1:])))
    return 1 if sign >= 0.0 else -1


def get_gradients(weights, x_n, N):
    bias = weights[0]
    y_n = x_n[0]
    wgradient = bgradient = 0
    if (y_n * (sum(weights[1:]*x_n[1:])+bias)) < 1:
        wgradient = np.subtract(np.multiply((1/N),(weights[1:])) , np.multiply(y_n, x_n[1:]))
        bgradient = np.multiply((-1), (y_n))
    else:
        wgradient = np.multiply((1/N), (weights[1:]))
    return wgradient, bgradient

def train_weights(train_data, learning_rate):
    weight_length = len(train_data[0])
    weights = np.array([0] * weight_length).astype(float)
    N = len(train_data)
    for point in train_data:
        wgradient, bgradient = get_gradients(weights, point, N)
        weights[0] -= learning_rate*bgradient 
        weights[1:] -= learning_rate*wgradient
    return weights


learning_rate = 0.01
weights = train_weights(new_data, learning_rate)
#plot_datas(new_data, labels)
# for d, l in zip(new_data, labels):
#     true_class = l
#     estimated_class = get_class(weights, d)


right = 0
wrong = 0
for d, l in zip(new_data, labels):
    true_class = l
    estimated_class = get_sign(weights, d)
    if estimated_class == true_class:
        right += 1
    else:
        wrong += 1
accuracy = float(right)/float((right+wrong))
print(accuracy)

# ### Using Scikit learn 
clf.fit(new_data, labels)


predicted_labels = []

for d in new_data:
    predicted_labels.append(clf.predict([d]))
#print(predicted_labels)
plot_datas(new_data, predicted_labels)
print(accuracy_score(labels, predicted_labels, normalize=True))



