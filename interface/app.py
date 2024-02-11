import streamlit as st
import utilis, game, help

st.set_page_config(page_title="Who am I?", layout="wide", initial_sidebar_state="collapsed")
utilis.add_logo()
utilis.remove_space()


if 'window' not in st.session_state:
    st.session_state.window = ""

if "start" not in st.session_state:
    st.session_state.start = False

if "text" not in st.session_state:
    st.session_state.text = 4



def start():
    with st.container(border=True,height=600):
        img, start_b, lvls_b = st.columns([1, 0.9, 1])

        #nie wiem czemu tak ma byc ale wtedy dziala
        if not st.session_state.start:
            st.session_state.start = True
            if start_b.button("Start", type="secondary", use_container_width=True):
                pass

        elif st.session_state.start:
            utilis.margin_top(40)
            img.image("assets/scientist.png", width=350)
            utilis.margin_top(30)
            messages = st.container(height=150, border=True)
            messages.write_stream(utilis.stream_data(st.session_state.text))
            st.session_state.text += 1

            if st.session_state.text > 5:
                if lvls_b.button("Easy", type="secondary", use_container_width=True):
                    pass
                elif lvls_b.button("Medium", type="secondary", use_container_width=True):
                    pass
                elif lvls_b.button("Hard", type="secondary", use_container_width=True):
                    pass

            if messages.button("→", type="secondary"):
                messages.empty()






def manage():
    if st.session_state.window == "game": game.game()
    elif st.session_state.window == "help": help.help()
    elif st.session_state.window == "start": start()

with st.sidebar:
    utilis.margin_top(40)
    st.image("assets/scientist.png", use_column_width=True)
    utilis.margin_bottom(30)

    b0 = st.button("Game", type="secondary", use_container_width=True)
    b1 = st.button("Get help from Professor", type="secondary", use_container_width=True)
    b2 = st.button("Start again your research", type="secondary", use_container_width=True)
    b3 = st.button("Settings", type="secondary", use_container_width=True)

if b0:
    st.session_state.window = "game"
elif b1:
    st.session_state.window = "help"
elif b2:
    st.session_state.window = "start"

manage()

