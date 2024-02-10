import streamlit as st
import utilis
import pandas as pd

st.set_page_config(page_title= "Help",layout="wide")
utilis.add_logo()

with st.sidebar:

    utilis.margin_top(40)
    st.image("assets/scientist.png", use_column_width=True)
    utilis.margin_bottom(30)

    if st.button("Get help from Professor", type="secondary", use_container_width=True):
        pass
    if st.button("Start again your research", type="secondary", use_container_width=True):
        pass

    if st.button("Settings", type="secondary", use_container_width=True):
        pass

utilis.remove_space()
with st.container(border=True):
    #mbti database
    mbti_data = pd.read_json("mbti_data.json")
    mbti_data = pd.DataFrame(mbti_data)
    mbti_data.columns = ['MBTI Type', 'Description']
    st.title("Short note from Professor")
    st.table(mbti_data)

    #celebritis database
    data = pd.read_json("data.json")
    data = pd.DataFrame(data)
    data.columns = ['Name', 'MBTI Type']

    st.title("Our robots")
    st.table(data)