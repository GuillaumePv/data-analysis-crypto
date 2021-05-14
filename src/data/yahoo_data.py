from yahoo_fin.stock_info import get_data
import pandas as pd


vix_daily = get_data("^VIX", start_date="17/08/2017", end_date="19/04/2021", interval="1d")
vix_daily.rename(columns = {'adjclose':'vix_close'}, inplace=True)
vix_daily = vix_daily['vix_close']

gvz_daily = get_data("^GVZ", start_date="17/08/2017", end_date="19/04/2021", interval="1d")
gvz_daily.rename(columns = {'adjclose':'gvz_close'}, inplace=True)
gvz_daily = gvz_daily['gvz_close']

yahoo_df = pd.concat((gvz_daily, vix_daily), axis=1)
yahoo_df['date'] = yahoo_df.index
yahoo_df['date'] = pd.to_datetime(yahoo_df['date'])


ticker_list = ['BTC', 'ETH', 'EOS']

for ticker in ticker_list:
    final_df = pd.read_csv(f'../../data/processed/{ticker}_finaldb_fct.csv')
    final_df['date'] = pd.to_datetime(final_df['date'])
    final = final_df.merge(yahoo_df, right_on='date', left_on='date')
    final = final.iloc[:, 3:]
    final = final.dropna()
    final.to_csv(f"../../data/processed/{ticker}_final_fct_yahoo.csv")
