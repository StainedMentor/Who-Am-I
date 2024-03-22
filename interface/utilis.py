import streamlit as st
import time
import pandas as pd

def background():
    st.markdown(
        """
        <style>

        .stApp {
            background-image: url("https://github.com/StainedMentor/Who-Am-I/blob/main/assets/tests/bg1.jpg?raw=true");
            background-size: 50%,50%
            
        }
        </style>
        """,
        unsafe_allow_html=True
    )


def container_bg():
    st.markdown(
        """
        <style>
    
         div[data-testid="stVerticalBlock"] > div{
            background-color: #1c1c1c;
            border-radius: 15px;
            max-width: 80%
            margin: auto;


        }
   
        </style>
        """,
        unsafe_allow_html=True
    )




def add_logo():
    st.markdown(
        """
        <style>
            [data-testid="stSidebar"] {
                background-image: url(https://github.com/StainedMentor/Who-Am-I/blob/main/assets/title.png?raw=true);
                background-repeat: no-repeat;
                background-size: contain;
                }

        </style>
        """,
        unsafe_allow_html=True,
    )

def remove_space():
    st.markdown("""
            <style>
                   .block-container {
                        padding-top: 1rem;
                        padding-bottom: 2rem;
                        padding-left: 5rem;
                        padding-right: 5rem;
                    }
            </style>
            """, unsafe_allow_html=True)


def margin_top(px):
    st.write(f'<div style="margin-top: {px}px;</div>',unsafe_allow_html=True)

def margin_bottom(px):
    st.write(f'<div style="margin-bottom: {px}px;</div>',unsafe_allow_html=True)


def stream_data(idx):
    texts = [
        f"Welcome {st.session_state.username} to the glow of neon lights and spinning gears of a cyberpunk laboratory, where mysterious science blends with intrigue and ambition. As a student of an eccentric scientist, you find yourself at the epicenter of an extraordinary experiment whose goal is nothing less than world domination through the creation of perfect copies of human personality.",
        "Your mentor, a genius of scientific madness, has long focused on creating humanoid robots that mimic influential figures. He creates them, develops them, and programs them to be indistinguishable from their originals. His elaborate plan for world domination involves manipulating even the simplest units by replacing them with clones.",
        "Your task is to delve into the mysteries of human personality, all within the framework of exercises in the laboratory. After greeting your mentor, you head deeper into the laboratory, ready for the next stage of your education. Your skills will be put to the test during a trial where you must match the personality type to each of the robots. By talking to them and asking questions, you must explore their nature to later create credible copies of people.",
        "An extraordinary journey begins through the intricacies of the human psyche and technological manipulation, where your decisions will shape the future of this cyberpunk world of science. Are you ready for the challenge? Take the test and delve into the secrets of the human soul to become a master of the art of creating perfect replicas of human personality.",
        "During your research you can use my notes. They are on the left panel of your tablet.",
        "So let's get started. Considering that today is your first day of testing, I'll let you choose the set for testing. I have prepared three sets of robots for you: Small set contains 4, medium 5, and large 6.",
        "Great choice. Firstly, I am going to explain to you basic concepts of each of MBTI type and then you can start your resarch. I will be waiting for the results till 8 PM. Do not disappoint me.",
        "All types are unique, there are 16 of them."
    ]
    for word in texts[idx].split():
        yield word + " "
        time.sleep(0.07)

def stream_data2(idx):
    mbti_data = pd.read_json("mbti_data.json")
    mbti_data = pd.DataFrame(mbti_data)

    for word in mbti_data.iloc[idx]['type'].split():
        yield word + " "
        time.sleep(0.07)

    for word in mbti_data.iloc[idx]['description'].split():
        yield word + " "
        time.sleep(0.07)


def github():

    st.markdown('<a href="https://github.com/StainedMentor/Who-Am-I">'
                '<img src="https://github.com/StainedMentor/Who-Am-I/blob/main/assets/github-mark-white.png?raw=true" '
                'width="50" height="50"></a>',
                unsafe_allow_html=True)
