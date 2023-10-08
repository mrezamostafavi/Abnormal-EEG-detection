# -*- coding: utf-8 -*-
"""TUH2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1hANM1pjctEonGsU6QfKM6884SR4Aonqm
"""

# Commented out IPython magic to ensure Python compatibility.
from google.colab import drive
drive.mount('/gdrive')
# %cd /gdrive

cd MyDrive/final dataset2

import numpy as np
import tensorflow as tf
import random as python_random

np.random.seed(100)
python_random.seed(100)
tf.random.set_seed(100)

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')
import tensorflow as tf
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, classification_report
from keras.regularizers import l2

train = pd.read_csv('train.csv')
test = pd.read_csv('test.csv')

Y_train = train[['abnormal','normal']]
X_train = train.drop(labels = ['abnormal','normal'],axis = 1)
Y_test = test[['abnormal','normal']]
X_test = test.drop(labels = ['abnormal','normal'],axis = 1)

X_test.drop('Unnamed: 0', inplace=True, axis=1)
X_train.drop('Unnamed: 0', inplace=True, axis=1)

from sklearn.preprocessing import MinMaxScaler

mm = MinMaxScaler()
X_test= mm.fit_transform(X_test)
X_test = pd.DataFrame(X_test)
X_train= mm.fit_transform(X_train)
X_train = pd.DataFrame(X_train)

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
X_test = scaler.fit_transform(X_test)
X_test = pd.DataFrame(X_test)
X_train = scaler.fit_transform(X_train)
X_train = pd.DataFrame(X_train)

X_train, X_val, Y_train, Y_val = train_test_split(X_train, Y_train, test_size = 0.2, random_state=4)

# Used Sequential
model=tf.keras.Sequential()
model.add(tf.keras.Input(
    shape=(15000,1),
    batch_size=None))
model.add(tf.keras.layers.Conv1D(8, (23), strides=3, activation='relu'))
model.add(tf.keras.layers.Dropout(.2))
model.add(tf.keras.layers.MaxPooling1D(2,strides=2))
model.add(tf.keras.layers.BatchNormalization())
model.add(tf.keras.layers.Conv1D(64, (13), strides=1, activation='relu'))
model.add(tf.keras.layers.MaxPooling1D(2,strides=2))
model.add(tf.keras.layers.Conv1D(128, (3), strides=1, activation='relu'))
model.add(tf.keras.layers.Conv1D(32, (7), strides=1, activation='relu'))
model.add(tf.keras.layers.MaxPooling1D(2,strides=2))
model.add(tf.keras.layers.Dropout(0.2))
model.add(tf.keras.layers.Conv1D(128, (11), strides=1, activation='relu'))
model.add(tf.keras.layers.Conv1D(64, (5), strides=1, activation='relu'))
model.add(tf.keras.layers.Conv1D(64, (9), strides=1, activation='relu'))
model.add(tf.keras.layers.Conv1D(48, (15), strides=1, activation='relu'))
model.add(tf.keras.layers.Dropout(0.1))
model.add(tf.keras.layers.MaxPooling1D(2,strides=2))
model.add(tf.keras.layers.Conv1D(32, (3), strides=1, activation='relu'))
model.add(tf.keras.layers.Conv1D(16, (3), strides=1, activation='relu'))
model.add(tf.keras.layers.MaxPooling1D(2,strides=2))
model.add(tf.keras.layers.BatchNormalization())
model.add(tf.keras.layers.Flatten())
model.add(tf.keras.layers.Dense(64,activation='relu'))
model.add(tf.keras.layers.Dropout(0.1))
model.add(tf.keras.layers.Dense(2,activation='softmax'))
model.summary()

optimizer = tf.keras.optimizers.Adam( learning_rate=0.00001,beta_1=0.9,beta_2=0.999,decay=1e-3)

model.compile(optimizer = optimizer , loss = "categorical_crossentropy", metrics=["accuracy"])

history = model.fit(X_train, Y_train, epochs = 150, validation_data= (X_val, Y_val),batch_size=128)
#score, acc = model.evaluate(X_val, Y_val)

fig, ax = plt.subplots(2,1)
ax[0].plot(history.history['loss'], color='b', label="Training loss")
ax[0].plot(history.history['val_loss'], color='r', label="validation loss",axes =ax[0])
legend = ax[0].legend(loc='best', shadow=True)

ax[1].plot(history.history['accuracy'], color='b', label="Training accuracy")
ax[1].plot(history.history['val_accuracy'], color='r',label="Validation accuracy")
legend = ax[1].legend(loc='best', shadow=True)

model_acc = model.evaluate(X_test, Y_test, verbose=0)[1]
print("Test Accuracy: {:.3f}%".format(model_acc * 100))

plt.figure(figsize=(12, 7))
plt.plot(history.history['accuracy'])
plt.plot(history.history['val_accuracy'])
plt.title('model accuracy')
plt.ylabel('accuracy')
plt.xlabel('epoch')
plt.legend(['train', 'val'], loc='upper left')
plt.show()

plt.figure(figsize=(12, 7))
plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.title('model loss')
plt.ylabel('loss')
plt.xlabel('epoch')
plt.legend(['train', 'val'], loc='upper left')
plt.show()

Y_pred = model.predict(X_test)
#Y_pred=np.argmax(Y_pred, axis=1)
Y_pred = pd.DataFrame(Y_pred)
Y_pred

Y_pred.loc[0].iat[0]=1

len(Y_pred)

for i in range(len(Y_pred)):

  if Y_pred.loc[i].iat[0] > 0.5:
    Y_pred.loc[i].iat[0] = 1
    Y_pred.loc[i].iat[1] = 0
  else:
    Y_pred.loc[i].iat[0] = 0
    Y_pred.loc[i].iat[1] = 1

Y_pred

Y_test

Y_test = np.array(Y_test)
Y_pred = np.array(Y_pred)

tn, fp, fn, tp = confusion_matrix(Y_test.argmax(axis=1), Y_pred.argmax(axis=1)).ravel()

cm = np.matrix([[tp, fn], [fp, tn]])
cm = np.array(cm)

cm = confusion_matrix(Y_test.argmax(axis=1), Y_pred.argmax(axis=1))

print(cm)

#recall
recall = (tp/(tp+fn))*100
print(recall)

#precision
p = (tp/(tp+fp))*100
print(p)

#f1
f = (recall*p*2/(recall+p))
print(f)

