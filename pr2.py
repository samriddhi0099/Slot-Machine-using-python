import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

# Corrected dictionary syntax
symbol_count = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2,
}

# Define symbol values for winnings
symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2,
}

def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []  # Initialize winning_lines within the function
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)

    return winnings, winning_lines  # Correct return statement placement

def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, count in symbols.items():
        for _ in range(count):
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)  # Append the column to columns list

    return columns  # Return the final list of columns

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:  # Check if it's not the last column
                print(column[row], "|", end=" ")
            else:
                print(column[row], end=" ")
        print()  # Newline after each row

def deposit():
    while True:
        amount = input("How much would you like to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than zero.")
        else:
            print("Please enter a valid number.")
    return amount

def get_number_of_lines():
    while True:
        lines = input("How many lines would you like to bet on (1 - " + str(MAX_LINES) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print(f"Please enter a number between 1 and {MAX_LINES}.")
        else:
            print("Please enter a valid number.")
    return lines

def get_bet():
    while True:
        amount = input("How much would you like to bet on each line? $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}.")
        else:
            print("Please enter a valid number.")
    return amount

def main():
    balance = deposit()
    while True:
        print(f"Current balance: ${balance}")
        lines = get_number_of_lines()
        while True:
            bet = get_bet()
            total_bet = bet * lines

            if total_bet > balance:
                print(f"You do not have sufficient balance.\nYour current balance is: ${balance}")
            else:
                print(f"YOU ARE BETTING ${bet} ON {lines} LINES.\nTOTAL BET IS ${total_bet}")
                break

        slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
        print_slot_machine(slots)
        winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
        balance += winnings - total_bet  # Update balance with winnings and total bet
        print(f"You won ${winnings}.")
        if winning_lines:
            print(f"You won on lines:", *winning_lines)
        else:
            print("No winning lines this time.")

        if balance <= 0:
            print("You ran out of balance. Game over!")
            break

        play_again = input("Do you want to play again? (y/n): ")
        if play_again.lower() != "y":
            print(f"You left the game with ${balance}.")
            break

main()