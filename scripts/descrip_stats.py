## Libairies to manage paths
from os import chdir, getcwd
import os
from pathlib import Path

# Scientific librairies
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from scipy.stats import kurtosis, skew

from tqdm import tqdm
##à voir pour enlever
import sys
#sys.path.append("..")
from data import Data

# A method which works well with python 3.4 +
path_original = Path(__file__).resolve().parents[1]
#print(path_original)
path_data = (path_original / "./data/raw/").resolve()
path_data_processed = (path_original / "./data/processed/").resolve()

# add condition to see if there exist otherwise create a folder
path_plot = (path_original / "./plots/").resolve()
if(os.path.isdir(path_plot) == False):
    os.mkdir(path_plot)

path_latex = (path_original / "./latex/").resolve()
if(os.path.isdir(path_latex) == False):
    os.mkdir(path_latex)

## Loading data ##

for crypto_name in ['BTC','ETH','EOS']:
    data = Data(crypto_name)
    data.load_data(pump_thresold=0.01)
    #choose for our estimation
    data.create_RNN_data(reg='Return',LAG=10)

    data.df.corr()[['Close_ret_t+1','pump']].to_latex(str(path_latex)+f"/{crypto_name}_corr_return_pump.tex")

    ## create table for stat descriptive
    describe_data = data.df.copy()
    del describe_data['date']
    del describe_data['Date']
    describe_data = describe_data.dropna()
    desc = describe_data.describe()

    kur = pd.Series(kurtosis(desc),name='Kurtosis')
    sk = pd.Series(skew(desc),name='Skewness')
    kur.index, sk.index = desc.columns, desc.columns
    desc = desc.append(kur)
    desc = desc.append(sk)
    desc.to_latex(str(path_latex)+f"/{crypto_name}_stat_descrip.tex")

    for columns in tqdm(data.df.columns):
        if columns != "pump" and columns != 'date' and columns != 'Date':
            fig = plt.figure(figsize=(10,5))
            plt.scatter(data.df["pump"],data.df[columns])
            plt.xlabel("return t+1 > 5% (1: yes / 0: no)")
            plt.ylabel(columns)
            plt.grid(True)
            #plt.show()
            plt.savefig(str(path_plot)+f"/{crypto_name}_{columns}_corr_pump.png")

