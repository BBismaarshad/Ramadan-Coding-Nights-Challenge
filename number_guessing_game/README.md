# Number Guessing Game

A simple Python-based number guessing game where the player has 5 attempts to guess a randomly generated number between 50 and 100.

## How to Play

1. The game will generate a random number between 50 and 100 (inclusive)
2. You have 5 attempts to guess the correct number
3. After each guess, the game will tell you if your guess was:
   - Too high
   - Too low
   - Correct (if you guessed the number)
4. If you don't guess the number within 5 attempts, the game will reveal the correct number

## Features

- Simple and intuitive gameplay
- Clear feedback after each guess
- Tracks number of attempts used
- Random number generation ensures a different challenge each time

## Requirements

- Python 3.x
- Random module (comes with Python standard library)

## How to Run

1. Save the code as `number_guessing_game.py`
2. Open a terminal/command prompt
3. Navigate to the directory containing the file
4. Run the command: `python number_guessing_game.py`

## Code Overview

- Uses `random.randrange()` to generate the target number
- Implements a while loop to handle up to 5 guesses
- Provides feedback after each guess
- Shows the correct number if all guesses are used

Enjoy the game! Try to guess the number in as few attempts as possible.
