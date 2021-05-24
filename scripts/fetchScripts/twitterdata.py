import twint
from pathlib import Path

path_original = Path(__file__).resolve().parents[1]
path_data = (path_original / "../data/raw/").resolve()
path_data_processed = (path_original / "../data/processed/").resolve()

def getTweets():

    #select keywords for each crypto we will train our model on
    names = []

    bitcoin = ["BTC", "Bitcoin", "bitcoin"]
    names.append(bitcoin)
    ethereum = ["ETH", "Ethereum", "ethereum"]
    names.append(ethereum)
    eos = ["EOS"]
    names.append(eos)

    #look for tweets for each crypto
    for i in names:
        print(f"FETCHING TWITTER DATA FOR {i[0]}...")
        name = i
        c = twint.Config()
        c.Search = name
        c.Custom["tweet"] = ["id", "created_at","username","tweet", "likes_count"]
        c.Verified = True
        c.Lang = "en"
        c.Min_replies = 1 # min replies
        c.Output = str(path_data) + f"/{name[0]}_data_tweet.json"
        c.Since = "2014-09-15"
        c.Store_json = True
        c.Hide_output = True

        tweets = twint.run.Search(c)
