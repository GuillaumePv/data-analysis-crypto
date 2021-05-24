# -> How to comment a block?

# Command + K + C


# -> How to uncomment a block?

# Command + K + U


from config import api_key, api_secret
from binance.client import Client
import csv
from pandas_datareader import data
import pandas as pd
import datetime as dt
from pathlib import Path

path_original = Path(__file__).resolve().parents[1]
path_data = (path_original / "../data/raw/").resolve()
path_data_processed = (path_original / "../data/processed/").resolve()

## Binance API
def obtain_cryptodata(Cryptoname):
    client = Client(api_key, api_secret)
    print(f"FETCHING BINANCE DATA FOR {Cryptoname}...")
    start_date = "1 Dec, 2012"
    csvfile = open(str(path_data) + f'/{Cryptoname}_data_binance.csv', 'w',newline='')
    candlestick_writer= csv.writer(csvfile, delimiter=',')

    # appel de Binance API pour avoir les données
    # 1er arg: pair de crypto => pour le moment c'est crypto /USDT
    candlesticks = client.get_historical_klines(f"{Cryptoname}USDT", Client.KLINE_INTERVAL_1DAY, start_date)
    candlestick_writer.writerow(['Date','Open','High','Low','Close','Volume','CloseTime','QuoteAssetVolume','NumberofTrade','TakerbuybaseV','TakerbuyquoteV','Ignore'])
    for i in range(len(candlesticks)):
        candlesticks[i][0] = candlesticks[i][0]/1000
        candlestick_writer.writerow(candlesticks[i])
        #print("===================================")
        #print(f'process value {i+1}/{len(candlesticks)}')

    csvfile.close()


def obtainCrypto_yahoofinance(Cryptoname):
    start_date = '2012-03-22' #@param {type:"date"}
    #@title Date fields
    end_date = str(dt.datetime.now().date())
    #end_date = '2020-12-31'
    df = data.DataReader(f"{Cryptoname}-USD",
                       start=start_date,
                       end=end_date,
                       data_source='yahoo')
    df['date'] = df.index
    df.to_csv(str(path_data) + f'/{Cryptoname}_data.csv')

def getRawCrypto():
    print("GETTING CRYPTO RAW DATA")

    ticker_list=['BTC', 'ETH', 'EOS']

    for ticker in ticker_list:
        obtainCrypto_yahoofinance(ticker)


'''
if __name__ == '__main__':
    name = str(input("Which crypto: ")) #Ticker de la crypto
    obtain_cryptodata(name)
'''
