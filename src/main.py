from tsne_cpu import tsne_cpu
from visualise import visualise
import pandas as pd
from predict import predict
from tweets import get_tweets
import json
import os
import torch

if __name__ == "__main__":
    #tweet_df = pd.read_pickle('FarmLaws100.pkl')
    if not os.path.isfile('twitterAPIkeys.json'):
        raise FileNotFoundError('Please make sure a \'twitterAPIkeys.json\' exists in the src folder!')
    
    with open('twitterAPIkeys.json') as f:
        APIkeys_dict = json.load(f)
    
    search_term = "iphone11"
    no_of_tweets = 500
    tweet_df = get_tweets(search_term, no_of_tweets, APIkeys_dict, retweets=False)
    print(tweet_df.head())
    inputs = list(tweet_df['tweet_text'].values)
    outputs = predict(inputs)
    outputs_2d = tsne_cpu(outputs)
    # print(outputs_2d)
    tweet_df['x_coord'] = outputs_2d[:,0]
    tweet_df['y_coord'] = outputs_2d[:,1]
    visualise(tweet_df)