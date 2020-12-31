from tsne_cpu import tsne_cpu
from visualise import visualise
import pandas as pd
from predict import predict
from tweets import get_tweets
import json
import os
import torch
import argparse

if __name__ == "__main__":
    my_parser = argparse.ArgumentParser()
    my_parser.version = '1.0'
    my_parser.add_argument("search_term", help="The search to be used in order to retrieve tweets")
    my_parser.add_argument('-n','--num_tweets', action='store',type=int,default=500,help='No of tweets to be retrieved, must be less than 1000')
    args = my_parser.parse_args()
    search_term = args.search_term
    no_of_tweets = args.num_tweets
    
    if not os.path.isfile('twitterAPIkeys.json'):
        raise FileNotFoundError('Please make sure a \'twitterAPIkeys.json\' exists in the src folder!')
    
    with open('twitterAPIkeys.json') as f:
        APIkeys_dict = json.load(f)
    
    
    tweet_df = get_tweets(search_term, no_of_tweets, APIkeys_dict, retweets=False)
    inputs = list(tweet_df['tweet_text'].values)
    outputs = predict(inputs)
    outputs_2d = tsne_cpu(outputs)
    # print(outputs_2d)
    tweet_df['x_coord'] = outputs_2d[:,0]
    tweet_df['y_coord'] = outputs_2d[:,1]
    visualise(tweet_df)