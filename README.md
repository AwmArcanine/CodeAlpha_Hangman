# CodeAlpha_Hangman
This is a simple implementation of the classic Hangman game written in Python. The player tries to guess a randomly selected word by suggesting letters one at a time. The player has a limited number of lives (6) to guess the word correctly.

📋 How to Play
A random word is selected from a predefined list.
The word is hidden using underscores (_), one for each letter.
You guess one letter per turn.
If the letter is correct, it's revealed in its correct position(s).
If the guess is incorrect, you lose a life.

The game ends when:
You guess the entire word correctly (Win), or
You run out of lives (Lose).

🔁 Game Loop Behavior
Repeated guesses are ignored with a warning.
The number of remaining lives is displayed after each incorrect guess.
Correct letters accumulate and update the display progressively.

📝 Notes
Word list: ['havana', 'banana','scenario','purple','elizabeth']
Initial lives: 6
Input is case-insensitive.
No external dependencies required.

▶️ To Run
Make sure you have Python installed. Save the code in a .py file and run it from your terminal.
