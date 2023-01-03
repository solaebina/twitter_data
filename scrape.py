import snscrape.modules.twitter as sntwitter
import pandas as pd

#list to append the tweet data
tweets_list = []

#Using snsscrape to scrape data and append tweets
for i, tweet in enumerate(sntwitter.TwitterSearchScraper('apex legends since:2022-12-01 until:2022-12-30 lang:en').get_items()):
    if i>2500:
        break
    tweets_list.append([tweet.user.location,tweet.user.followersCount, tweet.hashtags, tweet.user.username, tweet.date, tweet.content])

#Creating a data frame from the tweets
tweet_df = pd.DataFrame(tweets_list, columns=['location','Followers','Hashtags','Username', 'Datetime', 'Text'])
tweet_df.to_csv('tweet_data.csv', index=False)