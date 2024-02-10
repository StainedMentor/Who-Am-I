import importlib
import streamlit as st
import utilis, game, help

st.set_page_config(page_title="Who am I?", layout="wide")
utilis.add_logo()

def start():
    with st.container(border=True):
        st.write("start")


with st.sidebar:
    utilis.margin_top(40)
    st.image("assets/scientist.png", use_column_width=True)
    utilis.margin_bottom(30)


    b0 = st.button("Game", type="secondary", use_container_width=True)
    b1 = st.button("Get help from Professor", type="secondary", use_container_width=True)
    b2 = st.button("Start again your research", type="secondary", use_container_width=True)
    b3 = st.button("Settings", type="secondary", use_container_width=True)

if b0:game.game()
elif b1:help.help()
elif b2:start()
elif b3: pass
else:start()

