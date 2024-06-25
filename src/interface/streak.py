import streamlit as st
import pandas as pd
from streamlit_modal import Modal
import random
from src.ChatManager_Package.ChatManager import CM

from firebase_admin import db, credentials
from . import utilis

def tutorial():
    # Custom CSS to center the title
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

    utilis.remove_space()
    with st.container(border=True):
        # Use the custom CSS class for centering
        st.markdown("<h1 class='centered-title'>How to play Streak Challenge?</h1>", unsafe_allow_html=True)
        st.write("siema")
        if st.button("Let's Play", type="primary", use_container_width=True):
            st.session_state.window = "streak"
            st.session_state.tutorial_streak = True
            st.rerun()

def streak():

    @st.cache_data
    def additional_personalities():
        if st.session_state.current_lvl <= 25:
            update = 4 + int((st.session_state.current_lvl/5))
        else:
            update = 8
        return update


    def get_data():
        botsStreakList = st.session_state.botsStreakList
        random_mbti = random.sample(st.session_state.allMbti, 1 + additional_personalities())
        namesStreak = botsStreakList['name'].tolist()
        mbtiStreak = botsStreakList['mbti'].tolist()
        chosenBotName = random.choice(namesStreak)
        index = namesStreak.index(chosenBotName)
        chosenBotMbti = mbtiStreak[index]

        st.session_state.botsStreakList = botsStreakList[
            botsStreakList['name'] != chosenBotName]

        return chosenBotName, chosenBotMbti, random_mbti

    @st.cache_resource
    def init_CM():
        cm = CM()
        return cm


    @st.cache_resource
    def add_names(names):
        for name in names:
            cm.add_defaulted_system_prompt(name)

    @st.cache_data
    def shuffle(mbtis):
        return random.sample(mbtis, len(mbtis))

    def update_scoreboard(score, df, user=st.session_state.username):
        new_data = {'username': [user], 'score': [score]}
        data = pd.DataFrame(new_data)
        update = pd.concat([df, data], ignore_index=True)
        db.reference(f"/{user}/score_streak").set(str(st.session_state.score2))
        return update

    def get_all_scores():
        users = db.reference("/").get()
        data = []
        for user, info in users.items():
            if "score_streak" in info:
                data.append({'username': user, 'score': float(info['score_streak'])})
        return pd.DataFrame(data)

    def rerun_level():
        del st.session_state['selected_option_streak']
        st.session_state.current_lvl+=1
        st.session_state.streak_streak += 1
        score = (st.session_state.tries + 1) * 10
        st.session_state.score2 += score
        st.empty()
        st.session_state.data = update_scoreboard(score, st.session_state.data)
        st.session_state.lvl_data_streak = get_data()
        chosenBot, chosenBotMbti, mbtis = st.session_state.lvl_data_streak
        cm.reset(BOTS)
        cm.add_defaulted_system_prompt(chosenBot)

        if st.session_state.current_lvl <= 25:
            st.session_state.tries = 10 - (int(st.session_state.current_lvl/5))
        else:
            st.session_state.tries = 5
        st.rerun()
    def reset_level():
        del st.session_state['selected_option_streak']
        st.session_state.current_lvl=1
        st.session_state.streak_streak = 0
        st.session_state.score2 = 0
        st.session_state.score = 0
        st.empty()
        st.session_state.lvl_data_streak = get_data()
        chosenBot, chosenBotMbti, mbtis = st.session_state.lvl_data_streak
        cm.reset(BOTS)
        cm.add_defaulted_system_prompt(chosenBot)
        st.session_state._streak = 3
        if st.session_state.current_lvl <= 25:
            st.session_state.tries = 10 - (int(st.session_state.current_lvl/5))
        else:
            st.session_state.tries = 5


    def gameOverInfo():
        gameover = Modal(key="gameover", title="Game Over")
        recent = db.reference(f"/{st.session_state.username}/score_streak").get()
        if float(recent) < st.session_state.score2:
            db.reference("/").update({f"{st.session_state.username}/score_streak": f"{st.session_state.score2}"})

        with gameover.container():
            if st.session_state.tries == 0:
                st.write("You have exceeded the number of available tries!")
            else:
                st.write("Your answer was incorrect!")
                st.write(f"Your score in this game was: {st.session_state.score2}")

            all_scores = get_all_scores()
            sorted_scores = all_scores.sort_values(by='score', ascending=False)
            st.dataframe(sorted_scores, use_container_width=True)

            temp1, temp2, temp3, temp4, temp5 = st.columns([0.3, 1, 1,0.3,0.3], gap='small')

            with temp3:
                if st.button("Try Again", type="primary", on_click=reset_level):pass

    BOTS = 1

    if st.session_state.tries == 0:
        gameOverInfo()

    if 'lvl_data_streak' not in st.session_state:
        st.session_state.lvl_data_streak = get_data()
    chosenBot, chosenBotMbti, mbtis = st.session_state.lvl_data_streak

    print("Poprawna Odpowiedź")
    print(chosenBotMbti)
    isthere = all(element != chosenBotMbti for element in mbtis)
    if isthere:
        mbtis.pop()
        mbtis.append(chosenBotMbti)

    shuffled_toguess = shuffle(mbtis)

    #containery
    chat, bots, guesses = st.columns([1.5,1, 0.8], gap="medium")
    cm = init_CM()
    cm.add_defaulted_system_prompt(chosenBot)


    with chat:
        #user info above chats
        temp1, temp2, temp3, temp4, temp5= st.columns([1,1,1,1,1], gap="small")
        with temp1: st.write(f"name: {st.session_state.username}")
        with temp2: st.write(f"score: {st.session_state.score2}")
        with temp3: st.write(f"streak: {st.session_state.streak_streak}")
        with temp5: st.write(f"tries: {st.session_state.tries}")

        #chats
        with st.container(border=True):
            st.write(
            f'<div style="text-align: center; margin-bottom: 20px; font-size: 24px;'
            f'">Try to guess Who Am I</div>',
            unsafe_allow_html=True)

            ACTIVE_BOT = 0
            cm.switch_p(ACTIVE_BOT)
            messages = st.container(height=350, border=True)
            for message in cm.chats[cm.selected_p]:
                with messages.chat_message(message["role"]):
                    st.write(message["content"])

            if prompt := st.chat_input(placeholder="Your message"):
                messages.chat_message("user").write(prompt)
                cm.add_user_message(prompt)
                stream = cm.get_response_stream()
                with messages.chat_message("assistant"):
                    st.write_stream(stream)
                st.session_state.tries -= 1
                st.rerun()

    with bots:
        #avaible hints above bots img
        st.write(f"hints: {st.session_state.hints_streak}")
        with st.container(border=True, height=550):
            st.image("assets/temp.png", use_column_width=True)


    with guesses:
        #hints button and select boxes
        if st.button("Call Professor", type="primary", use_container_width=True) and st.session_state.hints_streak > 0:
            help = Modal(key="help",title="Help")
            st.session_state.hints_streak-=1
            with help.container():
                img, text = st.columns([0.8,1.2], gap="large")
                with img: st.image("assets/scientist.png", use_column_width=True)
                with text:
                    #tutaj prmpty podpowiedzi dla wybranego bota
                    #st.write(f"selected bot: {cm.selected_p+1}")
                    st.write(cm.get_hint_stream())


        with st.container(border=True, height=550):
            index = None
            options = []
            if 'selected_option_streak' in st.session_state:
                index = st.session_state.selected_option_streak[0]
            option = st.selectbox(
                f"Try to Guess",
                (shuffled_toguess),
                index=index,
                placeholder="Am I...",
                key = f"bot{0+1}")
            if 'selected_option_streak' not in st.session_state:
                temp = [None]
                st.session_state.selected_option_streak = temp
            options.append(option)
        #finish game
        if st.button("Next round", type="secondary", use_container_width=True):
            rightPick = False
            if options[0] == chosenBotMbti:
                rightPick = True
            #score and streak managment
            #streak
            if rightPick == True:
                print("Guessed correcly")
                rerun_level()
            #Wrong Answer
            else:
                gameOverInfo()
