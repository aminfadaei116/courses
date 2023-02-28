from skimage import io
import numpy as np
from numpy import linalg as LA
from sklearn.cluster import KMeans
import matplotlib.image as mpimg
import matplotlib.pyplot as plt




def displayImage(image):
    plt.imshow(image)
    plt.show()
    
#  read and show original image
image = io.imread('bird.png')
io.imshow(image)
io.show()
 
rows, cols = image.shape[0],image.shape[1]
image = image.reshape(rows*cols,3)
# do kmeans (think of order=20 clusters or so!)


clustering = KMeans(n_clusters=3, random_state=0).fit(image)

data = {0:[],1:[],2:[]}

for i in range(image.shape[0]):
    data[clustering.labels_[i]].append(image[i])

mean = []
for i in range(len(data)):
    mean.append(np.mean(data[i], axis = 0))
compress_image = []
for i in range(image.shape[0]):
    compress_image.append(mean[clustering.labels_[i]])
    
compress_image=np.reshape(compress_image,(rows, cols,3))

compress_image = compress_image.astype(int)
#imgplot = plt.imshow(compress_image)
io.imshow(compress_image)
io.show()

# get your clusters and labels
# find clusters and labels 
#labels = labels.reshape(rows,cols);  
#
#
#
## show decompressed image
#image = np.zeros((rows,cols,3),dtype=np.uint8 )
#for i in range(rows):
#    for j in range(cols):
#            image[i,j,:] = clusters[labels[i,j],:]
#io.imsave('compressed_image.png',image);
#io.imshow(image)
#io.show()