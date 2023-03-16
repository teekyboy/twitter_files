import streamlit as st
import pandas as pd

user_info = {
    "1 minute": {
        "avg": 0.05,
        "rank": 6
    },
    "1 hour": {
        "avg": 0.4,
        "rank": 7
    },
    "1 day": {
        "avg": 0.7,
        "rank": 5
    },
    "1 week": {
        "avg": 0.3,
        "rank": 4
    }
}

better_users = {
    "1 minute": {
        "user1": 0.45,
        "user2": 0.3,
        "user3": 0.1
    },
    "1 hour": {
        "user1": 0.45,
        "user2": 0.3,
        "user3": 0.1
    },
    "1 day": {
        "user1": 0.45,
        "user2": 0.3,
        "user3": 0.1
    },
    "1 week": {
        "user1": 0.45,
        "user2": 0.3
    }
}

# Set page configuration
st.set_page_config(layout="wide")

# Define the section title with center alignment
st.markdown("<h1 style='text-align: center;'>User Info</h1>", unsafe_allow_html=True)

# Create the user info DataFrame
df_user_info = pd.DataFrame(user_info).T
df_user_info.index.name = "Time"
df_user_info.columns = ["Average Profit", "Rank"]
df_user_info.index = df_user_info.index.str.capitalize() # Capitalize the time index

# Create the better users DataFrames
dfs_better_users = {}
for time, users in better_users.items():
    dfs_better_users[time] = pd.DataFrame.from_dict(users, orient="index", columns=["Profit"])
    dfs_better_users[time].index.name = "Twitter Handle"
    dfs_better_users[time].sort_values(by="Profit", ascending=False, inplace=True)
    dfs_better_users[time]["Rank"] = dfs_better_users[time]["Profit"].rank(ascending=False)

# Define the section titles with center alignment
col1_content = "<h3 style='text-align: center;'>Experts better at 1 Minute predictions</h3>"
col2_content = "<h3 style='text-align: center;'>Experts better at 1 Hour predictions</h3>"
col3_content = "<h3 style='text-align: center;'>Experts better at 1 Day predictions</h3>"
col4_content = "<h3 style='text-align: center;'>Experts better at 1 Week predictions</h3>"

# Create the columns using beta_columns function
col1, col2, col3, col4 = st.columns(4)

# Set the width of the columns
col1_width = 400
col2_width = 400
col3_width = 400
col4_width = 400

# Add the content to each column
with col1:
    st.markdown(col1_content, unsafe_allow_html=True)
    st.write(dfs_better_users["1 minute"].head(10))

with col2:
    st.markdown(col2_content, unsafe_allow_html=True)
    st.write(dfs_better_users["1 hour"].head(10))

with col3:
    st.markdown(col3_content, unsafe_allow_html=True)
    st.write(dfs_better_users["1 day"].head(10))

with col4:
    st.markdown(col4_content, unsafe_allow_html=True)
    st.write(dfs_better_users["1 week"].head(10))

# Display the user info DataFrame with center alignment
st.write(df_user_info.style.set_properties(**{'text-align': 'center', 'margin': 'auto'}).set_table_styles([{'selector': 'th', 'props': [('max-width', '50px')]}]).set_properties(**{'width': '250px', 'min-width': '150px', 'max-width': '500px'}))
