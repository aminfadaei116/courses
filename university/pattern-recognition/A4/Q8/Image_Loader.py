import numpy as np
import matplotlib.pyplot as plt
import math
import operator
import matplotlib.image as mpimg
from PIL import Image

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


train_data, train_label = readImages('FACES/', 'Train',28)
test_data, test_label = readImages('FACES/', 'Test',14)
