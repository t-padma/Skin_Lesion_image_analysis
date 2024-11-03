## Author: Aditya

import sys
import numpy as np
import random
import matplotlib.pyplot as plt 
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA 
from sklearn import metrics
np.set_printoptions(threshold=sys.maxsize)


Train_Data=np.load('encoded_train_new.npy')
Test_Data=np.load('encoded_test_new.npy')
Train_Labels=np.load('label_train.npy') 
Test_Labels=np.load('label_test.npy')
c = ['AK', 'Bee', 'BKL' , 'DF', 'MEL', 'NV', 'sec', 'v Asc 'J

def CLS(n):
    if n=='AK':
        return 1 
    elif n=='BCC':
        return 2 
    elif n=='BKL':
        return 2
    elif n=='DF':
        return 3
    elif n=='MEL':
        return 4 
    elif n=='NV':
        return 5 
    elif n=='SCC':
        return 6 
    elif n=='VASC':
        return 7


Train_Labels_N = np.array(list(map(CLS,Train_Labels)))

print(Train_Labels_N.shape) 
print(Train_Data.shape[O]) 
print(Test_Data.shape) 
print(Train_Labels.shape) 
print(Test_Labels.shape)

Train_vector=np.reshape(Train_Data,(Train_Data.shape[O],Train_Data.Shape[1]*Train_Data.shape[2]*Train_Data.shape[3])) 

Test_vector=np.reshape(Test_Data,(Test_Data.shape[O],Test_Data.Shape[1]*Test_Data.shape[2]*Test_Data.shape[3]))

print(Train_vector.shape) 
print(Test_vector.shape)

pea= PCA(n_components=2)
principalComponents = pca.fit_transform(Train_vector) 
np.shape(principalComponents)
N_C=[4,5,6,7,8,9]


fig, axs = plt.subplots(1, 3) 
for i in range(3):
    KM_PCA = KMeans(n_clusters=N_C[i], random_state=O,max_iter=1000).fit(principalComponents) 
    Predicted_Train_PCA = KM_PCA.labels_.reshape(18998,1) 
    centroids=KM_PCA.cluster_centers 
    axs[i].scatter(principalComponents[:,O],principalComponents[:,1],c=Predicted_Train_PCA, cmap=plt.cm.Paired)

    axs[i].scatter( centroids[:, OJ, centroids[:, 1], marker="x", s=169,
    linewidths=3, color="k", zorder=10)
    # square pLot
    axs[i].set_aspect('equal', adjustable='box') 
    fig.set_figwidth(20)
    fig.set_figheight(20)


fig, axs = plt.subplots(1, 3)
for i in range(3):
    KM_PCA = KMeans(n_clusters=N_C[iJ, random_state=O,max_iter=1OOO).fit(principalComponents) 
    Predicted_Train_PCA=KM_PCA.labels_.reshape(18998,1) 
    centroids=KM_PCA.cluster_centers
    axs[iJ.scatter(principalComponents[:,OJ,principalComponents[:,1J,c=Train_Labels_N, cmap=plt.cm.Paired)

    axs[iJ.scatter( centroids[:, OJ, centroids[:, 1J, marker="x", s=169, linewidths=3, color="k", zorder=1O)
    # square plot
    axs[iJ.set_aspect('equal', adjustable='box') 
    fig.set_figwidth(20)
    fig.set_figheight(20)
    axs[iJ.scatter(principalComponents[:,OJ,principalComponents[:,1J,c=Predicted_Train_PCA, cmap=plt.cm.Paired)

    axs[iJ.scatter( centroids[:, OJ, centroids[:, 1J, marker="x", s=169, linewidths=3, color="k", zorder=1O)
    # square plot
    axs[iJ.set_aspect('equal', adjustable='box') 
    fig.set_figwidth(20)
    fig.set_figheight(20)



fig, axs = plt.subplots(1, 3)
for i in range(3):
    KM_PCA = KMeans(n_clusters=N_C[i+3J, random_state=0,max_iter=1OOO).fit(principalComponents) 
    Predicted_Train_PCA=KM_PCA.labels_.reshape(18998,1) 
    centroids=KM_PCA.cluster_centers
    axs[iJ.scatter(principalComponents[:,OJ,principalComponents[:,1J,c=Train_Labels_N, cmap=plt.cm.Paired)

    axs [iJ.scatter(centroids[:, OJ, centroids[:, 1J, marker="x", s=169,linewidths=3, color="k", zorder=1O)
    # square plot
    axs[iJ .set_aspect('equal', adjustable='box') 
    fig.set_figwidth(20)
    fig.set_figheight(20)



for i in range(5):
    KM= KMeans(n_clusters=8, random_state=i,max_iter=1000).fit(Train_vector) 
    Train_Labels_Predicted=KM.labels_.reshape(18998,) 
    ARI_O=metrics.adjusted_rand_score(Train_Labels_N,Train_Labels_Predicted)
    print(ARI_O)


for i in range(5):
    KM= KMeans(n_clusters=7, random_state=i,max_iter=1000).fit(Train_vector) 
    Train_Labels_Predicted=KM.labels_.reshape(18998,) 
    ARI_O=metrics.adjusted_rand_score(Train_Labels_N,Train_Labels_Predicted) 
    print(ARI_O)

for i in range(5):
    KM= KMeans(n_clusters=6, random_state=i,max_iter=1000).fit(Train_vector) 
    Train_Labels_Predicted=KM.labels_.reshape(18998,) 
    ARI_O=metrics.adjusted_rand_score(Train_Labels_N,Train_Labels_Predicted) 
    print(ARI_O)


for i in range(5):
    KM= KMeans(n_clusters=5, random_state=i,max_iter=1000).fit(Train_vector) 
    Train_Labels_Predicted=KM.labels_.reshape(18998,) 
    ARI_0=metrics.adjusted_rand_score(Train_Labels_N,Train_Labels_Predicted) 
    print(ARI_0)

for i in range(5):
    KM= KMeans(n_clusters=9, random_state=i,max_iter=1000).fit(Train_vector) 
    Train_Labels_Predicted=KM.labels_.reshape(18998,) 
    ARI_0=metrics.adjusted_rand_score(Train_Labels_N,Train_Labels_Predicted) 
    print(ARI_0)
