#%%
#================
# Plot librairies
#================
import matplotlib.pyplot as plt
import seaborn as sns

#======================
# Scientific librairies
#======================
import numpy as np
import pandas as pd

import sys
from data import Data

#=========
# NN model
#=========
from NN_models import RNN

#=============
# Simple model
#=============
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
#====================
# Performance measure
#====================
from sklearn.metrics import confusion_matrix, accuracy_score
from sklearn.model_selection import train_test_split

#=====================================================================
#Initialization Data
data = Data("BTC")
data.load_data()
#choose for our estimation
data.create_RNN_data(reg='return',LAG=1)
print(f'dimension of data: {data.df.shape}')

#%%
#=======================#
# Neural Network models #
#=======================#

model=RNN()

# add callback for early stopping
model.create_model(data,architecture=[10,10,10],batch_normalization=True,activation="relu",drop_out=0.2)
model.train_model(data,verbose=0,epoch=100)
model.show_performance(label_='Error graph',data=data)
pred=model.model(data.X_te)

# plt.plot(pred.numpy().flatten(),color='k',label='Pred')
# plt.plot(data.y_te.flatten(),color='blue',linestyle='--',label='True')
# plt.legend()
# plt.show()

#===============#
# Simple models #
#===============#
print("\n","==== Simple model ====")
# standardize and choose our data
X = data.df[["Volume","vix","gvz","Close_std","RSI_10","tweet_count",'Mass Index']]
y = np.where(data.df['pump_5'].values > 0.05,0,1)
feature_names = [column for column in X.columns]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

print("\n","=== Random Forest ===")
randomForest = RandomForestClassifier().fit(X_train,y_train)

pscore_train = accuracy_score(y_test, randomForest.predict(X_test))
print(f'Accruracy score: {pscore_train}')

clf = confusion_matrix(y_test, randomForest.predict(X_test))
print("\n","Confusion Matrix")
print(clf)

print("\n","=== Logistic regresion ===")
clf = LogisticRegression(random_state=0).fit(X_train, y_train)

pscore_train = accuracy_score(y_test, clf.predict(X_test))
print(f'Accruracy score: {pscore_train}')
print("\n","Confusion Matrix")
print(confusion_matrix(y_test, clf.predict(X_test)))

