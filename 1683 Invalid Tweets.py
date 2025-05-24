import pandas as pd

def invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:
    # tweets['count'] = tweets['content'].apply(lambda s: sum(c.isalnum() or c in ['!', ' '] for c in s))
    # return tweets[tweets['count']>15][['tweet_id']]
    filter = tweets[tweets['content'].str.len() > 15]
    return filter[['tweet_id']]
    
    