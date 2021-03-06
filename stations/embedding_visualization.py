# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import pickle
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import numpy as np
from keras.models import load_model

model = load_model('models.h5')

weights = model.get_weights()

station_embedding = weights[0]
month_embedding = weights[2]
dow_embedding = weights[3]
hour_embedding = weights[4]
season_embedding = weights[5]

pca = PCA(n_components=2)
Y = pca.fit_transform(station_embedding)
names = [u'[서울 강남구 ]강남구',u'[서울 강동구 ]강동구',u'[서울 강북구 ]강북구',u'[서울 강서로 ]강서구',u'[서울 관악구 ]관악구',u'[서울 광진구 ]광진구',u'[서울 구로구 ]구로구',u'[서울 금천구 ]금천구',u'[서울 노원구 ]노원구',u'[서울 도봉구 ]도봉구',u'[서울 동대문구]동대문구',u'[서울 동작구 ]동작구',u'[서울 마포구 ]마포구',u'[서울 서대문구]서대문구',u'[서울 서초구 ]서초구',u'[서울 성동구 ]성동구',u'[서울 성북구 ]성북구',u'[서울 송파구 ]송파구',u'[서울 양천구 ]양천구',u'[서울 영등포구]영등포구',u'[서울 용산구 ]용산구',u'[서울 은평구 ]은평구',u'[서울 종로구 ]종로구',u'[서울 중구]중구',u'[서울 중랑구 ]중랑구',u'[서울 강남구 ]도산대로',u'[서울 강동구 ]천호대로',u'[서울 강서구 ]공항대로',u'[서울 동대문구]홍릉로',u'[서울 마포구 ]신촌로',u'[서울 성북구 ]정릉로',u'[서울 종로구 ]종로',u'[서울 중구 청]청계천로']
#for i in range(33):
#    names.append(i)
from matplotlib import font_manager, rc
font_name = font_manager.FontProperties(fname = '/usr/share/fonts/NanumBarunGothic.ttf').get_name()
plt.rc('font', family=font_name) 

plt.figure(figsize=(8,8))
plt.scatter(Y[:, 0], Y[:, 1])
for i, txt in enumerate(names):
    plt.annotate(txt, (Y[i, 0],Y[i, 1]))
plt.savefig('station_embedding1.png')
plt.show()

pca = PCA(n_components=2)
Y = pca.fit_transform(month_embedding)
names = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
plt.figure(figsize=(8,8))
plt.scatter(Y[:, 0], Y[:, 1])
for i, txt in enumerate(names):
    plt.annotate(txt, (Y[i, 0],Y[i, 1]))
plt.savefig('month_embedding.png')

pca = PCA(n_components=2)
Y = pca.fit_transform(dow_embedding)
names = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat','Sun']
plt.figure(figsize=(8,8))
plt.scatter(Y[:, 0], Y[:, 1])
for i, txt in enumerate(names):
    plt.annotate(txt, (Y[i, 0],Y[i, 1]))
plt.savefig('dow_embedding.png')

pca = PCA(n_components=2)
Y = pca.fit_transform(hour_embedding)
names = ['0', '1', '2', '3', '4', '5', '6','7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23']
plt.figure(figsize=(8,8))
plt.scatter(Y[:, 0], Y[:, 1])
for i, txt in enumerate(names):
    plt.annotate(txt, (Y[i, 0],Y[i, 1]))
plt.savefig('hour_embedding.png')

pca = PCA(n_components=2)
Y = pca.fit_transform(season_embedding)
names = ['spring', 'summer', 'fall', 'winter']
plt.figure(figsize=(8,8))
plt.scatter(Y[:, 0], Y[:, 1])
for i, txt in enumerate(names):
    plt.annotate(txt, (Y[i, 0],Y[i, 1]))
plt.savefig('season_embedding.png')
plt.show()
