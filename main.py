
import random
from unittest import result


print('Welcome to Rock, Paper, Scissors')
print('R for Rock, P for Paper, S for Scissors')
gameOver = False

while gameOver is False:
    choices = ['r', 'p', 's']


    computer = random.choice(choices)
    player = None

    while player not in choices:
        player = input('r, p or s?:').lower()

    if player == computer:
        gameOver == False
        print("player(%s) : computer (%s)" %(player, computer))
        print("Tie")
    elif player == "r":
        gameOver == True
        if computer == 'p':
            print("player (%s) : computer (%s)" %(player, computer))
            print("You lose!!")
            break
        if computer == 's':
            print("player (%s) : computer (%s)" %(player, computer))
            print("You Win!!")
            break
    elif player == "p":
        gameOver == True
        if computer == 'r':
            print("player (%s) : computer (%s)" %(player, computer))
            print("You Win!!")
            break
        if computer == 's':
            print("player (%s) : computer (%s)" %(player, computer))
            print("You Lose!!")
            break
    elif player == "s":
        gameOver == True
        if computer == 'r':
            print("player (%s) : computer (%s)" %(player, computer))
            print("You Lose!!")
            break
        if computer == 'p':
            print("player (%s) : computer (%s)" %(player, computer))
            print("You Win!!")
            break
