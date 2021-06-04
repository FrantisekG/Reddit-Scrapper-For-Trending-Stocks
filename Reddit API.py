#!/usr/bin/env python
# coding: utf-8

# # Script Objectives
# 1) Scrape posts that mention BTC
# 
# 2) Collect historical mentions from 1.1.2020 - 1.1.2021
# 
# 3) Save data into csv format into SQL database
# 
# 4) Apply NLP on or Linear regression to see results

# In[137]:


# Libraries

import praw
import os
import requests
import pandas as pd
import csv
from psaw import PushshiftAPI
from datetime import datetime

# Reddit API id establishment

reddit = praw.Reddit(
    client_id="U_X3AxlhV7UY1Q",
    client_secret="z34kRtWKiBfjQMUS4xBVLwWEYPS08A",
    password="Nightelf33",
    user_agent="testscript by u/Hunduk",
    username="Hunduk",)
#print(reddit.user.me())


# In[147]:


# Subreddit Cryptocurency

crypto_subreddit = reddit.subreddit("CryptoCurrency")
top_post = crypto_subreddit.search("BTC","Bitcoin",limit=100)
words = []

# Download post titles with BTC words

for word in top_post:
    words.append([word.title, word.selftext, word.created_utc])
    
words = pd.DataFrame(words, columns = ['Title', 'Text Body', 'Time Created'])
words['Time Created'] = pd.to_datetime(words['Time Created'],unit='s')
print(words[:5])
print(words[-5:])

# Save them into csv. or SQL

#words.to_csv("C:/Users/fgfra/OneDrive/Plocha/Sentiment_Data/Reddit_Posts/Reddit API.csv")


# In[ ]:




