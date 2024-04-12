import streamlit as st
from . import utilis
import pandas as pd


def help():
    utilis.remove_space()

    with st.container(border=True):
        #mbti database
        mbti_data = pd.read_json("mbti_data.json")
        mbti_data.columns = ['MBTI Type', 'Description']
        st.title("Short note from Professor")
        st.table(mbti_data)

        #celebrities database
        data = pd.read_json("data.json").iloc[:, :1]
        data.columns = ['Name']

        st.title("Our robots")
        st.table(data)