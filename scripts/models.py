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
from sklearn.preprocessing import StandardScaler

import sys
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
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
from sklearn.tree import DecisionTreeClassifier, plot_tree
#====================
# Performance measure
#====================
from sklearn.metrics import confusion_matrix, accuracy_score
from sklearn.model_selection import train_test_split
import tensorflow as tf
#=====================================================================
# Define seed

np.random.seed(1234)
tf.random.set_seed(1234)

print(40*"=")
print("INITIALIZATING THE MODEL")
print(40*"=")

#Initialization Data
data = Data("EOS")
thresold_pump = 0.01
model_type = 'Return'
data.load_data(pump_thresold=thresold_pump)

#print(data.df.corr())
#================
# Data Parameters
#================

features = data.df.iloc[:,3:-2].columns # select features for our model
features = features.drop('date')


#==============
# Creating Data
#==============
#choose for our estimation
data.create_RNN_data(reg=model_type,LAG=5,columns=features,pump_thresold=thresold_pump)
print(f'dimension of data: {data.df.shape}')

#%%
#=======================#
# Neural Network models #
#=======================#


# Parameters
#===========
architecture = [10]
activation_fct = "relu"
drop_out = 0.2
optimizer = "adam"

model=RNN()

# # add callback for early stopping
# model.create_model(data,architecture=architecture,batch_normalization=True,activation=activation_fct,drop_out=drop_out,opti=optimizer)
# model.train_model(data,verbose=0,epoch=20)
# model.show_performance(label_='Error graph',data=data)
# pred=model.model(data.X_te)

# plt.plot(pred.numpy().flatten(),color='k',label='Pred')
# plt.plot(data.y_te.flatten(),color='blue',linestyle='--',label='True')
# plt.legend()
# plt.show()

#===============#
# Simple models #
#===============#

print("\n","==== Simple model ====")
# standardize and choose our data
X = data.df[features]

# Standardize date
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)


y = data.df['pump_5'].values
print(f'number return > {thresold_pump}: {np.sum(y==1)}')
print(f'shape of y: {y.shape}')

# plt.scatter(X.index,y)
# plt.show()
feature_names = [column for column in X.columns]

pct_split = 0.3
split = int((1-pct_split)*len(X))
X_train, X_test, y_train, y_test = X_scaled[:split],X_scaled[split:], y[:split], y[split:]

#plot to see train test data
# X_tr, X_te = X.iloc[:split,:], X.iloc[split:,:]
# plt.plot(X_tr.index,X_tr['Close'])
# plt.plot(X_te.index,X_te['Close'])
# plt.ylabel("Close price ($)")
# plt.show()

print("\n","=== Random Forest ===")
# https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html
randomForest = RandomForestClassifier(criterion='entropy',n_estimators = 1000, random_state = 42).fit(X_train,y_train)

pscore_train = accuracy_score(y_test, randomForest.predict(X_test))
print(f'Accruracy score: {pscore_train}')

clf = confusion_matrix(y_test, randomForest.predict(X_test))
print("\n","Confusion Matrix")
print(clf)

#print(randomForest.predict_proba(X_test)[:15]) #only 1
print("\n","=== Logistic regresion ===")
# https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html
clf = LogisticRegression().fit(X_train, y_train)

pscore_train = accuracy_score(y_test, clf.predict(X_test))
print(f'Accruracy score: {pscore_train}')
print("\n","Confusion Matrix")
print(confusion_matrix(y_test, clf.predict(X_test)))


print("\n","=== Decision Tree ===")
# https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html
clf = DecisionTreeClassifier().fit(X_train, y_train)

pscore_train = accuracy_score(y_test, clf.predict(X_test))
print(f'Accruracy score: {pscore_train}')
print("\n","Confusion Matrix")
print(confusion_matrix(y_test, clf.predict(X_test)))

# plot decision Tree
#plot_tree(clf)
# %%
