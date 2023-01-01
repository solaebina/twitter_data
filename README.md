# Sentiment Analysis Using Python

## Table of Contents
This data analysis project consisted of three main tasks:
1. Scrape twitter data
2. Clean data
3. Sentimental analysis
4. Visualize data

## Why Did I Build This Project
Sentimental analysis of twitter is a way to understand what the general public is thinking about a certain topic. As someone that wants to go into marketing understanding the public is a critical tool which is why I decided to understake this project to learn how to perform sentimental analysis using python.

## Step 1: Scraping Twitter Data
To scrape twitter data, I chose to use snscrape. It is equipped with more customizability and no limit to the number of tweets it can scrape.

## Step 2: Cleaning Data
This is where I experienced the most roadblocks as well as learning curves. Reseraching and applying many data cleaning methods in order for a more accurate machine learning sentimental analysis in the next step. 

For the cleaning I performed these steps:
1. Pre-processing tweets: Which removes emojis, urls, @mentions, etc.
2. Removing stop words: clearing stop words to help the sentimental analysis step
3. Formatting: Removing some white space and symbols using regex. As well as lower casing all words.
4. Removing empty data
5. lemmatize and tokenize the tweets

## Step 3: Sentimental Analysis
Performed sentimental analysis using vader machine learning which has been proven to be the most accurate for tweets according to a couple reserach papers. The results were compiled onto the data set for further analysis and visualization.

## Step 4: Visualize data
To visualize the data I created several graphs that can be seen in the files to help viewers understand the data set.
