import streamlit as st
import pandas as pd
from streamlit_modal import Modal
import random
from ChatManager.ChatManager import CM


#DATA
if 'data' not in st.session_state:
    st.session_state.data = pd.DataFrame({'username': [], 'score': []})

if 'hints' not in st.session_state:
    st.session_state.hints = 3

if 'score2' not in st.session_state:
    st.session_state.score2 = 0

if 'streak' not in st.session_state:
    st.session_state.streak = 0

if 'current_lvl' not in st.session_state:
    st.session_state.current_lvl = 1

if 'tries' not in st.session_state:
    st.session_state.tries = 10

if 'guesses2' not in st.session_state:
    st.session_state.guesses2 = 1

if 'botsStreakList' not in st.session_state:
    data = pd.read_json("data.json")
    data = pd.DataFrame(data)
    st.session_state.botsStreakList = data

if 'allMbti' not in st.session_state:
    data = pd.read_json("data.json")
    data = pd.DataFrame(data)
    st.session_state.allMbti = data['mbti'].tolist()


def streak():

    @st.cache_data
    def additional_personalities():
        if st.session_state.current_lvl <= 25:
            update = 4 + int((st.session_state.current_lvl/5))
        else:
            update = 8
        return update


    # @st.cache_data
    def get_data():
        botsStreakList = st.session_state.botsStreakList
        random_mbti = random.sample(st.session_state.allMbti, 1 + additional_personalities())
        namesStreak = botsStreakList['name'].tolist()
        mbtiStreak = botsStreakList['mbti'].tolist()
        chosenBotName = random.choice(namesStreak)
        index = namesStreak.index(chosenBotName)
        chosenBotMbti = mbtiStreak[index]

        print("TEST 0")
        print(chosenBotName)
        print(chosenBotMbti)

        st.session_state.botsStreakList = botsStreakList[
            botsStreakList['name'] != chosenBotName]

        print("TEST")
        print(random_mbti)
        print(chosenBotName)
        print(chosenBotMbti)
        print("pitu pitu")

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


    def update_scoreboard(score, df, user = st.session_state.username):
        new_data = {'username': [user], 'score': [score]}
        data = pd.DataFrame(new_data)
        update = pd.concat([df,data],ignore_index=True)
        return update

    def modified_stream_generator(original_stream):
        original_list = list(original_stream)
        num_chars_to_replace = int(0.1 * len(original_list))
        indexes_to_replace = random.sample(range(len(original_list)), num_chars_to_replace)
        for i, char in enumerate(original_list):
            if i in indexes_to_replace:
                yield '*'
            else:
                yield char


    def rerun_level():
        del st.session_state['selected_option']
        st.session_state.current_lvl+=1
        st.session_state.streak += 1
        score = (st.session_state.tries + 1) * 10
        st.session_state.score2 += score
        st.empty()
        st.session_state.data = update_scoreboard(score, st.session_state.data)
        st.session_state.lvl_data = get_data()
        chosenBot, chosenBotMbti, mbtis = st.session_state.lvl_data
        cm.reset(BOTS)
        cm.add_defaulted_system_prompt(chosenBot)

        if st.session_state.current_lvl <= 25:
            st.session_state.tries = 10 - (int(st.session_state.current_lvl/5))
        else:
            st.session_state.tries = 5
        st.rerun()

    def gameOverInfo():
        gameover = Modal(key="gameover", title="Game Over")

        with gameover.container():
            if st.session_state.tries == 0:
                st.write("You have exceeded the number of available tries!")
            else:
                st.write("Your answer was incorrect!")

            temp1, temp2, temp3, temp4 = st.columns([0.3, 1, 0.3,1], gap='small')

            with temp2:
                if st.button("Try Again", type="primary"):
                        pass

            with temp4:
                if st.button("Show Scoreboard", type="primary"):
                    scoreboard = Modal(key="score", title="Scoreboard")

                    with scoreboard.container():
                        sorted = st.session_state.data.sort_values(by='score', ascending=False)
                        st.dataframe(sorted, use_container_width=True)

                        temp1, temp2 = st.columns([0.3, 1], gap='small')

                        # w funkcji rerun level jest reset ustawien i trzeba dodac zarzadzanie levelami
                        with temp1:
                            if st.button("Try Again", type="primary", on_click=rerun_level): pass



    BOTS = 1

    if st.session_state.tries == 0:
        gameOverInfo()

    if 'lvl_data_streak' not in st.session_state:
        st.session_state.lvl_data_streak = get_data()
    chosenBot, chosenBotMbti, mbtis = st.session_state.lvl_data_streak
    print("TEST 2")
    print(chosenBot)
    print(len(st.session_state.botsStreakList))

    print("Test 2.5")
    print(chosenBotMbti)
    print(mbtis)
    isthere = all(element != chosenBotMbti for element in mbtis)
    if isthere:
        mbtis.pop()
        mbtis.append(chosenBotMbti)

    print("TEST 3")
    print(isthere)
    print(mbtis)

    shuffled_toguess = shuffle(mbtis)

    print("TEST 4")
    print(shuffled_toguess)

    #containery
    chat, bots, guesses = st.columns([1.5,1, 0.8], gap="medium")
    cm = init_CM()
    cm.add_defaulted_system_prompt(chosenBot)


    with chat:
        #user info above chats
        temp1, temp2, temp3, temp4, temp5= st.columns([1,1,1,1,1], gap="small")
        with temp1: st.write(f"name: {st.session_state.username}")
        with temp2: st.write(f"score: {st.session_state.score2}")
        with temp3: st.write(f"streak: {st.session_state.streak}")
        with temp5: st.write(f"tries: {st.session_state.tries}")
        print("Sprawdzam ten shiet")

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
                #if st.session_state.current_lvl>2:
                #    stream=modified_stream_generator(stream)
                with messages.chat_message("assistant"):
                    st.write_stream(stream)
                st.session_state.tries -= 1
                st.rerun()


    with bots:
        #avaible hints above bots img
        st.write(f"hints: {st.session_state.hints}")
        with st.container(border=True, height=550):
            st.image("assets/temp.png", use_column_width=True)


    with guesses:
        #hints button and select boxes
        if st.button("Call Professor", type="primary", use_container_width=True) and st.session_state.hints > 0:
            help = Modal(key="help",title="Help")
            st.session_state.hints-=1
            with help.container():
                img, text = st.columns([0.8,1.2], gap="large")
                with img: st.image("assets/scientist.png", use_column_width=True)
                with text:
                    #tutaj prmpty podpowiedzi dla wybranego bota
                    st.write(f"selected bot: {cm.selected_p+1}")
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

            #if not option is None:
             #   st.session_state.selected_option[0] = shuffled_toguess.index(option)
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

            else:
                gameOverInfo()
