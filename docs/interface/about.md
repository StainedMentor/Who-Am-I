---
layout: default
title: About Page
parent: Interface
nav_order: 6
---
### Meet The Creators Page
#### Code Structure
The application is structured into two main parts: `about()` and `utilis`.

#### `about()`
This function is responsible for displaying the "Meet The Creators" page. It provides information about the creators of the application and their roles. Key features include:

- **Custom CSS**: Styles for centering titles and content within containers.
- **Creators and their avatars**: Displaying names, images, and descriptions of the creators.

##### Breakdown of Function Components:
1. **remove_space()**:
   - Called at the beginning to remove space in the user interface.

2. **First Container**:
   - Used to display the "Meet The Creators" title and a button linking to GitHub.

3. **Second Container**:
   - Displays columns with information about each creator.

##### Detailed Components:

1. **Custom CSS**:
    - Defines styles for centering the title (`centered-title`), justifying text (`justify`), and adding borders to columns (`column-border`).

2. **First Container**:
    - **description**: A column containing the main description and title.
        - Sets the title "Meet The Creators" with centered alignment using the `centered-title` CSS class.
    - **media**: A column containing the GitHub button, added via `utilis.github()`.

3. **Second Container**:
    - Divided into four columns, each representing a creator.
    - **creat1 to creat4**: Columns for each creator:
        - **creat1**:
            - Displays the name "StainedMentor" with centered alignment.
            - Displays the avatar using `utilis.avatar("oliver_cyber")`.
            - Provides a detailed description of StainedMentor's role and personality.
        - **creat2**:
            - Displays the name "Agkittens" with centered alignment.
            - Displays the avatar using `utilis.avatar("aga_cyber")`.
            - Provides a detailed description of Agkittens's role and personality.
        - **creat3**:
            - Displays the name "Marlon1385" with centered alignment.
            - Displays the avatar using `utilis.avatar("milosz_cyber")`.
            - Provides a detailed description of Marlon1385's role and personality.
        - **creat4**:
            - Displays the name "SamePinchy" with centered alignment.
            - Displays the avatar using `utilis.avatar("kuba_cyber")`.
            - Provides a detailed description of SamePinchy's role and personality.
