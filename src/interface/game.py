import streamlit as st
import pandas as pd
from streamlit_modal import Modal
import random
from src.ChatManager_Package.ChatManager import CM


from firebase_admin import db, credentials
from . import utilis


def tutorial():

    with st.container(border=True):
        # Use the custom CSS class for centering
        st.markdown("""
            <h1 style="text-align:center">How to play Classic Mode?</h1>
            """, unsafe_allow_html=True)
        utilis.game_dsc()
        if st.button("Let's Play", type="primary", use_container_width=True):
            st.session_state.window = "game"
            st.session_state.tutorial_classic = True
            st.rerun()

def game():

    if st.session_state.gamemode == 0:
        print("Classic Gamemode")
    else:
        print("Streak Gamemode")

    @st.cache_data
    def bots_num():
        return st.session_state.level

    @st.cache_data
    def additional_personalities():
        return 2


    # @st.cache_data
    def get_data():
        data = pd.read_json("src/data/data.json")
        data = pd.DataFrame(data)
        selected_data = data.sample(n=bots_num()+additional_personalities())
        selected_names = selected_data['name'].tolist()
        selected_mbti = selected_data['mbti'].tolist()

        return selected_names, selected_mbti

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
        db.reference(f"/{user}/score_classic").set(str(st.session_state.score))
        return update

    def get_all_scores():
        users = db.reference("/").get()
        data = []
        for user, info in users.items():
            if "score_classic" in info:
                data.append({'username': user, 'score': float(info['score_classic'])})
        return pd.DataFrame(data)


    def rerun_level():
        temp = [None] * BOTS
        st.session_state.selected_option = temp
        st.session_state.curr_lvl += 1
        st.session_state.lvl_data = get_data()
        names, mbtis = st.session_state.lvl_data
        st.session_state.hints_classic = 3
        cm.reset(BOTS)
        add_names(names[0:BOTS])
    def res_score(score):
        st.session_state.score -= score


    BOTS = bots_num()
    ACTIVE_BOT = 1

    if 'lvl_data' not in st.session_state:
        st.session_state.lvl_data = get_data()


    names,mbtis = st.session_state.lvl_data
    shuffled_mbtis = shuffle(mbtis)

    #containery
    chat, bots, guesses = st.columns([1.5,1.0, 0.8], gap="medium")
    cm = init_CM()

    if st.session_state.curr_lvl==1:
        add_names(names[0:BOTS])




    with chat:
        #user info above chats
        temp1, temp2, temp3, temp4 = st.columns([1,1,1,1], gap="small")
        with temp1: st.write(f"name: {st.session_state.username}")
        with temp2: st.write(f"score: {st.session_state.score}")
        with temp3: st.write(f"streak: {st.session_state.streak_classic}")
        with temp4: st.write(f"level: {st.session_state.curr_lvl}")

        #chats
        with st.container(border=True):
            st.write(
            f'<div style="text-align: center; margin-bottom: 20px; font-size: 24px;'
            f'">Choose your fighter</div>',
            unsafe_allow_html=True)

            columns = st.columns(BOTS)

            for i in range(len(columns)):
                with columns[i]:
                    if st.button(f"Bot {i+1}", type="secondary",key=i, use_container_width=True):
                        ACTIVE_BOT = i
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


    with bots:
        #avaible hints above bots img
        st.write(f"hints: {st.session_state.hints_classic}")
        with st.container(border=True, height=550):
            st.image("assets/temp.png", use_column_width=True)


    with guesses:
        #hints button and select boxes
        if st.button("Call Professor", type="primary", use_container_width=True) and st.session_state.hints_classic >0:
            help = Modal(key="help",title="Help")
            st.session_state.hints_classic-=1
            with help.container():
                img, text = st.columns([0.8,1.2], gap="large")
                with img: st.image("assets/scientist.png", use_column_width=True)
                with text:
                    #tutaj prmpty podpowiedzi dla wybranego bota
                    st.write(f"selected bot: {cm.selected_p+1}")
                    st.write(cm.get_hint_stream())


        with st.container(border=True, height=550):
            options = []
            for bot in range(BOTS):
                #print(bot)
                index = None
                if 'selected_option' in st.session_state:
                    index = st.session_state.selected_option[bot]
                option = st.selectbox(
                    f"Bot {bot+1}",
                    (shuffled_mbtis),
                    index=index,
                    placeholder="Am I...",
                    key = f"bot{bot+1}")

                if 'selected_option' not in st.session_state:
                    temp = [None]*BOTS
                    st.session_state.selected_option = temp

                if not option is None:
                    st.session_state.selected_option[bot] = shuffled_mbtis.index(option)
                options.append(option)


        #finish game
        if st.button("Finish research", type="secondary", use_container_width=True):
            counter = 0
            for i in range(0, len(options)):
                if options[i] == mbtis[i]:
                    counter += 1

            #score and streak managment
            score = counter / st.session_state.level * 100
            st.session_state.score += score
            st.empty()

            #streak
            if score == 100:
                st.session_state.streak_classic += 1

            else:
                st.session_state.streak_classic = 0


            recent = db.reference(f"/{st.session_state.username}/score_classic").get()
            if float(recent)<st.session_state.score:
                db.reference("/").update({f"{st.session_state.username}/score_classic": f"{st.session_state.score}"})


            #scoreboard display
            scoreboard = Modal(key="score",title="Scoreboard")

            with scoreboard.container():
                st.write(f"Your score in this game was: {st.session_state.score2}")
                all_scores = get_all_scores()
                sorted_scores = all_scores.sort_values(by='score', ascending=False)
                st.dataframe(sorted_scores, use_container_width=True)

                temp1, temp2 = st.columns([0.3, 1], gap='small')
                with temp1:
                    if st.button("Next round", type="primary", on_click=rerun_level): pass
                with temp2:
                    if st.button("Improve in this level", type="secondary",on_click=res_score(score)):pass





