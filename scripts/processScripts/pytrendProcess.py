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

    print("BECOMING TRENDY...")

    dfTrend = dailydata.get_daily_data('bitcoin', 2014, 1, 2021, 5,verbose=False)
    print(dfTrend.head())

if __name__ == '__main__':
    addPytrend()
