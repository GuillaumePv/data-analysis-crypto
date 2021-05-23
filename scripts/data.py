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

    def load_data(self,pump_thresold):
        try:
            self.df = pd.read_csv(f'./data/processed/{self.crypto_name}_finaldb.csv').dropna()
        except FileNotFoundError:
            self.df = pd.read_csv(f'../data/processed/{self.crypto_name}_finaldb.csv').dropna()
        #self.df = self.df.iloc[:,1:]
        self.df['abs_diff_close_open'] = np.abs(self.df['Close'] - self.df['Open'])
        self.df['Close_std'] = (self.df['Close']-self.df['Close'].mean())/self.df['Close'].std()
        self.df['Close_ret_t+1'] = np.log(self.df[['Close']].shift(-1).values/self.df[['Close']].values)
        self.df['pump_5'] = np.where(self.df['Close_ret_t+1'] > pump_thresold,1,0)

    def create_RNN_data(self,LAG=10,reg="Price",columns=["Volume","tweet_count","vix"],pump_thresold=0.05):
        
        # condtion to choose a thresold
        assert pump_thresold <= 0.10, "choose a thresold less than 10%"

        assert reg in ['Price','Return'], "No model is available for reg"

        if reg == "Price":
            y=self.df[['Close_std']].values
        else:
            y= self.df[['Close_ret_t+1']].iloc[1:,:].values
        
        #print(y)
        X = []
        xx = self.df[columns]
        for i in range(LAG+1,0-1,-1):
            if i > 0:
                X.append(xx[LAG+1 - i:-i])
            else:
                X.append(xx[LAG+1 - i:])

        X = np.concatenate(X, 1)
        y = y[-X.shape[0]:,:]
        
        X = X.reshape((X.shape[0], X.shape[1], 1)) # add the input dimension !
       
        y = y[:-1,:]

        #======================
        # LSTM classification #
        #======================
        y = np.concatenate((np.where(y>pump_thresold,1,0),np.where(y<=pump_thresold,1,0)),axis=1)

        #standardize X
        X = X[:-1,:]
        ind = np.arange(0, y.shape[0], 1)
        tr = int(np.ceil(len(ind) * 0.7))
        te = int(np.ceil(len(ind) * 0.9))
        
        self.X_tr = X[np.where(ind[:tr])[0], :]
        self.X_te = X[np.where(ind[tr:te])[0], :]
        self.X_va = X[np.where(ind[te:])[0], :]

        self.y_tr = y[np.where(ind[:tr])[0], :]
        self.y_te = y[np.where(ind[tr:te])[0], :]
        self.y_va = y[np.where(ind[te:])[0], :]

if __name__ == "__main__":
    data = Data("BTC")
    data.load_data()
    #choose for our estimation
    data.create_RNN_data(reg='return',LAG=10)