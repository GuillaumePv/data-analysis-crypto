from pytrends.request import TrendReq
from pytrends import dailydata
from datetime import date
import pandas as pd
import numpy as np
from pathlib import Path

path_original = Path(__file__).resolve().parents[1]
path_data = (path_original / "../data/raw/").resolve()
path_data_processed = (path_original / "../data/processed/").resolve()

def addPytrend():
    cryptos = ['bitcoin', 'ethereum', 'eos']

    print("FETCHING TRENDS...")

    pytrends = TrendReq(hl='en-US', tz=360)
    for crypto in cryptos:
        dfTrend = dailydata.get_daily_data(crypto, 2014, 1, 2021, 5, verbose=False)
        dfTrend = dfTrend[[f'{crypto}_unscaled', f'{crypto}_monthly']]
        dfTrend.rename(columns = {f'{crypto}_unscaled':f'{crypto}_pytrend_unscaled', f'{crypto}_monthly':f'{crypto}_pytrend_monthly'}, inplace = True)
        dfTrend.to_csv(str(path_data) + f'/{crypto}_data_trend.csv')

if __name__ == '__main__':
    addPytrend()
