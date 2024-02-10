import streamlit as st

def add_logo():
    st.markdown(
        """
        <style>
            [data-testid="stSidebar"] {
                background-image: url(https://github.com/StainedMentor/Who-Am-I/blob/main/assets/title.png?raw=true);
                background-repeat: no-repeat;
                background-size: contain;
                }

        </style>
        """,
        unsafe_allow_html=True,
    )

def remove_space():
    st.markdown("""
            <style>
                   .block-container {
                        padding-top: 1rem;
                        padding-bottom: 2rem;
                        padding-left: 5rem;
                        padding-right: 5rem;
                    }
            </style>
            """, unsafe_allow_html=True)


def margin_top(px):
    st.markdown(f'<div style="margin-top: {px}px;</div>',unsafe_allow_html=True)

def margin_bottom(px):
    st.write(f'<div style="margin-bottom: {px}px;</div>',unsafe_allow_html=True)

