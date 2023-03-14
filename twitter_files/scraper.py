import pandas as pd
import snscrape.modules.twitter as sntwitter

def user_scraper(username) -> pd.DataFrame:
    start_date = '2022-01-01'
    end_date = '2022-01-31'
    query = f'from:{username} since:{start_date} until:{end_date}'
    scraper = sntwitter.TwitterSearchScraper(query)
    tweets = []
    for i, tweet in enumerate(scraper.get_items()):
        data = [tweet.url, tweet.date, tweet.rawContent, tweet.user.username,
                tweet.cashtags]
        tweets.append(data)
    df = pd.DataFrame(tweets, columns= ['url', 'date', 'tweet', 'username', 'cashtags'])
    return df
