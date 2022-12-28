import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import time
import re
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from better_profanity import profanity

#importing data from scrape
tweet_data = pd.read_csv("tweet_data_spotify.csv")

tweet_data.drop_duplicates(inplace = True)

def clean_tweet(tweet):
    r = tweet.lower()
    r = profanity.censor(r)
    r = re.sub("'", "", r) # This is to avoid removing contractions in english
    r = re.sub("@[A-Za-z0-9_]+","", r)
    r = re.sub("#[A-Za-z0-9_]+","", r)
    r = re.sub(r'http\S+', '', r)
    r = re.sub('[()!?]', ' ', r)
    r = re.sub('\[.*?\]',' ', r)
    r = re.sub("[^a-z0-9]"," ", r)
    r = r.split()
    stopwords = ["for", "on", "an", "a", "of", "and", "in", "the", "to", "from"]
    r = [w for w in r if not w in stopwords]
    r = " ".join(word for word in r)
    return r

cleaned = [clean_tweet(tw) for tw in tweet_data]