#utilities
import os

#project modules
import fetchScripts.getCryptodata as cryptoRaw
import fetchScripts.twitterdata as twitterRaw

def fetchData():
    #creates data directory if it does not exists
    if not os.path.isdir('../data'):
        os.mkdir('../data')
        os.mkdir('../data/raw')


    #cryptoRaw.getRawCrypto()
    twitterRaw.getTweets()



if __name__ == '__main__':
    fetchData()
