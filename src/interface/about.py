import streamlit as st
from . import utilis

def about():

    with st.container(border=True):

        description, media = st.columns([1.5,0.13], gap="medium")
        with description:

            st.markdown("""
                <h1 style="text-align:center">Meet the creators</h1>
                """, unsafe_allow_html=True)
        with media: utilis.github()
    #with st.container(border=True):
    #    creat1,creat2,creat3,creat4 = st.columns([1, 1, 1, 1], gap="medium")
