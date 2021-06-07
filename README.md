# Advanced data analysis

# Presentation of the project

## Abstract

The market of cryptocurrencies presents great investment opportunities accompanied by both high potential returns and high risks. It is a new market that is characterized by high volatility and complex factors affecting the path of crypto making the forecasting methods a real challenge for investors and financial analysts. In this paper, we combine the results from the five most used methods of classification in deep learning to highlight the most efficient one in predicting the sign of crypto return. The analysis is based on three cryptocurrencies: Bitcoin, the leader of the market, Ethereum, the second-placed cryptocurrency in respect to market capitalization, and Eos, in the top twenty. The last was taken to test the algorithm accuracy not only on the market giants. Furthermore, for each of the algorithms, we used the same database, Binance, which makes it possible to compare them and to conduct a general conclusion about the adding value of their complexity. In the study, the impact of external social factors such as most popular Twitter posts is considered in addition to the historical trading information about the crypto market. The results of the research show that the accuracy of crypto return predictions is estimated medium to low. In addition, we concluded that simple classification algorithms such as Random Forest could perform as efficiently as the complex algorithm Long Short-Term Memory (LSTM) taking into consideration 28 factors.

## Authors

* Ruben Kempter : ruben.kempter@unil.ch
* Dimitri André : dimitri.andre@unil.ch
* Guillaume Pavé : guillaume.pave@unil.ch

## Install libraries and run project

1) Clone project

```bash
git clone https://github.com/GuillaumePv/data-analysis-crypto.git
```
2) Install libraries

* Python 2
```bash
pip install -r requirements.txt
```

* Python 3
```bash
pip3 install -r requirements.txt
```

2) using our makefile to run our project

* see helper of the makefile
```bash
make
```
* run the whole project
```bash
make run
```

* run only model script
```bash
make models
```

# Project structure
https://github.com/hbast/pyTree

```
├── README.md          <- The top-level README for developers using this project.
│
├── Makefile           <- makefile to run project or each part of project
│
├── data
│   ├── processed      <- The final, canonical data sets for modeling.
│   └── raw            <- The original, immutable data dump.
│
│
│
├── models             <- Trained and serialized models, model predictions, or model summaries
│
├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
│                         the creator's initials, and a short `-` delimited description, e.g.
│                         `1.0-jqp-initial-data-exploration`.
│
│
├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
│                         generated with `pip freeze > requirements.txt`
│
├── scripts            <- Source code for use in this project.
│   │
│   ├── fetchScripts           <- Scripts to download or generate data
│   │   └── make_dataset.py
│   │
│   ├── processScripts       <- Scripts to turn raw data into features for modeling
│   │   └── build_features.py
│   │
│   ├── NN_models.py   <- Librairy to create and analyze LSTM and Conv1D_LSTM models
│   │
│   ├── data.py         <- Library to process our final dataset to provide features for our LSTM and Conv1D-LSTM
│   │
│   ├── models.py         <- Script to train models and then use trained models to make
│   │
│   ├── descript_stats.py         <- Script to create Decriptive statistics of our dataset
│   │
│   ├── getData.py         <- Script to create, merge and process our datasets
│   │
│   └── visualization.py  <- Script to create exploratory and results oriented visualizations
│
```
# TO-DO
- [x] obtain twitter data
- [x] data macro => S&P, VIX, GVZ (gold index CBOE) => Yahoo finance
- [x] make descriptive statistics
- [x] create makefile to run all project
- [x] do classification of model performance
- [x] corrext excel name
- [x] create a structure tree for the report



