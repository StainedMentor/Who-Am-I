# Who-Am-I
## Table of Contents
* [Description](#description)
* [The Game](#the-game)
* [Installation](#installation)
* [Run graphical interface](#run-graphical-interface)
* [Run in console instructions](#run-in-console-instructions)
  
## Description
Who Am I is a game about scientist assistant journey in a robots' lab. The journey begins with a short story and selecting difficulty level, then all 16 MBTI types are introduced to us with hort description. Next, the game begins. We (scientist assistants) must match all bots to MBTI personalities. We do our research with talking to each bot, getting to know them, asking questions which may lead to personality traits connected to pecific MBTI type. The research is done when we match all bots with avaible MBTI types, then results from the scientist come.\

## The Game
### Start
* User is introduced to the plot and MBTI types.
* User can select one of 3 difficulty levels, each defines number of bots in gamplay - easy = 4, medium = 5, hard = 6.\
  \
![start](https://github.com/StainedMentor/Who-Am-I/blob/main/assets/select.png)
  
### Game
* User can use sidebar window to choose page -> game, help, start, settings. Game is a page for gameplay, help contains short notes about MBTI types, start restarts the game and settings manipulates options in the game.
* On the left column there is a chat for each of X bots.
* On the center column there is a representation of our game show.
* On the right column there are X selcectboxes with a list of couple MBTI types.
* User can talk to each bot by selecting specific button on the top of the left column. Bots mimic certain celebrity, they can not tell user who they are.
* User chooses predicted MBTI type for each bot on the right column selectboxes.
* After clicking "Finish research" button, user gets his results in %.\
  \
![game](https://github.com/StainedMentor/Who-Am-I/blob/main/assets/game.png)
  
### Help
![help](https://github.com/StainedMentor/Who-Am-I/blob/main/assets/help.png)
 
* E: Extroversion - This dimension represents how individuals interact with the world. Extroverts tend to be outgoing, social, and energized by interactions with others.
* N: Intuition - This dimension represents how individuals process information. Intuitive individuals tend to focus on patterns, possibilities, and abstract concepts rather than concrete details.
* T: Thinking - This dimension represents how individuals make decisions. Thinkers tend to prioritize logic and objective analysis when making decisions.
* J: Judging - This dimension represents how individuals approach structure and organization. Judging individuals prefer a structured and organized lifestyle, with a focus on planning and decision-making.
* I: Introversion - This dimension represents how individuals interact with the world. Introverts tend to be more reserved, reflective, and energized by time spent alone or in small groups.
* S: Sensing - This dimension represents how individuals process information. Sensing individuals tend to focus on concrete details, facts, and information gathered through their five senses.
* F: Feeling - This dimension represents how individuals make decisions. Feelers tend to prioritize empathy, harmony, and the impact on others when making decisions.
* P: Perceiving - This dimension represents how individuals approach structure and organization. Perceiving individuals prefer a flexible and spontaneous lifestyle, with a focus on adaptability and openness to new experiences 

### Tools used
The project uses Llama3 at its core. The API we built around the model uses llama-cpp-python as it had the best crossplatform hardware utilisation. It is designed in a manner where we could use bindings to different models to run the application. We also found that running larger than 8B parameter models on local machines with 8GB RAM is not viable. After some testing we found that the 8B 4_K_M quantised model has the best performance and doesnt run out of RAM.
## Installation
After cloning the repository and installing requirement, download and add the model to the projects directory: https://huggingface.co/QuantFactory/Meta-Llama-3-8B-Instruct-GGUF/resolve/main/Meta-Llama-3-8B-Instruct.Q4_K_M.gguf?download=true

After installing requirements, change the config file in  `~/.streamlit/config.toml.` directory.

On mac everything should work out of the box. If you are working on windows llama-cpp-python installs a CPU only version, which is extremely slow for this project. You can reinstall this package with the following command to use hardware acceleration `Use command prompt with the projects venvs selected to reinstall`:
```
set CMAKE_ARGS=-DLLAMA_CUBLAS=on
set FORCE_CMAKE=1
pip install llama-cpp-python --force-reinstall --upgrade --no-cache-dir
```
If you are running the project outside of pycharm you might have to manually activate your default python venv to set the environment parameters.
If there are further issues with text generation being slow please refer to this documentation: https://llama-cpp-python.readthedocs.io/en/latest/

## Run Application
After finishing the installation run in the projects directory this command:
```
streamlit run AppEntry.py
```
This should open autmatically in your browser. If not it would display a link in the console

WARNING 
The current version uses firebase. The `cred.json` isn't located in this repository. 
## Run in console instructions 
After installing run **ConsoleChat.py**.
This will start the backend and allow you to chat with 4 "different" bots.
To switch between bots simply type an integer from 0 to 3. (Ommit any other charecters to switch)

