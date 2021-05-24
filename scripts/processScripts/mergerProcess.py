#utilities
import os
import sys
from pathlib import Path
import json
from pathlib import Path

#data science librairies
import numpy as np
import pandas as pd

path_original = Path(__file__).resolve().parents[1]
path_data = (path_original / "../data/raw/").resolve()
path_data_processed = (path_original / "../data/processed/").resolve()

'''
data_path = "../data/raw/"
clean_data_path = "../data/processed/"
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

def mergeBinance():
    print("MERGING BINANCE AND TWEETS TOGETHER...")
    list_ticker = ['ETH','BTC','EOS']

    list_df = []
    for i in range(len(list_ticker)):
        df = pd.read_csv(str(path_data) + f"/{list_ticker[i]}_data.csv")
        list_df.append(df)


    clean_data_path = str(path_data_processed) + "/"

    ## Path
    tweetETH = str(path_data_processed) + "/ETH_tweet_clean.csv"
    tweetBTC = str(path_data_processed) + "/BTC_tweet_clean.csv"
    tweetEOS = str(path_data_processed) + "/EOS_tweet_clean.csv"

    list_tweet = [tweetETH,tweetBTC,tweetEOS]
    list_tweet_df = []

    for tweet in list_tweet:
        df = pd.read_csv(tweet)
        #df['date'] = pd.to_datetime(df['date'])
        list_tweet_df.append(df.sort_values('date'))

    for i in range(len(list_df)):
        df_outer = list_df[i].merge(list_tweet_df[i], on=['date'], how='left') #beug ici
        df_outer.to_csv(clean_data_path+list_ticker[i]+'_finaldb.csv', index=False)

    #Adding the pytrend data

    for crypto in [('bitcoin', 'BTC'), ('ethereum', 'ETH'), ('eos', 'EOS')]:
        dfTrend = pd.read_csv(str(path_data) + f'/{crypto[0]}_data_trend.csv')
        df = pd.read_csv(clean_data_path+crypto[1]+'_finaldb.csv')
        df = df.merge(dfTrend, on=['date'], how='right')
        df = df[df['Close'] > 0]
        df.to_csv(clean_data_path+crypto[1]+'_finaldb.csv', index=False)
