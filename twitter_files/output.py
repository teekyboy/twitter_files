import pandas as pd
from os import path

def generate_out(df_merged):

    avg_1m = df_merged['1min_profit'].mean()
    avg_1h = df_merged['1hour_profit'].mean()
    avg_1d = df_merged['1day_profit'].mean()
    avg_1w = df_merged['1week_profit'].mean()

    dir_path = path.dirname(path.realpath(__file__))
    path_1m = path.join(dir_path, '..','raw_data','avg_profit_by_user_1min.csv')
    path_1h = path.join(dir_path, '..','raw_data','avg_profit_by_user_1hour.csv')
    path_1d = path.join(dir_path, '..','raw_data','avg_profit_by_user_1day.csv')
    path_1w = path.join(dir_path, '..','raw_data','avg_profit_by_user_1week.csv')

    df_rankings_1m = pd.read_csv(path_1m)
    df_rankings_1h = pd.read_csv(path_1h)
    df_rankings_1d = pd.read_csv(path_1d)
    df_rankings_1w = pd.read_csv(path_1w)

    user_rank_1m = (df_rankings_1m['1min_profit'] > avg_1m).sum() + 1
    user_rank_1h = (df_rankings_1h['1hour_profit'] > avg_1h).sum() + 1
    user_rank_1d = (df_rankings_1d['1day_profit'] > avg_1d).sum() + 1
    user_rank_1w = (df_rankings_1w['1week_profit'] > avg_1w).sum() + 1

    df_better_1m = df_rankings_1m.iloc[:user_rank_1m]
    df_better_1h = df_rankings_1h.iloc[:user_rank_1h]
    df_better_1d = df_rankings_1d.iloc[:user_rank_1d]
    df_better_1w = df_rankings_1w.iloc[:user_rank_1w]

    user_info = {

        "avg_1m" : avg_1m,
        "avg_1h" : avg_1h,
        "avg_1d" : avg_1d,
        "avg_1w" : avg_1w,
        "user_rank_1m" : user_rank_1m,
        "user_rank_1h" : user_rank_1h,
        "user_rank_1d" : user_rank_1d,
        "user_rank_1w" : user_rank_1w
    }

    for key,value in user_info.items():
        user_info[key] = float(value)

    better_users_1m = {}
    better_users_1h = {}
    better_users_1d = {}
    better_users_1w = {}

    for _, row in df_better_1m.iterrows():
        name = row['username']
        profit = row['1min_profit']
        better_users_1m[name] = float(profit)

    for _, row in df_better_1h.iterrows():
        name = row['username']
        profit = row['1hour_profit']
        better_users_1h[name] = float(profit)

    for _, row in df_better_1d.iterrows():
        name = row['username']
        profit = row['1day_profit']
        better_users_1d[name] = float(profit)

    for _, row in df_better_1w.iterrows():
        name = row['username']
        profit = row['1week_profit']
        better_users_1w[name] = float(profit)

    return user_info, better_users_1m, better_users_1h, better_users_1d, better_users_1w
