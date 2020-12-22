import tweepy as tw
import json
import re
import pandas as pd
from datetime import datetime,date

def preprocess_tweet(tweet):
    tweet = re.sub(r"http\S+", "", tweet)
    tweet = re.sub(r"\s+"," ",tweet)
    tweet = re.sub(r"@\w+", "", tweet)
    tweet = tweet.strip()
    return tweet

def get_tweets(search_term, no_of_tweets, APIkeys_dict, retweets=True):
    if no_of_tweets > 1000:
        raise ValueError('The no of tweets cannot exceed 1000.')
    if retweets == False:
        search_term += '-filter:retweets'
    try:
        consumer_key = APIkeys_dict['API key']
        consumer_secret = APIkeys_dict['API secret key']
        access_token = APIkeys_dict['Access token']
        access_token_secret = APIkeys_dict['Access token secret']
    except KeyError as e:
        print('The following key not found in APIkeys_dict :', e.args[0])
    
    auth = tw.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tw.API(auth, wait_on_rate_limit=True)
    
    tweets = tw.Cursor(api.search,
              q=search_term,
              lang="en",
              tweet_mode='extended').items(no_of_tweets)
    
    tweet_df = pd.DataFrame(columns = ['tweet_id',
                                       'tweet_text',
                                       'tweet_retweeted',
                                       'tweet_retweet_count',
                                       'tweet_favorite_count',
                                       'tweet_hashtags',
                                       'tweet_user_mentions',
                                       'user_id',
                                       'user_follower_count',
                                       'user_age_days',
                                       'user_tweet_count'])
    for tweet in tweets:
        hashtags = [h['text'] for h in tweet.entities['hashtags']]
        user_mentions = [h['name'] for h in tweet.entities['user_mentions']]
        tweet_df = tweet_df.append({'tweet_id':tweet.id_str,
                                    'tweet_text':preprocess_tweet(tweet.full_text),
                                    'tweet_retweeted':tweet.retweeted,
                                    'tweet_retweet_count':tweet.retweet_count,
                                    'tweet_favorite_count':tweet.favorite_count,
                                    'tweet_hashtags':hashtags,
                                    'tweet_user_mentions':user_mentions,
                                    'user_id':tweet.user.id_str,
                                    'user_follower_count':tweet.user.followers_count,
                                    'user_age_days':(datetime.today()-tweet.user.created_at).days,
                                    'user_tweet_count':tweet.user.statuses_count},
                                    ignore_index=True)
    
    return tweet_df
    