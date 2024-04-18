import streamlit as st
import pandas

st.set_page_config(page_title="Portfolio", page_icon="📝")

col1, col2 = st.columns(2)

st.title("Featured Projects")

col3, empty_col, col4 = st.columns([1.5, 2.0, 1.5])

df = pandas.read_csv("backend/data/projects.csv", sep=";")
mid_ = int(len(df)/2)

with col3:
    for index, row in df[:mid_].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("backend/images/" + row["image"])
        st.write(f"[{row['title']}]({row['url']})")

with col4:
    for index, row in df[mid_:].iterrows():
        st.title(row["title"])
        st.write(row["description"])
        st.image("backend/images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")