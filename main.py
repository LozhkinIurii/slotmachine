MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

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
        amount = input("How much would you like to bet on each line (1$ - 100$)?: ")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                return amount
            else:
                print(f"Bet must be in valid range ({MIN_BET}$ - {MAX_BET}$).")
        else:
            print("Plese, enter a valid number.")


def main():
    balance = deposit()
    lines = get_number_of_lines()
    bet = get_bet()
    total_bet = lines*bet
    print(f"Your bet is {bet}$ on {lines} lines. Total bet: {total_bet}$.")
    print(f"Your balance: {balance}$.")


main()