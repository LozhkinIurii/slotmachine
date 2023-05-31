#!/usr/bin/env python3

from functions import deposit, spin


def main():
    balance = deposit()
    while True:
        answer = input("Press ENTER to spin('q' to quit):")
        if answer == "q":
            break
        balance = spin(balance)
        print(f"You have ${balance} left.")
        if balance == 0:
            answer = input("Do you want to deposit more money (y|n): ")
            if answer == "y":
                balance += deposit()
                print(f"Your balance: ${balance}.")
            else:
                print("You will be luckier next time!")
                break


main()