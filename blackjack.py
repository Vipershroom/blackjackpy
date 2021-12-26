import random

def cardDealer():
    num = random.randint(1, 14)
    return num

print("Hello, welcome to my Blackjack game!")

cardAmount = 0

print(f"You're number is currently {cardAmount}")

if cardAmount < 21:
    print("Do you want to hit? Y/N")
    a = input()
    if a.lower() == 'y':
        cardAmount += cardDealer()






