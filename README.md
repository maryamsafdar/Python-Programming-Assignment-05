# High-Low Game

## Overview

The High-Low game is a simple Python game designed to help you gain more experience with control flow and Boolean logic in Python. The game consists of multiple rounds where you will guess whether your randomly generated number is higher or lower than a randomly generated number for the computer. If your guess is correct, you earn a point!

## How to Play

1. **Two Numbers**: Each round, two random numbers between 1 and 100 are generated—one for you and one for the computer.
2. **Make a Guess**: You can see your number but not the computer's. You will guess whether your number is higher or lower than the computer's.
3. **Scoring**: If your guess is correct, you get a point. If not, you don't get a point. The game continues for a specified number of rounds.
4. **Winning**: At the end of all rounds, you will be given a score and a message based on your performance.

## Features

- **Random Number Generation**: The game generates random numbers for both the player and the computer.
- **User Input**: The player is prompted to guess if their number is higher or lower than the computer's.
- **Game Logic**: The game checks if the player's guess is correct and awards points accordingly.
- **Multiple Rounds**: The game plays for a fixed number of rounds, with the score updated after each round.
- **Input Validation**: The game ensures that the player's input is valid (`higher` or `lower`).
- **Conditional Ending Messages**: Based on the player's score, the game provides different ending messages.

## Requirements

- Python 3.x

## How to Run

1. Clone or download this repository.
2. Navigate to the directory containing the game script.
3. Run the game script using Python:

   ```bash
   python high_low_game.py
