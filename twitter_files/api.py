from scraper import user_scraper
from cleaner import merged_cleaner, user_cleaner
from sentiment import sentiment_analysis
from stock_prices import get_stocks
from output import generate_out
from if_error import random_user

def predict(username: str = 'elonmusk'):
    #df_users = user_scraper(username)
    #df_clean = user_cleaner(df_users)
    #df_sentiment = sentiment_analysis(df_clean)
    df_error = random_user(username)
    df_stocks = get_stocks()
    df_merged = merged_cleaner(df_error, df_stocks)
    user_info, better_users_1m, better_users_1h, better_users_1d, better_users_1w = generate_out(df_merged)
    return user_info, better_users_1m, better_users_1h, better_users_1d, better_users_1w

if __name__ == '__main__':
    out = predict('elonmusk')
    print(out)
