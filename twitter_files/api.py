from scraper import user_scraper
from cleaner import merged_cleaner, user_cleaner
from sentiment import sentiment_analysis
from stock_prices import get_stocks

def predict(username):
    df_users = user_scraper(username)
    df_clean = user_cleaner(df_users)
    df_sentiment = sentiment_analysis(df_clean)
    df_stocks = get_stocks()
    df_merged = merged_cleaner(df_sentiment, df_stocks)
    return df_merged

if __name__ == '__main__':
    df = predict('livetradepro')
    print(df)
