
# 📘 Assignment: Hangman Game Challenge

## 🎯 Objective

Build a terminal-based Hangman game in Python. Students will practice string manipulation, loops, conditionals, and simple input validation by implementing the game loop and a user-facing command-line interface.

## 📝 Tasks

### 🛠️ Implement Hangman Core

#### Description
Write the main Hangman program that runs in the terminal. The program should pick a secret word, accept single-letter guesses from the player, reveal letters as they are correctly guessed, and track the number of remaining incorrect attempts.

#### Requirements
Completed program should:

- Randomly select a word from a predefined list (list can be defined in the script).
- Prompt the player for single-letter guesses and validate input (ignore empty input, multiple characters, and non-letters).
- Display the current progress using underscores for unknown letters (e.g., `_ _ a _ _`).
- Keep and display a list of already-guessed letters and the number of incorrect attempts remaining.
- End the game and display a clear win message if the word is fully guessed, or a lose message when attempts are exhausted (reveal the word on loss).
- Provide a simple command-line interface using `input()` and `print()` so the game runs without extra setup.

Example interaction (simplified):

```
Word: _ _ _ _ _
Guessed: a, e
Attempts remaining: 4
Enter a letter: r
Correct! Word: _ r _ _ _
```

### 🛠️ Optional Enhancements

#### Description
After completing the core game, students may add one or more enhancements to make the game more polished or feature-rich.

#### Requirements (choose any)

- Add ASCII-art stages for the hangman that update with each incorrect guess.
- Load the word list from an external text file (e.g., `words.txt`) instead of a hardcoded list.
- Allow the player to guess the full word as an alternate action.
- Add a replay option so the player can play multiple rounds without restarting the script.
- Keep a simple high-score or win/loss count across a session.

Tip: A starter file `starter-code.py` is included to help you get started. Keep your solution simple and well-commented so other students can read and learn from it.
