import numpy as np
import preprocessor as p
import pandas as pd
from gensim.parsing.preprocessing import STOPWORDS
from gensim.parsing.preprocessing import remove_stopwords
import nltk
from nltk import word_tokenize, FreqDist
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import TweetTokenizer
from nltk.corpus import wordnet
nltk.download
nltk.download('wordnet')
lemmatizer = nltk.stem.WordNetLemmatizer()
w_tokenizer = TweetTokenizer()

#importing data from scrape and do some easy pre processing
tweet_data = pd.read_csv("tweet_data.csv")
tweet_data.drop_duplicates()

'''
preprocess
input: sentence (string)
output: takes out  (string)
'''
def preprocess_tweet(df):
    text = df['Text']
    text = p.clean(text)
    return text

'''
remove stop words
input: sentence (string)
output: sentence without stop words (string)
'''
def stop_words(df):
    text = df['Text']
    text = remove_stopwords(text)
    return text

'''
lemmatize
input: sentence (string)
output: lemmatized sentence (list)
'''
def lemmatize_text(df):
    return [(lemmatizer.lemmatize(w)) for w in (w_tokenizer.tokenize(df))]
    

'''
clean text
input: sentence (string)
output: cleaned sentence using regex (string)
'''
def clean_text(df):
    text = df
    text=text.str.lower()
    text = text.str.replace('[+-]?([0-9]*[.])?[0-9]+', ' ')
    text = text.str.replace("[^\w'#\s]",' ')
    text = text.str.replace('\s\s+', ' ')
    text.replace('', np.nan, inplace=True)
    return text

#clean tweet data   
tweet_data['Text'] = tweet_data.apply(preprocess_tweet, axis=1)
original_cleaned = tweet_data[["Text","Username"]]
tweet_data['Text'] = tweet_data.apply(stop_words, axis=1)
tweet_data['Text'] = clean_text(tweet_data["Text"])
tweet_data = tweet_data.dropna(subset=["Text"])
tweet_data = tweet_data.reset_index(drop=True)
data_unlemmatize = tweet_data[["Text","Username"]]
tweet_data['Text'] = tweet_data['Text'].apply(lemmatize_text)
tweet_data['Original'] = original_cleaned['Text']
tweet_data['Unlemmatize'] = data_unlemmatize['Text']
tweet_data.to_csv('tweet_data_cleaned.csv', index=False)