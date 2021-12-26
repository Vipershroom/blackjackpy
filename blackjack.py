import random

def cardDealer():
    num = random.randint(1, 13)
    return num

print("Hello, welcome to my Blackjack game!")

cardAmount = 0

print(f"You're number is currently {cardAmount}")

running = True
while running:
    if cardAmount < 21:
        print("Do you want to hit? Y/N")
        a = input()
        if a.lower() == 'y':
            cardAmount += cardDealer()
            print(f"Your current amount is {cardAmount}")
    elif cardAmount == 21:
        print(f"Card amount is {cardAmount}")
        print("You Win Congratulations!")
        
        print("Do you want to play again? Y/N")
        response = input()
        if response.lower() == "n":
            running = False
    else:
        print(f"Card amount is {cardAmount}")
        print("You lose, sad!")
        
        print("Do you want to play again? Y/N")
        response = input()
        if response.lower() == "n":
            running = False
    
    
        
        






