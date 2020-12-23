from tsne_cpu import tsne_cpu
from visualise import visualise
import pandas as pd
from predict import predict

if __name__ == "__main__":
    tweet_df = pd.read_pickle('FarmLaws100.pkl')
    inputs = list(tweet_df['tweet_text'].values)
    outputs = predict(inputs)
    outputs_2d = tsne_cpu(outputs)
    # print(outputs_2d)
    tweet_df['x_coord'] = outputs_2d[:,0]
    tweet_df['y_coord'] = outputs_2d[:,1]
    visualise(tweet_df)