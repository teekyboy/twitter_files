import numpy as np
import pandas as pd
import re
from twitter_files.symbol_list import symbol_list, ticker_list

def user_cleaner(df) -> pd.DataFrame:
    def user_renamer(df):
        df['symbol'] = ''
        return df

    def tweet_cleaner(tweet):
        tweet = re.sub(r'https?:\/\/\S+', ' ', tweet)
        tweet = re.sub(r'http?:\/\/\S+', ' ', tweet)
        tweet = re.sub(r'\n', ' ', tweet)
        tweet = re.sub(r'@[A-Za-z0-9]+', ' ', tweet)
        tweet = re.sub(r'#', ' ', tweet)
        tweet = re.sub(r'RT[\s]+', ' ', tweet)
        tweet = re.sub(r'\s\s+', ' ', tweet)
        tweet = re.sub(r'\b(lp|LP|inc|corp|co|ltd|llc|ETF|etf|Inc|Corp|Co|LLC|&amp|&)\b', ' ', tweet)
        return tweet

    def stock_patterns(symbol_list):
        stock_patterns = {
            key: re.compile("(" + "|".join(re.escape(value) for value in values) + ")")
                for key, values in symbol_list.items()
        }
        return stock_patterns

    def replace_stock_names(tweet):
        tweet_clean = tweet
        for key, pattern in stock_patterns.items():
            tweet_clean = re.sub(pattern, key, tweet_clean)
        return tweet_clean

    def get_stocks_mentioned(tweet):
        stocks_mentioned = []
        for key, pattern in stock_patterns.items():
            if re.search(key, tweet):
                stocks_mentioned.append(key)
        return stocks_mentioned

    def clean_cashtag(column):
        cleaned_column = []
        for value in column:
            if isinstance(value, float) and np.isnan(value):
                cleaned_column.append([])
            else:
                cleaned_value = str(value).strip('[]').replace(' ','').replace("'",'')
                cleaned_list = cleaned_value.split(',')
                cleaned_column.append(cleaned_list)
        return cleaned_column

    def stocks_list(df):
        df = df[df['symbol'].isin(ticker_list)]
        return df

    df = user_renamer(df)
    df['tweet'] = df['tweet'].apply(tweet_cleaner)
    stock_patterns = stock_patterns(symbol_list)
    df['tweet'] = df['tweet'].apply(lambda x: replace_stock_names(x))
    df['stocks_without_cashtag'] = df['tweet'].apply(lambda x: get_stocks_mentioned(x))
    df['cashtags'] = clean_cashtag(df['cashtags'])

    df['symbol'] = df.apply(lambda x: x['cashtags'][0] if len(x['cashtags']) > 0
                           else x['stocks_without_cashtag'][0]
                           if len(x['stocks_without_cashtag']) > 0 else np.nan, axis=1)
    df = df[df['symbol'].notnull()]
    df.drop(['cashtags', 'stocks_without_cashtag'], axis=1, inplace=True)
    df['symbol'] = df['symbol'].str.upper()
    df = stocks_list(df)

    return df

def merged_cleaner(df_tweets, df_stocks) -> pd.DataFrame:
    df_tweets['date'] = pd.to_datetime(df_tweets['date'], utc=True).dt.tz_convert('US/Eastern').dt.tz_localize(None)

    df_tweets['date'] = df_tweets['date'].dt.strftime('%Y-%m-%d %H:%M')

    df_tweets = df_tweets.set_index(['date', 'symbol'])
    start_time = '09:30'
    end_time = '16:00'
    date_index = pd.to_datetime(df_tweets.index.get_level_values('date'))
    time_index = date_index.strftime('%H:%M')
    mask = (time_index >= start_time) & (time_index <= end_time)
    df_tweets = df_tweets.loc[mask]

    df_merged = df_tweets.merge(df_stocks, left_index=True, right_index=True, how= 'left')
    df_merged = df_merged.sort_index(level=['symbol', 'date'])
    df_merged = df_merged.dropna()

    #for 1 minute
    df_merged['1min_profit'] = np.where(df_merged['sentiment'] == "Positive",
                                       (df_merged['1minute_after']-df_merged['open']) / df_merged['open'],
                                       (df_merged['open']-df_merged['1minute_after']) / df_merged['1minute_after'])
    #for 1 hour
    df_merged['1hour_profit'] = np.where(df_merged['sentiment'] == "Positive",
                                       (df_merged['1hour_after']-df_merged['open']) / df_merged['open'],
                                       (df_merged['open']-df_merged['1hour_after']) / df_merged['1hour_after'])

    #for 1 day
    df_merged['1day_profit'] = np.where(df_merged['sentiment'] == "Positive",
                                       (df_merged['1day_after']-df_merged['open']) / df_merged['open'],
                                       (df_merged['open']-df_merged['1day_after']) / df_merged['1day_after'])

    #for 1 week
    df_merged['1week_profit'] = np.where(df_merged['sentiment'] == "Positive",
                                       (df_merged['1week_after']-df_merged['open']) / df_merged['open'],
                                       (df_merged['open']-df_merged['1week_after']) / df_merged['1week_after'])

    return df_merged
