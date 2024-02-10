import utilis
import streamlit as st
import pandas as pd


st.set_page_config(page_title= "Who am I?", layout="wide")

@st.cache_data
def bots_num():
    return 4

@st.cache_data
def get_names():
    data = pd.read_json("data.json")
    data = pd.DataFrame(data)

    names = data['name'].sample(n=4)

    return names

BOTS = bots_num()
ACTIVE_BOT = 1
#page 1

utilis.add_logo()
# utilis.remove_space()

#getting data
names = get_names()


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




col1, col2, col3 = st.columns([1.5,1, 0.8], gap="medium")

with col1:
    with st.container(border=True):
        st.write(
        f'<div style="text-align: center; margin-bottom: 20px; font-size: 24px;'
        f'">Choose your fighter</div>',
        unsafe_allow_html=True)

        columns = st.columns(BOTS)

        for i in range(len(columns)):
            with columns[i]:
                if st.button(f"Bot {i+1}", type="secondary",key=i, use_container_width=True):
                    ACTIVE_BOT = i+1


        messages = st.container(height=300, border=True)

        if prompt := st.chat_input(placeholder="Your message"):
            messages.chat_message("user").write(prompt)
            messages.chat_message("assistant").write(f"Echo: {prompt}")
            # st.experimental_rerun()


with col2:
    with st.container(border=True, height=500):
        st.image("assets/temp.png", use_column_width=True)

with col3:
    with st.container(border=True, height=500):
        options = []
        for bot in range(BOTS):
            option = st.selectbox(
                f"Bot {bot+1}",
                (names),
                index=None,
                placeholder="Am I...",
                key = f"bot{bot+1}")

            if 'option' not in st.session_state:
                st.session_state.selected_option = option

            options.append(option)
            print(option)
    if st.button("Finish research", type="secondary", use_container_width=True):
        pass


