---
layout: default
title: Game
parent: Interface
nav_order: 2
---
### Classic Mode Gameplay
#### Code Structure
The application is structured into two main parts: `tutorial()` and `game()`.

#### `tutorial()`
This function serves as the introductory guide to the Classic Game mode. It provides an overview of how to play and initiates the game session when the user clicks "Let's Play". Key features include:

- **Custom CSS**: Styles for centering the title.
- **Game Instructions**: Detailed instructions on how to play the Classic Game mode.

##### Breakdown of Function Components:

1. **Custom CSS**:
    - Defines styles for centering the title (`centered-title`).

2. **Tutorial Container**:
    - Displays the title "How to play Classic Mode?" with centered alignment.
    - Provides a detailed guide on how to play the Classic Game mode.
    - Includes a button to start the game, which sets session state variables and triggers a rerun.

#### `game()`
This function represents the core gameplay loop of the Classic Game mode. It manages the interaction between the user, characters (bots), and game mechanics. Here’s a breakdown of its components:

##### CACHING FUNCTIONS

1. **bots_num()**:
    - Returns the number of bots based on the current game level.

2. **additional_personalities()**:
    - Returns a fixed number of additional MBTI personalities to include.

3. **get_data()**:
    - Retrieves data for the current round, including selected characters' names and MBTI types.

4. **init_CM()**:
    - Initializes the ChatManager (CM) instance for managing interactions with characters.

5. **add_names(names)**:
    - Adds default system prompts for characters using the provided names.

6. **shuffle(mbtis)**:
    - Shuffles the list of MBTI types for each round.

##### GAME MECHANICS

1. **update_scoreboard(score, df, user)**:
    - Updates the scoreboard with the player's latest score and stores it in Firebase.

2. **get_all_scores()**:
    - Retrieves all players' scores from Firebase and returns them as a DataFrame.

3. **rerun_level()**:
    - Resets the current game level and prepares new data for the next round.

4. **res_score(score)**:
    - Adjusts the player's score when retrying the level.

##### SESSION STATE MANAGEMENT
- **st.session_state**: Manages game state variables across sessions, including username, score, streak, current level, selected options, and hints.

##### USER INTERFACE SECTIONS

1. **Chat Section**:
    - Displays user information and chat interactions with characters.
    - Allows users to send messages and receive responses from characters.

2. **Bots Section**:
    - Displays available hints and character images.

3. **Guesses Section**:
    - Allows users to select and submit their guesses for the characters' MBTI types.
    - Includes a button to call the Professor for hints and a button to finish the game and submit guesses.

##### Gameplay Flow:

1. **Initialization**:
    - Retrieves initial data and sets up the game state.

2. **Interaction**:
    - Users interact with characters through chat, ask questions, and analyze responses to deduce MBTI types.

3. **Hint Usage**:
    - Users can call the Professor for hints if needed.

4. **Submission**:
    - Users submit their MBTI guesses for each character.
    - The game calculates the score and updates the scoreboard.

5. **Next Round**:
    - Users can proceed to the next round or retry the current level based on their performance.

