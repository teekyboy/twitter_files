import streamlit as st
import pandas as pd

CSS = """
.stApp {
    min-height: 100vh;
    color: #000;
    background-color: #fff;
  }
.stH {
    margin: 0;
    font-size: 96px;
    line-height: 1;
    font-weight: 300;
    letter-spacing: -1.5px;
  }
.stLi {
    display: inline-block;
    margin-right: 12px;
    font-size: 14px;
    line-height: 1.5;
    color: #ccc;
    border-top: 2px solid transparent;
  }
.stLiActive {
    color: #000;
    border-top: 2px solid #000;
  }
.stTable {
    font-size: 14px;
    line-height: 1.5;
    border-collapse: collapse;
    margin-top: 20px;
  }
.stTh {
    font-weight: 700;
    text-align: left;
    padding: 8px 16px;
    border: none;
    background-color: #ccc;
    color: #000;
    position: sticky;
    top: 0px;
  }
.stTd {
    text-align: left;
    padding: 8px 16px;
    border: none;
  }
"""
st.set_page_config(page_title="Apple CSS", page_icon=":iphone:", layout="wide", initial_sidebar_state="collapsed")
st.markdown(f'<style>{CSS}</style>', unsafe_allow_html=True)

# Create a dictionary of dictionaries
data = {
    "Tab 1": {
        "Name": ["Alice", "Bob", "Charlie"],
        "Age": [25, 30, 35]
    },
    "Tab 2": {
        "Name": ["David", "Emily", "Frank"],
        "Age": [40, 45, 50]
    }
}

# Create a sidebar with tabs for each dictionary
selected_tab = st.sidebar.selectbox("Select a tab", list(data.keys()))
df = pd.DataFrame(data[selected_tab])
st.write(df)
