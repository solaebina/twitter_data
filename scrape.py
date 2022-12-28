import snscrape.modules.twitter as sntwitter
import pandas as pd

#list to append the tweet data
tweets_list = []

#Using snsscrape to scrape data and append tweets
for i, tweet in enumerate(sntwitter.TwitterSearchScraper('spotify wrapped since:2022-11-30 until:2022-12-2').get_items()):
    if i>2500:
        break
    tweets_list.append([tweet.user.username, tweet.date, tweet.content])

#Creating a data frame from the tweets
tweet_df = pd.DataFrame(tweets_list, columns=['Username', 'Datetime', 'Text'])
tweet_df.to_csv('tweet_data_spotify.csv', index=False)