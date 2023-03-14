from fastapi import FastAPI
#from twitter_files.scraper import user_scraper
from twitter_files.cleaner import merged_cleaner
#from twitter_files.sentiment import sentiment_analysis
from twitter_files.stock_prices import get_stocks
from twitter_files.if_error import random_user
from twitter_files.output import generate_out

app = FastAPI()

#define a root '/' endpoint
@app.get("/")
def read_root():
    return {'ok' : True}

@app.get("/predict")
def predict(username: str):
    # df_users = user_scraper(username)
    # df_clean = user_cleaner(df_users)
    # df_sentiment = sentiment_analysis(df_clean)
    df_error = random_user(username)
    df_stocks = get_stocks()
    df_merged = merged_cleaner(df_error, df_stocks)
    user_info, better_users_1m, better_users_1h, better_users_1d, better_users_1w = generate_out(df_merged)
    final_dict = {
        "user_info" : user_info,
        "better_users_1m" : better_users_1m,
        "better_users_1h" : better_users_1h,
        "better_users_1d" : better_users_1d,
        "better_users_1w" : better_users_1w
    }
    return final_dict
