import streamlit as st
import utilis, game, help, about

st.set_page_config(page_title="Who am I?", layout="wide", initial_sidebar_state="collapsed")
utilis.add_logo()
utilis.remove_space()

if 'username' not in st.session_state:
    st.session_state.username = ""

if 'window' not in st.session_state:
    st.session_state.window = ""

if "start" not in st.session_state:
    st.session_state.start = 0

if "text" not in st.session_state:
    st.session_state.text = 0

if "lvl" not in st.session_state:
    st.session_state.lvl = 1

if "research" not in st.session_state:
    st.session_state.research = False

if "level" not in st.session_state:
    st.session_state.level = 4

if "gamemode" not in st.session_state:
    st.session_state.gamemode = None

def start():

    with st.container(border=True,height=600):
        img, start_b, lvls_b = st.columns([1, 0.9, 1])

        #nie wiem czemu tak ma byc ale wtedy dziala znikanie po wcisnieciu start
        if st.session_state.start==0:
            st.session_state.start = 1
            if start_b.button("Start", type="secondary", use_container_width=True):pass


        elif st.session_state.start==1:
            st.write("Welcome to Who Am I?\n Tell me, what is your name?")

            username = st.text_input("Your name:",st.session_state.username)
            st.session_state.username = username

            if st.button("Meet Professor"):
                st.session_state.start = 2


        elif st.session_state.start==2:

            utilis.margin_top(40)
            img.image("assets/scientist.png", width=350)
            utilis.margin_top(30)


            messages = st.container(height=150, border=True)


            #introduction
            if st.session_state.text < 8:
                messages.write_stream(utilis.stream_data(st.session_state.text))

            #a little bit about mbti types
            elif st.session_state.text >= 8:
                messages.write_stream(utilis.stream_data2(st.session_state.text-8))

            # if not st.session_state.research:
            if st.session_state.text <24:
                st.session_state.text+=1

            if st.session_state.text == 6 and st.session_state.lvl == 0:
                st.session_state.text = 5

                #TUTAJ SA POZIOMY
                if lvls_b.button("Easy", type="secondary", use_container_width=True):
                    st.session_state.lvl = 1
                    st.session_state.text += 1
                    st.session_state.level = 4


                elif lvls_b.button("Medium", type="secondary", use_container_width=True):
                    st.session_state.lvl = 2
                    st.session_state.text += 1
                    st.session_state.level = 5


                elif lvls_b.button("Hard", type="secondary", use_container_width=True):
                    st.session_state.lvl = 3
                    st.session_state.text += 1
                    st.session_state.level = 6
                #TU KONIEC POZIOMOW


            if st.session_state.text >=24:
                st.session_state.text = 23
                messages.empty()

                if messages.button("Start classic research", type="secondary"):
                    st.session_state.window = "game"
                    st.rerun()
                if messages.button("Start streak game", type="secondary"):
                    st.session_state.window = "streak"
                    st.rerun()

            elif st.session_state.text <24:
                if messages.button("→", type="secondary") or st.session_state.lvl > 0:
                    messages.empty()




def manage():
    if st.session_state.window == "game":
        st.session_state.gamemode = 0
        game.game()
    elif st.session_state.window == "help" : help.help()
    elif st.session_state.window == "start": start()
    elif st.session_state.window == "about": about.about()
    elif st.session_state.window == "streak":
        st.session_state.gamemode = 1
        game.game()

with st.sidebar:
    utilis.margin_top(40)
    st.image("assets/scientist.png", use_column_width=True)
    utilis.margin_bottom(30)

    b0 = st.button("Classic Game", type="secondary", use_container_width=True)
    b5 = st.button("Streak challenge", type="secondary", use_container_width=True)
    b1 = st.button("Get help from Professor", type="secondary", use_container_width=True)
    b2 = st.button("Start again your research", type="secondary", use_container_width=True)
    b3 = st.button("Settings", type="secondary", use_container_width=True)
    b4 = st.button("About us", type="secondary", use_container_width=True)



if b0:
    st.session_state.window = "game"
elif b1:
    st.session_state.window = "help"
elif b2:
    st.session_state.window = "start"
elif b4:
    st.session_state.window = "about"
elif b5:
    st.session_state.window = "streak"
manage()
