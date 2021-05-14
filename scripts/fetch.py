#utilities
import os

#project modules
import fetchScripts.getCryptodata as cryptoRaw
import fetchScripts.twitterdata as twitterRaw

#creates data directory if it does not exists
if not os.path.isdir('../data'):
    os.mkdir('../data')
    os.mkdir('../data/raw')


#cryptoRaw.getRawCrypto()
twitterRaw.getTweets()
