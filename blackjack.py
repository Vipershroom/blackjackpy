import random

def cardDealer():
    num = random.randint(1, 13)
    return num

cards = []
gameStarted = False


print("Hello, welcome to my Blackjack game!") 

running = True
while running:
    if gameStarted == False:
        cards.append(cardDealer())
        cards.append(cardDealer()) 
        gameStarted = True
    print(f"You're cards are {cards}. Your sum is {sum(cards)}")
    
    if sum(cards) < 21:
        print("Do you want to hit? Y/N")
        a = input()
        if a.lower() == 'y':
            cards.append(cardDealer())
            print(f"Your cards are {cards}.Your current amount is {sum(cards)}")
    elif sum(cards) == 21:
        print(f"Your cards are {cards}.Card amount is {sum(cards)}")
        print("You Win Congratulations!")
        
        print("Do you want to play again? Y/N")
        response = input()
        if response.lower() == "n":
            running = False
    else:
        print(f"Your cards are {cards},Card amount is {sum(cards)}")
        print("You lose, sad!")
        
        print("Do you want to play again? Y/N")
        response = input()
        if response.lower() == "n":
            running = False
        else:
            gameStarted = False
            cards = []
    
    
        
        






