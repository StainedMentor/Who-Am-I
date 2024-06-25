import streamlit as st
import utilis

def about():
    utilis.remove_space()

    with st.container(border=True):

        description, media = st.columns([1.5,0.13], gap="medium")
        with description:
            st.markdown(
                """
                <style>
                .centered-title {
                    text-align: center;
                }
                </style>
                """,
                unsafe_allow_html=True
            )
            st.markdown("<h1 class='centered-title'>Meet The Creators</h1>", unsafe_allow_html=True)

        with media: utilis.github()
    #with st.container(border=True):
    #    creat1,creat2,creat3,creat4 = st.columns([1, 1, 1, 1], gap="medium")
