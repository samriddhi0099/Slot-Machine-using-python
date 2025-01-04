# Slot Machine Game

# Overview

This is a simple Python-based slot machine game where players can deposit money, place bets, and spin the reels to win based on matching symbols. The project was created as a hands-on exercise to practice Python programming concepts.

---

# Features

- Deposit System: Users can input an initial deposit to start the game.
- Customizable Bets: Players can choose the number of lines to bet on and the bet amount per line.
- Randomized Spins: Each spin generates random symbols with varying probabilities.
- Winning Calculation: Calculates winnings based on bet amount and matched symbols on specific lines.
- Replay Option: Players can choose to play multiple rounds as long as they have a balance.

---

# Rules

1. Lines: Players can bet on 1 to 3 lines.
2. Symbols: The slot machine uses symbols with different frequencies:
   - `A`: High frequency, high value
   - `B`: Moderate frequency and value
   - `C`: Lower frequency, moderate value
   - `D`: Lowest frequency, highest value
3. Winning Lines: A line wins if all symbols in that line match.

---

# How to Play

1. Clone or download the repository.
2. Run the `main()` function in the Python file to start the game.
3. Follow the prompts:
   - Deposit an amount.
   - Choose how many lines to bet on (1-3).
   - Place a bet per line.
   - Spin the reels and see if you win!
4. Repeat or exit the game.

---

# Gameplay Example:
How much would you like to deposit? $100
Current balance: $100
How many lines would you like to bet on (1 - 3)? 2
How much would you like to bet on each line? $10
YOU ARE BETTING $10 ON 2 LINES.
TOTAL BET IS $20

Slot Machine:
A | B | C
B | B | B
C | D | A

You won $40.
You won on lines: 2
Current balance: $120
Do you want to play again? (y/n): n
You left the game with $120.

---

# Learning Outcomes

This project helped practice:

- Python basics like loops, conditional statements, and functions.
- Dictionary usage for symbol counts and values.
- Randomization using the `random` module.
- Implementing logic for betting systems and user input validation.
