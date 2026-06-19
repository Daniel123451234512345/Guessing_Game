# Number Guessing Game 🎲

A terminal-based number guessing game where you race against the clock to match wits with the computer.

## Solution for the https://roadmap.sh/projects/number-guessing-game challenge

![Build Status](https://img.shields.io/badge/build-passing-brightgreen) ![Version](https://img.shields.io/badge/version-1.0.0-blue) ![License](https://img.shields.io/badge/license-MIT-green)

## Demo

Upon starting, you'll be prompted to choose a difficulty level. The computer then secretly picks a number between 1 and 100. As you input guesses, the terminal will immediately feedback whether your guess is too high or too low, while keeping a strict countdown of your remaining attempts.

## Features

- **3 Difficulty Modes:** Choose between Easy (10 attempts), Medium (5 attempts), or Hard (3 attempts)
- **Smart Hints:** Get "too high" or "too low" feedback after every guess to narrow down the answer
- **Input Validation:** Robust handling for non-numeric entries and out-of-range numbers
- **Warning System:** Special alert when you are down to your very last attempt
- **Replayability:** Instantly restart the game without relaunching the script

## Prerequisites

- Python 3.x

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/guessing-game.git
   ```
2. Navigate to the project directory:
   ```bash
   cd guessing-game
   ```

## Usage

Run the game script from your terminal:

```bash
python3 game.py
```

Follow the interactive prompts to choose your difficulty and start guessing:

```text
----------------------------------------------------------------------------------------------------
Welcome to the Number Guessing Game

Intro:
 -   1. Guess a number between 1-100
 -   2. You will have a certain amount of guesses depending on the difficulty you choose
 -   3. You will get hints as you keep guessing
----------------------------------------------------------------------------------------------------
Which difficulty would you like to attempt: easy, medium or hard: hard

You have have chosen difficulty: 3, you have 3 attempts to guess the number, may the odds be in your favor!

What would you like to guess: 50
Your guess was too low
Remaining guesses left: 2
```

## Project URL

https://github.com/Daniel123451234512345/Guessing_Game

## Contributing

We welcome contributions! Feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License.
