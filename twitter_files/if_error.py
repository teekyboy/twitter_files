import pandas as pd
from os import path

def random_user(username) -> pd.DataFrame:
    dir_path = path.dirname(path.realpath(__file__))
    data_path = path.join(dir_path, '..','raw_data','twitter_complete.csv')
    df = pd.read_csv(data_path)
    df = df[df['username'] == username]
    df.rename(columns={'stock':'symbol'}, inplace=True)
    df.loc[df['sentiment'] == 'Negative', 'score'] *= -1
    df = df[['symbol', 'date', 'username', 'score','sentiment']]

    return df
