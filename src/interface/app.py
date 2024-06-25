import streamlit as st
from . import utilis, game, help, about, streak
import pandas as pd
import firebase_admin
from firebase_admin import db, credentials

def main():
    st.set_page_config(page_title="Who am I?", layout="wide", initial_sidebar_state="collapsed")

    utilis.add_logo()
    # utilis.remove_space()
    utilis.background()

    utilis.container_bg()
    # utilis.custom_c()
    # Session state data initialized on app start

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

    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False

    if 'data' not in st.session_state:
        st.session_state.data = pd.DataFrame({'username': [], 'score': []})

    if 'data_streak' not in st.session_state:
        st.session_state.data_streak = pd.DataFrame({'username': [], 'score': []})

    if 'score' not in st.session_state:
        st.session_state.score = 0

    if 'streak_classic' not in st.session_state:
        st.session_state.streak_classic = 0

    if 'curr_lvl' not in st.session_state:
        st.session_state.curr_lvl = 1

    if 'hints_classic' not in st.session_state:
        st.session_state.hints_classic = 3

    if 'hints_streak' not in st.session_state:
        st.session_state.hints_streak = 3

    if 'score2' not in st.session_state:
        st.session_state.score2 = 0

    if 'streak_streak' not in st.session_state:
        st.session_state.streak_streak = 0

    if 'current_lvl' not in st.session_state:
        st.session_state.current_lvl = 1

    if 'tries' not in st.session_state:
        st.session_state.tries = 10

    if 'guesses2' not in st.session_state:
        st.session_state.guesses2 = 1

    if 'botsStreakList' not in st.session_state:
        data = pd.read_json("./src/data/data.json")
        data = pd.DataFrame(data)
        st.session_state.botsStreakList = data

    if 'allMbti' not in st.session_state:
        data = pd.read_json("./src/data/data.json")
        data = pd.DataFrame(data)
        st.session_state.allMbti = data['mbti'].tolist()

    if 'tutorial_classic' not in st.session_state:
        st.session_state.tutorial_classic = False

    if 'tutorial_streak' not in st.session_state:
        st.session_state.tutorial_streak = False

    if 'previous_bot' not in st.session_state:
        st.session_state.previous_bot = ""

    def login():

        st.write("### LOG IN")
        username = st.text_input("Username:")
        password = st.text_input("Password:", type="password")

        if st.button("LOG IN"):
            us = db.reference(f"/{username}").get()
            if us == None:
                db.reference("/").update({f"{username}/password": f"{password}"})
                db.reference("/").update({f"{username}/score_classic": "0"})
                db.reference("/").update({f"{username}/score_streak": "0"})
                st.error("Created an account, log in again")
            else:
                pas = db.reference(f"/{username}/password").get()
                if pas == password:
                    st.session_state.logged_in = True
                    st.session_state.username = username
                    st.experimental_rerun()  # Re-run the app to proceed to the main content
                else:
                    st.error("A user with this name exists, but you entered the wrong password")

    def start():
        with st.container(border=True):
            img, start_b, lvls_b = st.columns([1, 0.9, 1])

            # nie wiem czemu tak ma byc ale wtedy dziala znikanie po wcisnieciu start
            if st.session_state.start == 0:
                st.session_state.start = 1
                if start_b.button("Start", type="secondary", use_container_width=True): pass


            elif st.session_state.start == 1:
                st.subheader("Welcome to Who Am I? Tell me, what is your name?")

                username = st.text_input("Your name:", st.session_state.username)
                st.session_state.username = username

                if st.button("Meet Professor"):
                    st.session_state.start = 2
                    st.rerun()


            elif st.session_state.start == 2:

                utilis.margin_top(40)
                img.image("assets/scientist.png", width=350)
                utilis.margin_top(30)

                messages = st.container(height=150, border=True)

                # introduction
                if st.session_state.text < 8:
                    messages.write_stream(utilis.stream_data(st.session_state.text))

                # a little bit about mbti types
                elif st.session_state.text >= 8:
                    messages.write_stream(utilis.stream_data2(st.session_state.text - 8))

                # if not st.session_state.research:
                if st.session_state.text < 24:
                    st.session_state.text += 1

                if st.session_state.text == 6 and st.session_state.lvl == 0:
                    st.session_state.text = 5

                    # TUTAJ SA POZIOMY
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
                    # TU KONIEC POZIOMOW

                if st.session_state.text >= 24:
                    st.session_state.text = 23
                    messages.empty()

                    if messages.button("Start classic research", type="secondary"):
                        st.session_state.window = "game"
                        st.rerun()
                    if messages.button("Start streak game", type="secondary"):
                        st.session_state.window = "streak"
                        st.rerun()

                elif st.session_state.text < 24:
                    if messages.button("→", type="secondary") or st.session_state.lvl > 0:
                        messages.empty()

    def manage():
        if st.session_state.window == "game" and not st.session_state.tutorial_classic:
            st.session_state.gamemode = 0
            game.tutorial()
        elif st.session_state.window == "game" and st.session_state.tutorial_classic:
            st.session_state.gamemode = 0
            game.game()
        elif st.session_state.window == "help":
            help.help()
        elif st.session_state.window == "start":
            start()
        elif st.session_state.window == "about":
            about.about()
        elif st.session_state.window == "streak" and not st.session_state.tutorial_streak:
            st.session_state.gamemode = 1
            streak.tutorial()
        elif st.session_state.window == "streak" and st.session_state.tutorial_streak:
            st.session_state.gamemode = 1
            streak.streak()

    if not st.session_state.logged_in:
        if not firebase_admin._apps:
            cred_obj = firebase_admin.credentials.Certificate('cred.json')
            default_app = firebase_admin.initialize_app(cred_obj, {
                'databaseURL': "https://who-am-i-c969c-default-rtdb.europe-west1.firebasedatabase.app/"})
        ref = db.reference("/")
        login()
    else:
        if st.session_state.window != "game" and st.session_state.window != "streak":
            st.session_state.window = "start"

    with st.sidebar:
        utilis.margin_top(40)
        st.image("assets/scientist.png", use_column_width=True)
        utilis.margin_bottom(30)

        b0 = st.button("Classic Game", type="secondary", use_container_width=True)
        b4 = st.button("Streak challenge", type="secondary", use_container_width=True)
        b1 = st.button("Get help from Professor", type="secondary", use_container_width=True)
        b2 = st.button("Start again your research", type="secondary", use_container_width=True)
        b3 = st.button("About us", type="secondary", use_container_width=True)

    if st.session_state.logged_in:
        if b0:
            st.session_state.window = "game"
        elif b1:
            st.session_state.window = "help"
        elif b2:
            st.session_state.window = "start"
        elif b3:
            st.session_state.window = "about"
        elif b4:
            st.session_state.window = "streak"
    manage()