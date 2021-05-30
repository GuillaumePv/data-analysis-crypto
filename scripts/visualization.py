## Libairies to manage paths
from os import chdir, getcwd
import os
from pathlib import Path

## Scienttific libraries ##
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import sys
from scipy.stats import kurtosis, skew


from data import Data
from NN_models import RNN


path_original = Path(__file__).resolve().parents[1]
#print(path_original)
path_data = (path_original / "./data/raw/").resolve()
path_data_processed = (path_original / "./data/processed/").resolve()

# add condition to see if there exist otherwise create a folder
path_plot = (path_original / "./plots/").resolve()
if(os.path.isdir(path_plot) == False):
    os.mkdir(path_plot)


data_btc = Data("BTC")
data_btc.load_data(pump_thresold=0.01)
data_btc.df.index = pd.to_datetime(data_btc.df['date'])

data_eth = Data("ETH")
data_eth.load_data(pump_thresold=0.01)
data_eth.df.index = pd.to_datetime(data_eth.df['date'])

data_eos = Data("EOS")
data_eos.load_data(pump_thresold=0.01)
data_eos.df.index = pd.to_datetime(data_eos.df['date'])


#===============
# Return Graphs 
#===============

plt.figure(figsize=(15,5))

plt.subplot(131)
return_btc = data_btc.df['Close_ret_t+1'].dropna().values
sns.distplot(return_btc,color='orange')
mean_return = return_btc.mean()
plt.title('Distribution of Returns t+1 in BTC')
plt.axvline(mean_return, ls=':', label='Index Mean: {}'.format(round(mean_return, 2)))
plt.legend()

plt.subplot(132)
return_eth = data_eth.df['Close_ret_t+1'].dropna().values
sns.distplot(return_eth,color='black')
mean_return = return_eth.mean()
plt.title('Distribution of Returns t+1 in ETH')
plt.axvline(mean_return, ls=':', label='Index Mean: {}'.format(round(mean_return, 2)))
plt.legend()

plt.subplot(133)
data_eos.df = data_eos.df.dropna()
return_eos = data_eos.df['Close_ret_t+1'].values
sns.distplot(return_eos,color='gray')
mean_return = return_eos.mean()
plt.title('Distribution of Returns t+1 in EOS')
plt.axvline(mean_return, ls=':', label='Index Mean: {}'.format(round(mean_return, 2)))
plt.legend()

plt.savefig(str(path_plot)+"/Returns_graph.png")


#========================
# Cumulative return graph
#========================

plt.figure(figsize=(15,5))

plt.subplot(131)
plt.plot((data_btc.df['Close_ret_t+1']+1).cumprod(),color="orange")
plt.grid(True)
plt.title("Cumulative return of BTC")
plt.tight_layout()

plt.subplot(132)
plt.plot(-(data_eth.df['Close_ret_t+1']+1).cumprod(),color="black")
plt.title("Cumulative return of ETH return")
plt.grid(True)
plt.tight_layout()

plt.subplot(133)
plt.plot((data_eos.df['Close_ret_t+1']+1).cumprod(),color="gray")
plt.title("Cumulative return of EOS return")
plt.grid(True)
plt.tight_layout()

plt.savefig(str(path_plot)+"/Cumulative_return_graph.png")