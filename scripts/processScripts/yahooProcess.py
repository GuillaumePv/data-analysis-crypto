from yahoo_fin.stock_info import get_data
from datetime import date
import pandas as pd
import numpy as np

def getData():
    dates = pd.date_range("17/08/2017", end=date.today(), freq='d')
    dates = pd.to_datetime(dates)

    print("GETTING VIX DATA...")
    vix_daily = get_data("^VIX", start_date="22/03/2012", interval="1d")
    vix_daily.rename(columns = {'adjclose':'vix_close'}, inplace=True)
    vix_daily['date'] = vix_daily.index.values
    vix_daily['date'] = pd.to_datetime(vix_daily['date'])
    for i in dates:
        if i not in vix_daily['date'].values:
            vix_daily = vix_daily.append(pd.Series(data={'date': i, 'vix_close':np.nan}), ignore_index=True)
    vix_daily = vix_daily.loc[:, ('date', 'close')]
    vix_daily.rename(columns = {'close':'vix'}, inplace = True)


    print("GETTING SOME GOLD...")
    gvz_daily = get_data("^GVZ", start_date="22/03/2012", interval="1d")
    gvz_daily.rename(columns = {'adjclose':'gvz_close'}, inplace=True)
    gvz_daily['date'] = gvz_daily.index.values
    gvz_daily['date'] = pd.to_datetime(gvz_daily['date'])
    for i in dates:
        if i not in gvz_daily['date'].values:
            gvz_daily = gvz_daily.append(pd.Series(data={'date': i, 'gvz_close':np.nan}), ignore_index=True)
    gvz_daily = gvz_daily.loc[:, ('date', 'close')]
    gvz_daily.rename(columns = {'close':'gvz'}, inplace = True)

    yahoo_df = vix_daily.merge(gvz_daily, right_on='date', left_on='date')
    yahoo_df['date'] = pd.to_datetime(yahoo_df['date'])
    yahoo_df.sort_values(by=['date'], inplace=True)
    yahoo_df = yahoo_df.fillna(method='ffill')



    ticker_list = ['BTC', 'ETH', 'EOS']

    for ticker in ticker_list:
        final_df = pd.read_csv(f'../data/processed/{ticker}_finaldb.csv')
        final_df['date'] = pd.to_datetime(final_df['date'])
        final = final_df.merge(yahoo_df, right_on='date', left_on='date')
        final = final.dropna()
        final.to_csv(f"../data/processed/{ticker}_finaldb.csv", index=False)
