import streamlit as st
import utilis
import pandas as pd


def help():
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