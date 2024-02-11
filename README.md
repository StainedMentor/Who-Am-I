# Who-Am-I
## Description
Who Am I is a game about scientist assistant journey in a robots' lab. The journey begins with a short story and selecting difficulty level, then all 16 MBTI types are introduced to us with hort description. Next, the game begins. We (scientist assistants) must match all bots to MBTI personalities. We do our research with talking to each bot, getting to know them, asking questions which may lead to personality traits connected to pecific MBTI type. The research is done when we match all bots with avaible MBTI types, then results from the scientist come.

## The game
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
* After clicking "Finish research" button, user gets his resukts in %.\
  \
![game](https://github.com/StainedMentor/Who-Am-I/blob/main/assets/game.png)

### Help
![help](https://github.com/StainedMentor/Who-Am-I/blob/main/assets/help.png)
  

## Installation
After cloning the repository and installing requirement, download and add the model to the projects directory: https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGUF/resolve/main/llama-2-7b-chat.Q4_K_M.gguf?download=true

After installing requirements, change the config file in  `~/.streamlit/config.toml.` directory.

On mac everything should work out of the box. If you are working on windows llama-cpp-python installs a CPU only version, which is extremely slow for this project. You can reinstall this package with the following command to use hardware acceleration:
```
CMAKE_ARGS="-DLLAMA_CUBLAS=on"  pip install llama-cpp-python --upgrade --force-reinstall --no-cache-dir
```
If there are further issues this guide should fix them. https://medium.com/@piyushbatra1999/installing-llama-cpp-python-with-nvidia-gpu-acceleration-on-windows-a-short-guide-0dfac475002d

## Run graphical interface
After finishing the installation run in the projects directory this command:
```
streamlit run interface/app.py
```
This should open autmatically in your browser. If not it would display a link in the console
### Run in console instructions 
Note this has wrong import paths due to streamlit and would need to be changed in order to run

After installing run **ConsoleChat.py**.
This will start the backend and allow you to chat with 4 "different" bots.
To switch between bots simply type an integer from 0 to 3. (Ommit any other charecters to switch)

