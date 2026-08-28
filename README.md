# Blackjack

A terminal-based blackjack game built in Python as a learning project.

## Features

- Builds and shuffles a standard 52-card deck
- Deals separate player and dealer hands without duplicate cards
- Hides the dealer's second card until the round is complete
- Supports player hit and stand actions with validated input
- Calculates number-card and face-card values
- Correctly adjusts one or more Aces between 11 and 1
- Makes the dealer draw until reaching at least 17
- Detects busts, wins, losses, and ties
- Starts a fresh round when the player chooses to play again

## Requirements

- Python 3

The game uses only Python's standard library, so no third-party packages are
required.

## Run the Game

From the project directory:

```bash
python3 blackjack.py
```

Enter `h` to hit or `s` to stand. After the result is announced, enter `y` to
play another round or `n` to exit.

## Version 1 Rules

- One player competes against a computer-controlled dealer.
- A fresh shuffled deck is created for every round.
- Number cards use their printed values.
- Jacks, Queens, and Kings count as 10.
- Aces count as 11 unless reducing an Ace to 1 is necessary to avoid a bust.
- The dealer draws below 17 and stands on all totals of 17 or more.
- A hand above 21 busts.
- If neither hand busts, the higher total wins; equal totals tie.

## Project Structure

- `blackjack.py` — the playable game
- `learning.py` — a short exercise on moving cards between collections
- `LEARNING_STYLE.md` — learning goals and tutoring preferences
- `BLACKJACK_PROJECT.md` — the original development roadmap

## What I Practiced

- Designing functions with focused responsibilities
- Passing values between cooperating functions
- Distinguishing arguments, parameters, local variables, and return values
- Managing a deck and multiple hands as interacting collections
- Mutating lists while preserving the correct data shape
- Representing cards with tuples
- Using nested loops to construct a complete deck
- Calculating totals with dictionaries, accumulators, and Ace adjustment
- Building player and dealer loops with clear stopping conditions
- Separating one-round logic from whole-game orchestration
- Debugging by tracing which line changes each piece of state

## Current Scope

Version 1 focuses on the core hit-or-stand game. It intentionally does not
include betting, bankroll tracking, splitting, doubling down, insurance,
surrender, or special blackjack payouts.

Possible future additions include:

- Betting and bankroll tracking
- Natural blackjack detection and 3:2 payouts
- Double-down and split actions
- Win/loss statistics
- Improved card and table formatting
