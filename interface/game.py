import streamlit as st
import pandas as pd
# import app
import random
from ChatManager.ChatManager import CM

def game():

    # @st.cache_data
    # def bots_num(lvl = 4):
    #     return lvl

    # @st.cache_data
    # def get_types():
    #     data = pd.read_json("data.json")
    #     data = pd.DataFrame(data)
    #
    #     types = data['mbti'].sample(n=4)
    #
    #     return types


    @st.cache_data
    def bots_num():
        return st.session_state.level

    @st.cache_data
    def additional_personalities():
        return 2


    @st.cache_data
    def get_data():
        data = pd.read_json("data.json")
        data = pd.DataFrame(data)

        selected_data = data.sample(n=bots_num()+additional_personalities())
        selected_names = selected_data['name'].tolist()
        selected_mbti = selected_data['mbti'].tolist()

        return selected_names, selected_mbti

    @st.cache_resource
    def init_CM(names):
        cm = CM(n_people=len(names))
        for name in names:
            cm.add_defaulted_system_prompt(name)
            print(names)
        return cm

    @st.cache_data
    def shuffle(mbtis):
        return random.sample(mbtis, len(mbtis))


    BOTS = bots_num()
    ACTIVE_BOT = 1

    # getting data
    # types = get_types()
    names,mbtis = get_data()
    shuffled_mbtis = shuffle(mbtis)

    chat, bots, guesses = st.columns([1.5,1, 0.8], gap="medium")
    cm = init_CM(names[0:BOTS])



    with chat:
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
                # st.experimental_rerun()


    with bots:
        with st.container(border=True, height=550):
            st.image("assets/temp.png", use_column_width=True)

    with guesses:
        with st.container(border=True, height=550):
            options = []
            for bot in range(BOTS):
                index = None
                if 'selected_option' in st.session_state:
                    index = st.session_state.selected_option[bot]
                option = st.selectbox(
                    f"Bot {bot+1}",
                    (shuffled_mbtis),
                    index=index,
                    placeholder="Am I...",
                    key = f"bot{bot+1}")
                print(option)

                if 'selected_option' not in st.session_state:
                    temp = [None]*BOTS
                    st.session_state.selected_option = temp

                if not option is None:
                    st.session_state.selected_option[bot] = shuffled_mbtis.index(option)
                options.append(option)
        if st.button("Finish research", type="secondary", use_container_width=True):
            counter = 0
            for i in range(0, len(options)):
                if options[i] == mbtis[i]:
                    counter += 1
            score = counter / st.session_state.level * 100
            st.empty()
            st.write(f'Congratulations! {score}% of your answers were correct')


