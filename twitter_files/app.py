import streamlit as st

import numpy as np
import pandas as pd


user_info = {

    "avg_1m" : 0.05,
    "avg_1h" : 0.4,
    "avg_1d" : 0.7,
    "avg_1w" : 0.3,
    "user_rank_1m" : 6,
    "user_rank_1h" : 7,
    "user_rank_1d" : 5,
    "user_rank_1w" : 4
}
better_users_1m = {"user1": 0.45,
"user2": 0.3,
"user3": 0.1}

better_users_1h = {"user1": 0.45,
"user2": 0.3,
"user3": 0.1}

better_users_1d = {"user1": 0.45,
"user2": 0.3,
"user3": 0.1}

better_users_1w = {"user1": 0.45,
"user2": 0.3}

#Create the User DataFrame:
df = pd.DataFrame({
"Profit": [user_info["avg_1m"], user_info["avg_1h"], user_info["avg_1d"], user_info["avg_1w"]],
"Rank": [user_info["user_rank_1m"], user_info["user_rank_1h"], user_info["user_rank_1d"], user_info["user_rank_1w"]]
}, index=["1_minute", "1_hour", "1_day", "1_week"])

# Define the section title with center alignment
st.markdown("<h1 style='text-align: center;'>User Info</h1>", unsafe_allow_html=True)



# Define the section title with center alignment
st.markdown("<h1 style='text-align: center;'>User Info</h1>", unsafe_allow_html=True)


# Define the section title with center alignment
st.markdown("<h1 style='text-align: center;'>User Info</h1>", unsafe_allow_html=True)

# Display the DataFrame with center alignment
st.write(df.style.set_properties(**{'text-align': 'center', 'margin': 'auto'}))




#Display the DataFrame
st.dataframe(df)

#Create the DataFrames of the better users:
df_better_1m = pd.DataFrame(list(better_users_1m.items()), columns=["User Name", "Profit"], index=pd.RangeIndex(start=1, stop=len(better_users_1m)+1, name="Rank"))
df_better_1h = pd.DataFrame(list(better_users_1h.items()), columns=["User Name", "Profit"], index=pd.RangeIndex(start=1, stop=len(better_users_1h)+1, name="Rank"))
df_better_1d = pd.DataFrame(list(better_users_1d.items()), columns=["User Name", "Profit"], index=pd.RangeIndex(start=1, stop=len(better_users_1d)+1, name="Rank"))
df_better_1w = pd.DataFrame(list(better_users_1w.items()), columns=["User Name", "Profit"], index=pd.RangeIndex(start=1, stop=len(better_users_1w)+1, name="Rank"))

col1_content = "### Better 1 min users"
col2_content = "### Better 1 hour users"
col3_content = "### Better 1 day users"
col4_content = "### Better 1 week users"

#Create the columns using beta_columns function
col1, col2, col3, col4 = st.columns(4)

#Add the content to each column
col1.write(col1_content)
col1.dataframe(df_better_1m)

col2.write(col2_content)
col2.dataframe(df_better_1h)

col3.write(col3_content)
col3.dataframe(df_better_1d)

col4.write(col4_content)
col4.dataframe(df_better_1w)
