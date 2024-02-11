import streamlit as st
import time

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
    st.markdown(f'<div style="margin-top: {px}px;</div>',unsafe_allow_html=True)

def margin_bottom(px):
    st.write(f'<div style="margin-bottom: {px}px;</div>',unsafe_allow_html=True)


def stream_data(idx):
    texts = [
        "Welcome to the glow of neon lights and spinning gears of a cyberpunk laboratory, where mysterious science blends with intrigue and ambition. As a student of an eccentric scientist, you find yourself at the epicenter of an extraordinary experiment whose goal is nothing less than world domination through the creation of perfect copies of human personality.",
        "Your mentor, a genius of scientific madness, has long focused on creating humanoid robots that mimic influential figures. He creates them, develops them, and programs them to be indistinguishable from their originals. His elaborate plan for world domination involves manipulating even the simplest units by replacing them with clones.",
        "Your task is to delve into the mysteries of human personality, all within the framework of exercises in the laboratory. After greeting your mentor, you head deeper into the laboratory, ready for the next stage of your education. Your skills will be put to the test during a trial where you must match the personality type to each of the robots. By talking to them and asking questions, you must explore their nature to later create credible copies of people.",
        "An extraordinary journey begins through the intricacies of the human psyche and technological manipulation, where your decisions will shape the future of this cyberpunk world of science. Are you ready for the challenge? Take the test and delve into the secrets of the human soul to become a master of the art of creating perfect replicas of human personality."
    ]
    for word in texts[idx].split():
        yield word + " "
        time.sleep(0.07)


