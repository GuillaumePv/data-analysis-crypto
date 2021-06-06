
#==========================
# Libairies to manage paths
#=========================
from os import chdir, getcwd
import os
from pathlib import Path

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
import pickle
from pickle import load

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

# A method which works well with python 3.4 +
path_original = Path(__file__).resolve().parents[1]

path_latex = (path_original / "./latex/").resolve()

if(os.path.isdir(path_latex) == False):
    os.mkdir(path_latex)

path_model = (path_original / "./models/").resolve()
if(os.path.isdir(path_model) == False):
    os.mkdir(path_model)


cryptos = ["BTC","ETH","EOS"]
data_list = []
for crypto in cryptos:
    accurracy_list = []
    print(40*"=")
    print(f"INITIALIZATING THE MODEL FOR {crypto}")
    print(40*"=")

    #Initialization Data
    data = Data(crypto)
    thresold_pump = 0.01
    model_type = 'Return'
    data.load_data(pump_thresold=thresold_pump)

    #print(data.df.corr())
    #================
    # Data Parameters
    #================

    features = data.df.iloc[:,3:-2].columns # select features for our model
    features = features.drop('date')
    features = features.drop('Adj Close')

    #print(features)
    #==============
    # Creating Data
    #==============
    #choose for our estimation
    data.create_RNN_data(reg=model_type,LAG=10,columns=features,pump_thresold=thresold_pump)
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

    print("===== Running LSTM =====")
    model=RNN(crypto,False)

    # # add callback for early stopping
    model.create_model(data,architecture=architecture,batch_normalization=True,activation=activation_fct,drop_out=drop_out,opti=optimizer)
    model.train_model(data,verbose=1,epoch=10)
    model.show_performance(label_='Error graph',data=data)

    accurracy_list.append(model.accuracy)
    print("===== Running conv1D-LSTM =====")
    model=RNN(crypto,True)

    # # add callback for early stopping
    model.create_model(data,architecture=architecture,batch_normalization=True,activation=activation_fct,drop_out=drop_out,opti=optimizer)
    model.train_model(data,verbose=1,epoch=10)
    model.show_performance(label_='Error graph',data=data)
    accurracy_list.append(model.accuracy)
    

    #===============#
    # Simple models #
    #===============#

    print("\n","==== Simple model ====")
    # standardize and choose our data
    X = data.df[features]

    scaler = load(open(str(path_model)+'/scaler.pkl', 'rb'))
    # Standardize date
    X_scaled = scaler.fit_transform(X)


    y = data.df['pump'].values
    print(f'number return <= {thresold_pump}: {np.sum(y==1)}')
    print(f'shape of y: {y.shape}')

    feature_names = [column for column in X.columns]
    
    pct_split = 0.2
    split = int((1-pct_split)*len(X))
    X_train, X_test, y_train, y_test = X_scaled[:split],X_scaled[split:], y[:split], y[split:]

  
    print(f'(test) number return <= {thresold_pump}: {np.sum(y_test==1)}')

    print("\n","=== Random Forest ===")
    # https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html
    randomForest = RandomForestClassifier(criterion='entropy', random_state = 42).fit(X_train,y_train)


    filename = str(path_model)+f'/{crypto}_rf_finalized_model.sav'
    pickle.dump(randomForest, open(filename, 'wb'))
    print("=== Random forest model saved !! ===")

    pscore_train = accuracy_score(y_test, randomForest.predict(X_test))
    accurracy_list.append(pscore_train)
    print(f'Accruracy score: {pscore_train}')
    #print(randomForest.predict_proba(X_test))
    clf = confusion_matrix(y_test, randomForest.predict(X_test))
    print("\n","Confusion Matrix")
    print(clf)

    #print(randomForest.predict_proba(X_test)[:15]) #only 1
    print("\n","=== Logistic regresion ===")
    # https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html
    clf = LogisticRegression().fit(X_train, y_train)

    pscore_train = accuracy_score(y_test, clf.predict(X_test))
    accurracy_list.append(pscore_train)
    print(f'Accruracy score: {pscore_train}')
    print("\n","Confusion Matrix")
    print(confusion_matrix(y_test, clf.predict(X_test)))


    print("\n","=== Decision Tree ===")
    # https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html
    clf = DecisionTreeClassifier().fit(X_train, y_train)

    pscore_train = accuracy_score(y_test, clf.predict(X_test))
    accurracy_list.append(pscore_train)
    print(f'Accruracy score: {pscore_train}')
    print("\n","Confusion Matrix")
    print(confusion_matrix(y_test, clf.predict(X_test)))


    #tester un SVM

    # changer avec sigmoid
    # plot decision Tree
    #plot_tree(clf)
    data_list.append(accurracy_list)

data = {
    'BTC':data_list[0],
    'ETH':data_list[1],
    'EOS':data_list[2]
}
# data = {
#     'BTC':data_list[0],
# }
df_result = pd.DataFrame(data)
df_result.index = ['LSTM','Conv1D_LSTM','Random Forest', 'Logistic Regression','Decision Tree']
print(df_result)
df_result.to_latex(str(path_latex)+f"/accuracy_result.tex")
