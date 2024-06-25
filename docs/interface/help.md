---
layout: default
title: Help Page
parent: Interface
nav_order: 3
---
### Help Page
#### Code Structure
The application is structured into a single main function: `help()`.

#### `help()`
This function is responsible for displaying the "Help" page. It provides useful information about MBTI personality types and a list of known characters with their corresponding MBTI types. Key features include:

- **Custom CSS**: Adjusts the layout by removing space.
- **MBTI Database Display**: Shows a table of MBTI types and their descriptions.
- **Celebrities Database Display**: Shows a table of known characters and their MBTI types.

##### Breakdown of Function Components:

1. **remove_space()**:
    - Called at the beginning to remove space in the user interface.

2. **Help Container**:
    - Contains two main sections: MBTI Database and Celebrities Database.

##### Detailed Components:

1. **MBTI Database**:
    - Loads data from `mbti_data.json`, which contains descriptions and names of the 16 MBTI personality types.
    - Displays the data in a table format with columns for "MBTI Type" and "Description".

2. **Celebrities Database**:
    - Loads data from `data.json`, which contains names of known characters and their MBTI types.
    - Displays the data in a table format with a column for "Name".

