---
layout: default
title: App
parent: Interface
nav_order: 1
---

### Who am I?

This project is a Streamlit-based web application titled "Who am I?". It includes several features and functionalities aimed at interactive user engagement. App.py contains all of the key data to manage gameplay.

#### Initialization and Setup

1. **Imports and Initialization**: 
   - It imports necessary modules from Streamlit (`streamlit`), local modules (`utilis`, `game`, `help`, `about`, `streak`), and external libraries (`pandas`, `firebase_admin`).
   - Initializes Firebase Admin for database operations.

2. **Session State Initialization**:
   - Sets up various session state variables using `st.session_state` to manage user sessions and game states. These variables include `username`, `window`, `start`, `text`, `lvl`, `research`, `level`, `gamemode`, `logged_in`, `data`, `data_streak`, `score`, `score2`, `streak_classic`, `streak_streak`, `curr_lvl`, `current_lvl`, `hints_classic`, `hints_streak`, `tries`, `guesses2`, `botsStreakList`, `allMbti`, `tutorial_classic`, and `tutorial_streak`. These are used to store user-specific data and game progress.

#### User Interface and Functionality

3. **Main Function (`main()`)**:
   - Configures the Streamlit page layout and settings (`st.set_page_config`).
   - Initializes graphical elements (`add_logo`, `background`, `container_bg`) using utility functions from `utilis`.

4. **Login Function (`login()`)**:
   - Manages user authentication with Firebase.
   - Allows users to log in with a username and password.
   - Creates a new account if the username doesn't exist.
   - Updates session state upon successful login.

5. **Start Function (`start()`)**:
   - Manages the start-up sequence of the application.
   - Allows users to input their name and begin interactions with the virtual assistant ("Professor").
   - Provides options to choose game difficulty levels (Easy, Medium, Hard).
   - Initiates classic research or streak game based on user selection.

6. **Management Function (`manage()`)**:
   - Routes the application flow based on `st.session_state.window`:
     - Directs to game tutorials or gameplay (`game` or `streak` modules).
     - Displays help information (`help` module).
     - Shows application introduction (`start()`), about information (`about`), or other functionalities based on user interaction.

#### Sidebar and User Interaction

7. **Sidebar**:
   - Provides interactive buttons for users:
     - Classic Game, Streak Challenge, Help from Professor, Restart Research, About Us.
   - Updates `st.session_state.window` based on user selection to manage application state and flow.

#### Conclusion

This readme provides an overview of the functionality and structure of the "Who am I?" Streamlit application code. It integrates Firebase for user authentication and data storage, uses Streamlit for the web interface, and includes modular components for different game modes and user interactions.
