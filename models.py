#%%
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import sys
from data import Data
from NN_models import RNN

data = Data("BTC")
data.load_data()
#choose for our estimation
data.create_RNN_data(reg='return',LAG=10)
data.df

#%%
model=RNN()

model.create_model(data,architecture=[10],batch_normalization=True,activation="relu",drop_out=0.2)
model.train_model(data,verbose=0,epoch=10)
model.show_performance(label_='Error graph',data=data)
pred=model.model(data.X_te)


# plt.plot(pred.numpy().flatten(),color='k',label='Pred')
# plt.plot(data.y_te.flatten(),color='blue',linestyle='--',label='True')
# plt.legend()
# plt.show()



# %%

# %%
