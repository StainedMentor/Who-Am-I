import streamlit as st
import utilis

#page 2


st.set_page_config(page_title= "Settings",layout="wide")

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

