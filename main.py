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


def main():
    balance = deposit()
    lines = get_number_of_lines()
    print(balance, lines)


main()