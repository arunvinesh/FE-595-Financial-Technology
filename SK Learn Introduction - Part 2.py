# FE-595-Financial Technology
# SK Learn Introduction - Part 2
# Arun Thiravianathan
# CWID 10444121

# Required Libraries
import numpy as np
import matplotlib.pyplot as plt

import pandas as pd

# As suggested, from sklearn, I only import the features needed
from sklearn.cluster import KMeans
from sklearn.datasets import load_iris



# Loading Iris data sets
iris = load_iris()

# Creating a dataframe with the preditors that it will be used to identify the clusters
X = pd.DataFrame(iris.data, columns=iris['feature_names'])


# In order to proceed with the elbow heuristic, we need to calculate the Kmeans for the different number of clusters
# from 1 - no cluster to 10 (although we know that it is 3)
Inertia = {}
for k in range(1, 10):
    #Although we can change the parameters, the default ones should be good enough (we have only 150 points to cluster)
    kmeans = KMeans(n_clusters=k).fit(X)
    #in oder to plot the elbow, we store the inertia -Sum of Squares-
    Inertia[k] = kmeans.inertia_


# Plotting the Elbow
plt.figure()
plt.plot(list(Inertia.keys()), list(Inertia.values()))
plt.xlabel("Number of cluster")
plt.ylabel("Inertia")
plt.show()


# the following steps are not actually needed, when doing the exercesise i tried to plot to see how the clustering was
# as we are talking about 4 characteristics (dimensions) there isn't any way to plot it in a visualization all at the same time
# we have the option of 3-d missing 1, or 3-d with the 4th characteristic as size or shape, however, size/shape doesn't provide
# a vision on the distance between points/clusters
# I generate a Scatter plot matrix (using matplotlib and subplot)

kmeans = KMeans(n_clusters=3).fit(X)

X["clusters"] = kmeans.labels_
x = X['sepal length (cm)']
y = X['sepal width (cm)']
z = X['petal length (cm)']
w = X['petal width (cm)']
col_b = X["clusters"]

plt.subplot(4, 4, 1)
plt.scatter(x, x, c = "w")
plt.text((x.max()+x.min())/2, (x.max()+x.min())/2, s= "Sepal Length",horizontalalignment='center',verticalalignment='center',fontsize = 14)
plt.ylabel('sepal length (cm)')

plt.subplot(4, 4, 5)
plt.scatter(x, y, c = col_b)
plt.ylabel('sepal width (cm)')

plt.subplot(4, 4, 9)
plt.scatter(x, z, c = col_b)
plt.ylabel('petal length (cm)')

plt.subplot(4, 4, 13)
plt.scatter(x, w, c = col_b)
plt.ylabel('petal width (cm)')
plt.xlabel('sepal length (cm)')

plt.subplot(4, 4, 2)
plt.scatter(y, x, c = col_b)

plt.subplot(4, 4, 6)
plt.scatter(y, y, c = "w")
plt.text((y.max()+y.min())/2, (y.max()+y.min())/2, s= "Sepal Width",horizontalalignment='center',verticalalignment='center',fontsize = 14)

plt.subplot(4, 4, 10)
plt.scatter(y, z, c = col_b)

plt.subplot(4, 4, 14)
plt.scatter(y, w, c = col_b)
plt.xlabel('sepal width (cm)')

plt.subplot(4, 4, 3)
plt.scatter(z, x, c = col_b)

plt.subplot(4, 4, 7)
plt.scatter(z, y, c = col_b)

plt.subplot(4, 4, 11)
plt.scatter(z, z, c = "w")
plt.text((z.max()+z.min())/2, (z.max()+z.min())/2, s= "Pethal Length",horizontalalignment='center',verticalalignment='center',fontsize = 14)

plt.subplot(4, 4, 15)
plt.scatter(z, w, c = col_b)
plt.xlabel('petal length (cm)')

plt.subplot(4, 4, 4)
plt.scatter(w, x, c = col_b)

plt.subplot(4, 4, 8)
plt.scatter(w, y, c = col_b)

plt.subplot(4, 4, 12)
plt.scatter(w, z, c = col_b)

plt.subplot(4, 4, 16)
plt.scatter(w, w, c = "w")
plt.text((w.max()+w.min())/2, (w.max()+w.min())/2, s= "Pethal Width",horizontalalignment='center',verticalalignment='center',fontsize = 14)
plt.xlabel('petal width (cm)')

plt.show()