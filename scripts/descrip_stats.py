from os import chdir, getcwd
from pathlib import Path
import pandas as pd

# A method which works well with python 3.4 +
path_original = Path(__file__).resolve().parents[1]
print(path_original)
path_data = (path_original / "./data/raw/").resolve()
path_data_processed = (path_original / "./data/processed/").resolve()
path_plot = (path_original / "./plots/").resolve()
#chdir(path_original)
#chdir(path_data)
print(getcwd())

df = pd.read_csv(str(path_data)+"/BTC_data_binance.csv")
print(df)
