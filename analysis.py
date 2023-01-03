import numpy as np
import pandas as pd
import re
import matplotlib.pyplot as plt
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import matplotlib.pyplot as plt
from wordcloud import WordCloud, ImageColorGenerator
from PIL import Image
import matplotlib.image as mpimg

stopwords = set({'legend','apex','legends'})
analyser = SentimentIntensityAnalyzer()
tweet_data = pd.read_csv("tweet_data_cleaned.csv")
scores = []
compound_list = []
positive_list = []
negative_list = []
neutral_list = []
analyser.lexicon.pop('kill')

for i in range(tweet_data['Text'].shape[0]):
    compound = analyser.polarity_scores(tweet_data['Text'][i])["compound"]
    pos = analyser.polarity_scores(tweet_data['Text'][i])["pos"]
    neu = analyser.polarity_scores(tweet_data['Text'][i])["neu"]
    neg = analyser.polarity_scores(tweet_data['Text'][i])["neg"]

    scores.append({"Compound": compound,
                    "Positive": pos,
                    "Negative": neg,
                    "Neutral": neu
                  })
sentiments_score = pd.DataFrame.from_dict(scores)
tweet_data = tweet_data.join(sentiments_score)

#Creating new data frames for all sentiments (positive, negative and neutral)tw_list_negative = tw_list[tw_list[“sentiment”]==”negative”] 
listpositive = tweet_data[tweet_data['Compound'] > 0] 
listnegative = tweet_data[tweet_data['Compound'] < 0]
listneutral = tweet_data[tweet_data['Compound'] == 0] 

HTpositive = tweet_data['Hashtags'][tweet_data['Compound'] > 0] 
HTnegative = tweet_data['Hashtags'][tweet_data['Compound'] < 0]
HTnegative = tweet_data['Hashtags'][tweet_data['Compound'] == 0] 

print(tweet_data.head(1))
tweet_data.to_csv('tweet_sentiment.csv', index=False)
