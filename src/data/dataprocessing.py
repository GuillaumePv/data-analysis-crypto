#utilities
import os
import sys
from pathlib import Path
import json

#data science librairies
import numpy as np
import pandas as pd

'''
data_path = "../../data/raw/"
clean_data_path = "../../data/processed/"
eth_file = data_path+"ETH_raw.csv"
btc_file = data_path+"BTC_raw.csv"
eos_file = data_path+'EOS_raw.csv'

file_list = [eth_file,btc_file,eos_file]
list_ticker = ['ETH','BTC','EOS']

# faire une classe pour générer les données => folder 'data'
#create a function
def processPricedata(file,ticker):
    df = pd.read_csv(file)
    df['date'] = pd.to_datetime(df['Date'],unit="s")
    #df_btc.index = df_btc['Date']
    del df['Date']
    del df['Ignore']
    # del df_btc['CloseTime']
    df.to_csv(clean_data_path+ticker+'_Price_clean.csv')
    return df

list_df = []
for i in range(len(file_list)):
    list_df.append(processPricedata(file_list[i],list_ticker[i]))
'''

##############################
## Merge DB price & Twitter ##
##############################


list_ticker = ['ETH','BTC','EOS']

list_df = []
for i in range(len(list_ticker)):
    df = pd.read_csv(f"../../data/processed/{list_ticker[i]}_Price_clean.csv")
    df['date'] = pd.to_datetime(df['date'])
    list_df.append(df)


clean_data_path = "../../data/processed/"

## Path
tweetETH = "../../data/processed/ETH_clean.csv"
tweetBTC = "../../data/processed/BTC_clean.csv"
tweetEOS = "../../data/processed/EOS_clean.csv"

list_tweet = [tweetETH,tweetBTC,tweetEOS]
list_tweet_df = []

for tweet in list_tweet:
    df = pd.read_csv(tweet)
    df['date'] = pd.to_datetime(df['date'])
    list_tweet_df.append(df.iloc[:,1:].sort_values('date'))

for i in range(len(list_df)):
    df_outer = list_df[i].merge(list_tweet_df[i], on=['date'], how='left')
    df_outer.to_csv(clean_data_path+list_ticker[i]+'_finaldb.csv')
