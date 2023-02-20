import numpy as np
import matplotlib.pyplot as plt
import math
import operator
import matplotlib.image as mpimg
from PIL import Image
from sklearn.decomposition import PCA

def readImages(path, type, n):
    list_ = list()
    for i in range(1, n+1):
        img = mpimg.imread(path + type +'/' + str(i) + '.png')
        list_.append(img)

    data_size = len(list_)
    labels=[]
    temp = 1
    if(type=='Train'):
        temp = 2
    for i in range(0, data_size):
        class_label = math.floor(i/temp)
        labels.append(class_label)
    return np.array(list_), np.array(labels)

def make_pca (image_list, n_components):
    pca = PCA(n_components=n_components)
    pca.fit(image_list)
    return pca

f = False
def predict_label (test_img, train_data):
    global f
    err = [0 for i in range(len(train_data))]
    for train_idx in range(len(train_data)):
        for i in range(len(test_img)):
                    err[train_idx] += (train_data[train_idx][i] - test_img[i])**2
    for i in range(len(err)):
        err[i] = math.sqrt(err[i])
    return math.floor(err.index(min(err)) / 2)


def euclidian_recognize(train_data, test_data, test_label, pca):
    reduced_train_data = np.array(pca.transform(train_data))
    reduced_test_data = np.array(pca.transform(test_data))
    correct = 0
    i = 0
    for test_img in reduced_test_data:
        if predict_label(test_img, reduced_train_data) == test_label[i]:
            correct += 1
        i += 1
    return reduced_test_data, correct / len(test_data)

def get_error (image1, image2):
    err = 0
    for i in range(len(image1)):
        err += (image1[i] - image2[i])**2
    return err**(1/len(image1))


train_data, train_label = readImages('FACES/', 'Train',28)
test_data, test_label = readImages('FACES/', 'Test',14)
print (train_data[0].shape)
nsamples, nx, ny, nz = train_data.shape
train_data = train_data.reshape(nsamples, nx * ny * nz)
nsamples, nx, ny, nz = test_data.shape
test_data = test_data.reshape(nsamples, nx * ny * nz)

accuracy = []
reduced_test_datas = []

for i in range (1, 29):
    pca = make_pca(train_data, i)
    reduced_test_data, acc = euclidian_recognize(train_data, test_data, test_label, pca)
    reduced_test_datas.append(reduced_test_data)
    accuracy.append(acc)

plt.figure()
plt.xlim(left=1, right=30)
plt.plot([i for i in range(1, len(accuracy) + 1)], accuracy)
plt.show()

errors = []
total_err = 0

for image_pack in reduced_test_datas:
    total_err = 0
    for i, img in enumerate(image_pack):
        total_err += get_error(img, test_data[i])
    total_err /= len(image_pack)
    errors.append(total_err)
plt.figure()
plt.xlim(left=1, right=30)
plt.plot([i for i in range(1, len(errors) + 1)], errors)
plt.show()        
