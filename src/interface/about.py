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

    with st.container(border=True):
        creat1, creat2, creat3, creat4 = st.columns([1, 1, 1, 1], gap="medium")

        with creat1:
            st.markdown('<h2 class="centered-title">StainedMentor</h2>', unsafe_allow_html=True)
            utilis.avatar("oliver_cyber")

        with creat2:
            st.markdown('<h2 class="centered-title">Agkittens</h2>', unsafe_allow_html=True)
            utilis.avatar("aga_cyber")

        with creat3:
            st.markdown('<h2 class="centered-title">Marlon1385</h2>', unsafe_allow_html=True)
            utilis.avatar("milosz_cyber")
            st.markdown(
                '<div class="justify">A hundred percent ISTP. Capable, but lazy. Responsible for connecting the database with the application, handling users, and the scoreboard. Created the Streak Challenge game mode.</div>',
                unsafe_allow_html=True)

        with creat4:
            st.markdown('<h2 class="centered-title">SamePinchy</h2>', unsafe_allow_html=True)
            utilis.avatar("kuba_cyber")
    #with st.container(border=True):
    #    creat1,creat2,creat3,creat4 = st.columns([1, 1, 1, 1], gap="medium")
