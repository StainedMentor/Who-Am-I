import streamlit as st
import utilis, game, help

st.set_page_config(page_title="Who am I?", layout="wide", initial_sidebar_state="collapsed")
utilis.add_logo()
utilis.remove_space()

if 'game' not in st.session_state:
    st.session_state.game = False

def start():
    @st.cache_data
    def text_num(idx=0):
        return idx

    idx = text_num()

    with st.container(border=True,height=600):

        if st.button("→", type="secondary"):
            st.image("assets/scientist.png", width=350)
            messages = st.container(height=140, border=True)
            messages.write_stream(utilis.stream_data(idx))
            idx = text_num(idx+1)
            # if st.button("→", type="secondary"):
            #     idx +=1
            #     messages.write_stream(utilis.stream_data(idx))

with st.sidebar:
    utilis.margin_top(40)
    st.image("assets/scientist.png", use_column_width=True)
    utilis.margin_bottom(30)

    b0 = st.button("Game", type="secondary", use_container_width=True)
    b1 = st.button("Get help from Professor", type="secondary", use_container_width=True)
    b2 = st.button("Start again your research", type="secondary", use_container_width=True)
    b3 = st.button("Settings", type="secondary", use_container_width=True)

if b0 or st.session_state.game:game.game()
elif b1:help.help()
elif b2:start()
elif b3: pass
else:start()

