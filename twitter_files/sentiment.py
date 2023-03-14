import pandas as pd
import re
from transformers import AutoTokenizer, AutoModelForSequenceClassification
from sklearn.preprocessing import MinMaxScaler
from transformers import BertTokenizer, BertForSequenceClassification, pipeline
import torch

finbert = BertForSequenceClassification.from_pretrained('yiyanghkust/finbert-tone',num_labels=3)
tokenizer = BertTokenizer.from_pretrained('yiyanghkust/finbert-tone')
sentiment = pipeline("sentiment-analysis", model=finbert, tokenizer=tokenizer)

def sentiment_analysis(df) -> pd.DataFrame:
    df['sentiment'] = ''
    df['score'] = 0.0
    for idx, row in df.iterrows():
        tweet = row['tweet']
        result = sentiment(tweet)[0]
        df.at[idx, 'sentiment'] = result['label']
        df.at[idx, 'score'] = result['score']

    df = df[df.sentiment != 'Neutral']
    df.loc[df['sentiment'] == 'Negative', 'score'] *= -1
    df = df[['symbol', 'date', 'username', 'score','sentiment']]

    return df
