#utilities
import os
from pathlib import Path

#project modules
import fetchScripts.getCryptodata as cryptoRaw
import fetchScripts.twitterdata as twitterRaw
import fetchScripts.pytrendFetch as pytrendRaw

path_original = Path(__file__).resolve().parents[1]
path_data_origin = (path_original / "./data/").resolve()
path_data = (path_original / "./data/raw/").resolve()
path_data_processed = (path_original / "./data/processed/").resolve()

def fetchData():
    #creates data directory if it does not exists
    if not os.path.isdir(str(path_data_origin)):
        os.mkdir(str(path_data))
        os.mkdir(str(path_data))


    cryptoRaw.getRawCrypto()
    twitterRaw.getTweets()
    pytrendRaw.addPytrend()



if __name__ == '__main__':
    fetchData()
