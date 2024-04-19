import streamlit as st
import pandas
from sidebar import sidebar
st.set_page_config(page_title="Portfolio", page_icon="📝", layout="wide")

sidebar()
st.header("Featured Projects")

col3, empty_col, col4 = st.columns([1.5, 1.0, 1.5])

df = pandas.read_csv("backend/data/projects.csv", sep=";")
mid_ = int(len(df)/2)


for idx in range(len(df)):
    row = df.iloc[idx]
    col = col4 if idx%2 else col3
    col.header(row["title"])
    col.markdown(row["description"])
    col.image("backend/images/" + row["image"])
    if row['url'].startswith("https://github.com"):
        col.write(f"[Source Code]({row['url']})")
    else:
        col.write(f"[{row['title']}]({row['url']})")
        

        
