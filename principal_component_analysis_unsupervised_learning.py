# -*- coding: utf-8 -*-
"""
Created on Fri Sep 24 03:23:14 2021

@author: Mahfuz_Shazol
"""

from sklearn import datasets
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

iris=datasets.load_iris()
print(iris.data.shape)
print(iris.get('feature_names'))
print(iris.data[0:6,:])


#PCA
pca=PCA(n_components=2)
print(pca)

x=pca.fit_transform(iris.data)
print(x.shape)
print(x[0:6,:])

plt.scatter(x[:,0], x[:,1],c=iris.target)





