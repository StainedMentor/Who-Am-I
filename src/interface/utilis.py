import streamlit as st
import time
import pandas as pd

def background():
    st.markdown(
        """
        <style>

        .stApp {
            background-image: url("https://github.com/StainedMentor/Who-Am-I/blob/main/assets/tests/bg4a.png?raw=true");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            background-attachment: fixed;
            
        }
        
        
        </style>
        """,
        unsafe_allow_html=True

    )
    # remove_space()


def container_bg():
    st.markdown(
        """
        <style>

         div[data-testid="stVerticalBlock"] > div{

            background-color: rgba(28, 28, 28, 0.7);
            border-radius: 15px;
            max-width: 80%
            margin: auto;
            margin-right:20px


        }

         div[data-testid="stVerticalBlock"] > div:nth-child(n+4) > div:nth-child(-n+6){
            display: inherit
            background-color: rgba(28, 28, 28, 0.7);
            border-radius: 15px;
            max-width: 80%
            margin: auto;
            margin-right: 10px;

            padding:20px;



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
    st.write(f'<div class="other" style="margin-top: {px}px;</div>',unsafe_allow_html=True)

def margin_bottom(px):
    st.write(f'<div class="other" style="margin-bottom: {px}px;</div>',unsafe_allow_html=True)


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
    mbti_data = pd.read_json("src/data/mbti_data.json")
    mbti_data = pd.DataFrame(mbti_data)

    for word in mbti_data.iloc[idx]['type'].split():
        yield word + " "
        time.sleep(0.07)

    for word in mbti_data.iloc[idx]['description'].split():
        yield word + " "
        time.sleep(0.07)

def center_title():
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

def github():

    st.markdown('<a href="https://github.com/StainedMentor/Who-Am-I">'
                '<img src="https://github.com/StainedMentor/Who-Am-I/blob/main/assets/github-mark-white.png?raw=true" '
                'width="50" height="50"></a>',
                unsafe_allow_html=True)

def avatar(path):
    st.markdown(
        """
        <style>
        .centered-image {
            display: block;
            margin-left: auto;
            margin-right: auto;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.markdown('<a href="https://github.com/StainedMentor/Who-Am-I">'
                f'<img src="https://github.com/StainedMentor/Who-Am-I/blob/main/assets/avatars/{path}.png?raw=true" '
                'width="300" height="300" class="centered-image" ></a>',
                unsafe_allow_html=True)

def game_dsc():
    st.markdown("""
                **<span style="font-size: 24px;">Welcome to Classic Game mode!</span>**<br> Your goal is to uncover the MBTI personality types of hidden characters, both fictional and real. Here’s a guide on how to play effectively:

                **<span style="font-size: 24px;">Start the Game:</span>**<br>
                When you launch Classic Game mode, you will see a list of characters hidden behind avatars.

                **<span style="font-size: 24px;">Communicating with Characters:</span>**<br>
                Click on any character to open a dialog window.
                Ask questions to get clues about their personality. Remember, characters will try to hide their true identity, so formulate your questions precisely.

                **<span style="font-size: 24px;">Analyzing Responses:</span>**<br>
                Carefully analyze the characters' responses. Pay attention to details that may indicate their MBTI personality type.

                **<span style="font-size: 24px;">Using Professor's Help:</span>**<br>
                If you feel stuck, you can ask the Professor for hints. Remember, you can only ask for help 3 times during a single game, so use this option wisely.

                **<span style="font-size: 24px;">Choosing the Personality Type:</span>**<br>
                After gathering enough information, select the MBTI personality type that best fits the analyzed character.
                Depending on the chosen difficulty level, the number of available MBTI types may vary. Remember that personality types can repeat.

                **<span style="font-size: 24px;">Game Objective:</span>**<br>
                Your main goal is to improve your skills in recognizing personality types. Through the game, you will learn to better understand different human characters, which can be useful both in everyday life and professionally.
                <br>
                Have fun and enhance your skills in identifying personality types!
                """, unsafe_allow_html=True)

def streak_dsc():
    st.markdown("""
                **<span style="font-size: 24px;">Welcome to Streak Challenge mode!</span>**<br> Your goal is to achieve the longest streak by correctly identifying the MBTI personality types of a single character. Here’s how to play:

                **<span style="font-size: 24px;">Start the Game:</span>**<br>
                When you launch Streak Challenge mode, you will see one hidden character.

                **<span style="font-size: 24px;">Communicating with the Character:</span>**<br>
                Click on the character to open a dialog window.
                Ask questions to gather clues about their personality. Remember, the character will try to hide their true identity, so formulate your questions carefully.

                **<span style="font-size: 24px;">Message Limitation:</span>**<br>
                You have a limited number of messages you can send at each stage. This number is dynamic and decreases every few stages, increasing the difficulty level.

                **<span style="font-size: 24px;">Analyzing Responses:</span>**<br>
                Carefully analyze the character's responses. Look for details that may indicate their MBTI personality type.

                **<span style="font-size: 24px;">Using Professor's Help:</span>**<br>
                If you get stuck, you can ask the Professor for hints. Remember, you can only ask for help 3 times during a single game, so use this option wisely.

                **<span style="font-size: 24px;">Choosing the Personality Type:</span>**<br>
                After gathering enough information, select the MBTI personality type that best fits the analyzed character.
                As you progress through the game, the number of available MBTI types in the selection window will increase, making the game more challenging.

                **<span style="font-size: 24px;">Increasing the Streak:</span>**<br>
                After a correct answer, your streak will increase. The goal is to achieve the longest streak by continuously correctly identifying personality types.

                **<span style="font-size: 24px;">Game Objective:</span>**<br>
                Your main goal is to improve your skills in recognizing personality types, which will help you better understand different human characters.
                <br>
                Have fun and try to achieve the longest streak, enhancing your skills in identifying personality types!
                """, unsafe_allow_html=True)