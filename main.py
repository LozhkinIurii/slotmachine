def deposit():
    while True:
        amount = input("You deposit in $: ")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                return amount
            else:
                print("Amount must be greater than zero!")
        else:
            print("Plese, enter a valid number.")

deposit()

def main():
    balance = deposit()


main()