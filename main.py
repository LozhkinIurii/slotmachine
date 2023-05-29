import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1
ROWS = 5
COLS = 3

symbols = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8,
}

def spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbols_count in symbols.items():
        for _ in range(symbols_count):
            all_symbols.append(symbol)
    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)
    return columns


def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, col in enumerate(columns):
            if i != len(columns)-1:
                print(col[row], end=" | ")
            else:
                print(col[row])



def deposit():
    while True:
        amount = input("Enter your deposit in $: ")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                return amount
            else:
                print("Amount must be greater than zero.")
        else:
            print("Plese, enter a valid number.")


def get_number_of_lines():
    while True:
        lines = input("Enter number of lines to bet on (1-" + str(MAX_LINES) + "): ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                return lines
            else:
                print("Enter a valid number of lines.")
        else:
            print("Plese, enter a valid number.")

def get_bet():
    while True:
        amount = input("How much would you like to bet on each line ($1 - $100)?: ")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                return amount
            else:
                print(f"Bet must be in valid range (${MIN_BET} - ${MAX_BET}).")
        else:
            print("Plese, enter a valid number.")


def main():
    balance = deposit()
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines
        if total_bet > balance:
            print(f"You do not have enough money to bet that amount. Your current balance: ${balance}.")
        else:
            break
    print(f"Your bet is ${bet} on {lines} lines. Total bet: ${total_bet}.")
    print(f"Your balance: ${balance}.")
    slots = spin(ROWS, COLS, symbols)
    print_slot_machine(slots)


main()