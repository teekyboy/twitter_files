import pandas as pd
from os import path

def get_stocks() -> pd.DataFrame:
    dir_path = path.dirname(path.realpath(__file__))
    data_path = path.join(dir_path, '..','raw_data','combined_data.csv')
    df_stocks = pd.read_csv(data_path)
    df_stocks = df_stocks.rename(columns={'time': 'date'})
    df_stocks['date'] = pd.to_datetime(df_stocks['date'])
    df_stocks['date'] = df_stocks['date'].dt.strftime('%Y-%m-%d %H:%M')
    df_stocks = df_stocks.set_index(['date', 'symbol'])
    return df_stocks
