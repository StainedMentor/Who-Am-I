---
layout: default
title: Streak
parent: Interface
nav_order: 4
---
# Streak Challenge Game Mode

## Code Structure

The application is structured into two main parts: `tutorial()` and `streak()`.

### tutorial()

This function serves as the introductory guide to the game. It provides an overview of how to play and initiates the game session when the user clicks "Let's Play". Key features include:

- Custom CSS to center the game title.
- Explanation of game rules and objectives.
- Button to start the game (`streak()` function).

### streak()

This function represents the core gameplay loop of the Streak Challenge mode. It manages the interaction between the user, characters (bots), and game mechanics. Here's a breakdown of its components:

#### Caching Functions

- **additional_personalities()**: Calculates the number of additional MBTI personalities based on the current game level.
- **get_data()**: Retrieves data for the current round, including the selected character's name, MBTI type, and potential MBTI types to guess.
- **init_CM()**: Initializes the ChatManager (CM) instance for managing interactions with characters.
- **add_names()**: Adds default system prompts for characters.
- **shuffle()**: Shuffles the list of potential MBTI types to guess for each round.

#### Game Mechanics

##### Update and Reset Functions

- **update_scoreboard()**: Updates the scoreboard with the player's latest score.
- **gameOverInfo()**: Displays game over information, including final score and options to retry or view scores.
- **rerun_level()**: Resets the game level and updates scores upon correctly identifying a character's MBTI type.
- **reset_level()**: Resets the game to the initial level and score.

#### Session State Management

- **st.session_state**: Manages game state variables across sessions, including username, score (`score2`), streak (`streak_streak`), remaining tries (`tries`), and selected options (`selected_option_streak`).

#### User Interface Sections

- **Chat Section (chat)**: Handles user interactions with characters, including sending messages and receiving responses.
- **Bots Section (bots)**: Displays hints and character images related to the game.
- **Guesses Section (guesses)**: Allows users to select and submit their guesses for the character's MBTI type.

## Installation and Usage

To run the Streak Challenge game mode:

### Requirements

Ensure Python is installed along with required dependencies (`streamlit`, `pandas`, `firebase-admin`, `streamlit_modal`).

### Setup

1. Clone the repository containing the game code.
2. Install dependencies using `pip install -r requirements.txt`.

### Run Application

Execute `streamlit run your_app_name.py` in your terminal to start the application locally.

## Additional Features

- **Firebase Integration**: Utilizes Firebase Realtime Database to store and retrieve player scores (`score_streak`).
- **Dynamic Difficulty**: Adjusts game difficulty based on player progress, enhancing the challenge as the game proceeds.
