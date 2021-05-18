import numpy as np
import pandas as pd
from sklearn import datasets
import sklearn


class Data:
    def __init__(self,crypto_name):
        self.X_tr = None
        self.X_te = None
        self.X_va = None

        self.y_tr = None
        self.y_te = None
        self.y_va = None
        self.df = None
        self.crypto_name = crypto_name

    def load_data(self):
        try:
            self.df = pd.read_csv(f'./data/processed/{self.crypto_name}_finaldb_fct.csv').dropna()
        except FileNotFoundError:
            self.df = pd.read_csv(f'../data/processed/{self.crypto_name}_finaldb_fct.csv').dropna()
        self.df = self.df.iloc[:,1:]
        self.df['Close_std'] = (self.df['Close']-self.df['Close'].mean())/self.df['Close'].std()
        self.df['Close_ret'] = np.log(self.df[['Close']].shift(-1).values/self.df[['Close']].values)
    
    def create_RNN_data(self,LAG=10,reg="Price"):
        
        if reg == "Price":
            y=self.df[['Close_std']].values
        else:
            y= self.df[['Close_ret']].iloc[1:,:].values
        
        #print(y)
        X = []
        xx = self.df[["Volume","MA_100","coinmarketcap","justinsuntron","tweet_count"]]
        for i in range(LAG+1,0-1,-1):
            if i > 0:
                X.append(xx[LAG+1 - i:-i])
            else:
                X.append(xx[LAG+1 - i:])

        X = np.concatenate(X, 1)
        y = y[-X.shape[0]:,:]
        
        X = X.reshape((X.shape[0], X.shape[1], 1)) # add the input dimension !
       
        y = y[:-1,:]
        #==================
        ## Classification ##
        #==================
        #y = np.concatenate((np.where(y>0,1),np.where(y<=0,1)),axis=1)

        #standardize X
        X = X[:-1,:]
        ind = np.arange(0, y.shape[0], 1)
        tr = int(np.ceil(len(ind) * 0.8))
        te = int(np.ceil(len(ind) * 0.9))
        
        self.X_tr = X[np.where(ind[:tr])[0], :]
        self.X_te = X[np.where(ind[tr:te])[0], :]
        self.X_va = X[np.where(ind[te:])[0], :]

        self.y_tr = y[np.where(ind[:tr])[0], :]
        self.y_te = y[np.where(ind[tr:te])[0], :]
        self.y_va = y[np.where(ind[te:])[0], :]