# Advanced data analysis

```bash
git clone https://github.com/GuillaumePv/data-analysis-crypto.git
```
2) installer les librairies nécessaires pour le projet

Python 2
```bash
pip install -r requirements.txt
```

Python 3
```bash
pip3 install -r requirements.txt
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



