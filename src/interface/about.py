import streamlit as st
from . import utilis

def about():
    utilis.remove_space()

    with st.container(border=True):

        description, media = st.columns([1.5,0.13], gap="medium")

        description.title("Meet creators")
        description.write("bla bla bla")

        with media: utilis.github()