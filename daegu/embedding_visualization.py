# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import pickle
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import numpy as np
from keras.models import load_model

model = load_model('model_so2.h5')

weights = model.get_weights()

mapidx_embedding = weights[0]
month_embedding = weights[2]
dow_embedding = weights[3]
hour_embedding = weights[4]

pca = PCA(n_components=2)
Y = pca.fit_transform(mapidx_embedding)
names = []
for i in range(1024):
    names.append(i)

plt.figure(figsize=(8,8))
plt.scatter(Y[:, 0], Y[:, 1])
for i, txt in enumerate(names):
    plt.annotate(txt, (Y[i, 0],Y[i, 1]))
plt.savefig('mapidx_embedding_so2.png')
plt.show()

pca = PCA(n_components=2)
Y = pca.fit_transform(month_embedding)
names = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
plt.figure(figsize=(8,8))
plt.scatter(Y[:, 0], Y[:, 1])
for i, txt in enumerate(names):
    plt.annotate(txt, (Y[i, 0],Y[i, 1]))
plt.savefig('month_embedding_so2.png')

pca = PCA(n_components=2)
Y = pca.fit_transform(dow_embedding)
names = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat','Sun']
plt.figure(figsize=(8,8))
plt.scatter(Y[:, 0], Y[:, 1])
for i, txt in enumerate(names):
    plt.annotate(txt, (Y[i, 0],Y[i, 1]))
plt.savefig('dow_embedding_so2.png')

pca = PCA(n_components=2)
Y = pca.fit_transform(hour_embedding)
names = ['0', '1', '2', '3', '4', '5', '6','7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23']
plt.figure(figsize=(8,8))
plt.scatter(Y[:, 0], Y[:, 1])
for i, txt in enumerate(names):
    plt.annotate(txt, (Y[i, 0],Y[i, 1]))
plt.savefig('hour_embedding_so2.png')

plt.show()
