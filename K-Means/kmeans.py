# -*- coding: utf-8 -*-

import csv
import numpy as np
import matplotlib.pyplot as plt

def kMeans(X, K, maxIters):

    centroids = X[np.random.choice(np.arange(len(X)), K), :]
    for i in range(maxIters):
        C = np.array([np.argmin([np.dot(x_i-y_k, x_i-y_k) for y_k in centroids]) for x_i in X])
        centroids = [X[C == k].mean(axis = 0) for k in range(K)]
    return np.array(centroids) , C
    
    
def main():
    reader=csv.reader(open("iristwod.csv","rt"),delimiter=',')
    x=list(reader)
    data = []
    data = np.array(x).astype('float')
    centroids, C = kMeans(data, K = 3, maxIters=10)
    print (centroids)
    print (C)
    #plt.plot(centroids,)
    print (data.size)
    markers= ['s','o','x']
    colors = ['red','blue','g']
    for i in range (int(data.size/2)):
        plt.scatter(data[i,0], data[i,1],c=colors[C[i]], alpha=0.8, marker=markers[C[i]])

main()
    