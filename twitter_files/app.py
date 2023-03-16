import streamlit as st
import pandas as pd
import requests

# Set page configuration
st.set_page_config(layout="wide")

# Define the section title with center alignment
title_html = """
        <div style="display: flex; justify-content: center;">
            <h1>Twitter Know-it Alls?&#128269</h1>
        </div>
    """
st.write(title_html, unsafe_allow_html=True)

# Define the section title with center alignment
#st.markdown("<h1 style='text-align: center;'>Who are the experts? :mag_right:</h1>", unsafe_allow_html=True)

with st.form(key='params_for_api'):

    username = st.text_input("Enter a Twitter handle")
    st.form_submit_button('Make prediction')

twitter_api = f'https://api-3m5fgr32ua-ew.a.run.app/predict?username={username}'
response = requests.get(twitter_api)
output = response.json()

user_info = output['user_info']

# user_info = {
#     "avg_1m": -0.0004316488458779642,
#     "avg_1h": 0.0033923568857185324,
#     "avg_1d": 0.014273638684566983,
#     "avg_1w": 0.0222285934138953,
#     "user_rank_1m": 30,
#     "user_rank_1h": 1,
#     "user_rank_1d": 2,
#     "user_rank_1w": 3
# }

new_user_info = {
    'Time': ['1 minute', '1 hour', '1 day', '1 week'],
    'Average Profit': [user_info['avg_1m'], user_info['avg_1h'], user_info['avg_1d'], user_info['avg_1w']],
    'Rank': [user_info['user_rank_1m'], user_info['user_rank_1h'], user_info['user_rank_1d'], user_info['user_rank_1w']]
}

df = pd.DataFrame(new_user_info)
df.set_index('Time', inplace=True)
df['Average Profit'] = df['Average Profit'].apply(lambda x: '{:.2f}%'.format(round(x * 100, 2)))


st.markdown(f'<h3>Overview @{username}</h3>', unsafe_allow_html=True)
st.write(df.style.set_properties(**{'text-align': 'center', 'margin': 'auto'}).set_table_styles([{'selector': 'th', 'props': [('max-width', '50px')]}]).set_properties(**{'width': '250px', 'min-width': '150px', 'max-width': '500px'}))

better_users_1m = output['better_users_1m']

# better_users_1m = {
#     "zerohedge": 0.0015472426079598,
#     "mikealfred": 0.0009827125066278,
#     "gurgavin": 0.0009445239730543,
#     "charliebilello": 0.0006874936376666,
#     "hmeisler": 0.0006456358371876,
#     "PelosiTracker_": 0.0004425115724779,
#     "AdamMancini4": 0.000429178138209,
#     "LynAldenContact": 0.0003851618333977,
#     "Stocktwits": 0.0003779669201227,
#     "CryptoKaleo": 0.000344288287305,
#     "TommyThornton": 0.0003297516607421,
#     "CordovaTrades": 0.0002986342561035,
#     "GerberKawasaki": 0.0002476459116982,
#     "StockMKTNewz": 0.0002438723160656,
#     "SunriseTrader": 0.0001820404678723,
#     "alphatrends": 0.0001765618418572,
#     "canuck2usa": 0.0001649509424969,
#     "Jake__Wujastyk": 0.0001548143924334,
#     "paulg": 0.00005348929036820233,
#     "ShardiB2": 0.000014513797680336672,
#     "johnscharts": 0.000007796955163160362,
#     "traderstewie": -0.000016072965717946543,
#     "jimcramer": -0.00004258348949239255,
#     "FirstSquawk": -0.00005142649102128179,
#     "Schuldensuehner": -0.0001280009178682,
#     "unusual_whales": -0.0001969465603012,
#     "BowTiedBull": -0.000261994276254,
#     "OMillionaires": -0.0003036818480815,
#     "elonmusk": -0.0004316488458779,
#     "CheddarFlow": -0.000440592233176
# }

df1m = pd.DataFrame.from_dict(better_users_1m, orient='index', columns=['Profit'])
df1m['Twitter Handle'] = df1m.index
df1m.set_index('Twitter Handle', inplace=True)
df1m['Rank'] = df1m['Profit'].rank(ascending=False).round(0).astype(int)
df1m['Profit'] = (df1m['Profit'] * 100).round(3).astype(str) + '%'

better_users_1h = output['better_users_1h']
# better_users_1h = {
#     "elonmusk": 0.0033923568857185
# }

df1h = pd.DataFrame.from_dict(better_users_1h, orient='index', columns=['Profit'])
df1h['Twitter Handle'] = df1h.index
df1h.set_index('Twitter Handle', inplace=True)
df1h['Rank'] = df1h['Profit'].rank(ascending=False).round(0).astype(int)
df1h['Profit'] = (df1h['Profit'] * 100).round(3).astype(str) + '%'

better_users_1d = output['better_users_1d']
# better_users_1d = {
#     "canuck2usa": 0.0179002347280155,
#     "elonmusk": 0.0142736386845669
# }

df1d = pd.DataFrame.from_dict(better_users_1d, orient='index', columns=['Profit'])
df1d['Twitter Handle'] = df1d.index
df1d.set_index('Twitter Handle', inplace=True)
df1d['Rank'] = df1d['Profit'].rank(ascending=False).round(0).astype(int)
df1d['Profit'] = (df1d['Profit'] * 100).round(3).astype(str) + '%'

better_users_1w = output['better_users_1w']
# better_users_1w = {
#     "Fxhedgers": 0.0724858983793038,
#     "canuck2usa": 0.0401738043856678,
#     "elonmusk": 0.0222285934138953
# }

df1w = pd.DataFrame.from_dict(better_users_1w, orient='index', columns=['Profit'])
df1w['Twitter Handle'] = df1w.index
df1w.set_index('Twitter Handle', inplace=True)
df1w['Rank'] = df1w['Profit'].rank(ascending=False).round(0).astype(int)
df1w['Profit'] = (df1w['Profit'] * 100).round(3).astype(str) + '%'


# Define the section titles with center alignment
col1_content = "<h3 style='text-align: center;'>Experts better at 1 Minute predictions</h3>"
col2_content = "<h3 style='text-align: center;'>Experts better at 1 Hour predictions</h3>"
col3_content = "<h3 style='text-align: center;'>Experts better at 1 Day predictions</h3>"
col4_content = "<h3 style='text-align: center;'>Experts better at 1 Week predictions</h3>"

# Create the columns using beta_columns function
col1, col2, col3, col4 = st.columns(4)


# Add the content to each column
with col1:
    st.markdown(col1_content, unsafe_allow_html=True)
    st.write(df1m.style.set_properties(**{'text-align': 'center', 'margin': 'auto'}).set_table_styles([{'selector': 'th', 'props': [('max-width', '50px')]}]).set_properties(**{'width': '250px', 'min-width': '150px', 'max-width': '500px'}))

with col2:
    st.markdown(col2_content, unsafe_allow_html=True)
    st.write(df1h.style.set_properties(**{'text-align': 'center', 'margin': 'auto'}).set_table_styles([{'selector': 'th', 'props': [('max-width', '50px')]}]).set_properties(**{'width': '250px', 'min-width': '150px', 'max-width': '500px'}))

with col3:
    st.markdown(col3_content, unsafe_allow_html=True)
    st.write(df1d.style.set_properties(**{'text-align': 'center', 'margin': 'auto'}).set_table_styles([{'selector': 'th', 'props': [('max-width', '50px')]}]).set_properties(**{'width': '250px', 'min-width': '150px', 'max-width': '500px'}))

with col4:
    st.markdown(col4_content, unsafe_allow_html=True)
    st.write(df1w.style.set_properties(**{'text-align': 'center', 'margin': 'auto'}).set_table_styles([{'selector': 'th', 'props': [('max-width', '50px')]}]).set_properties(**{'width': '250px', 'min-width': '150px', 'max-width': '500px'}))
