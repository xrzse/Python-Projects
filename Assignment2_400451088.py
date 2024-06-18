""" 
Student Number: 400451088
Full Name: Manav Sharma 
This file showcases the three games for assignment 2 of COMPSCI 1MD3.
"""
'''
'''

import random
import time

### Coin Flips Game

Head_or_tail = ["H", "T"]

## Flips coin 10 times and calculates score then returns both the flip results and the score
def play_coin():
    
    flipresult = ""
    score = 0

    for _ in range(10):
        flipresult += random.choice(Head_or_tail)  # Randomly select "H" or "T" for 10 times and concatenate the results
    print(flipresult)

    # If the first flip is tails, the user gets 2 points for every head.
    if flipresult[0] == "T":
        for _ in list(flipresult):
            if _ == "H":
                score += 2
            else:
                score += 0

    # If the first flip is heads, the user gets one point for every tail.
    else:
        for _ in list(flipresult):
            if _ == "T":
                score += 1
            else:
                score += 0
    return flipresult, score

### Number Guess

## Takes in user's guess and sums two dice rolls, rewards user depending on how close their guess is to the sum.
def play_number_guess(guess):
    sumdiceroll = 0
    for _ in range(2):
        sumdiceroll += random.choice(range(1,7))  # Randomly takes a number from all possible dice rolls (1 to 6)
    
    if guess == sumdiceroll:
        points = 10
    elif abs(guess - sumdiceroll) <= 2:
        points = 5
    else: 
        points = 0
    
    return sumdiceroll, points  # Returns both sumdiceroll and points

### Rock Paper Scissors Lizard Spock
moveset = [" ", "Rock", "Paper", "Scissor", "Lizard", "Spock"]

## Function that plays RPSLS against computer.
def play_rpsls(move):
    computermove = random.choice(range(1,6))  # Randomly choose a move for the computer

    if move == computermove:
        rpsls_points = 5
        
    elif (move == 1 and computermove in [3, 4]) or \
        (move == 2 and computermove in [1, 5]) or \
        (move == 3 and computermove in [2, 4]) or \
        (move == 4 and computermove in [2, 5]) or \
        (move == 5 and computermove in [1, 3]):
            rpsls_points = 10
    else:
        rpsls_points = 0
        
    return computermove, rpsls_points


### The Games Room

## Function to choose and play a game, keeps track of the total score
def games_room():
    total_score = 0
    coinflips = ["coin flip", "coinflip", "flipcoin", "flip coin"]
    numberguess = ["numberguess", "number guess", "guess number", "guessnumber"]

    print("Games available: \n"
          "- Coin Flip \n"
          "- Number Guess \n"
          "- Rock Paper Scissors Lizard Spock (RPSLS)")
    time.sleep(1)

    for _ in range(n):
        which_game = input("What game do you want to play?: ").lower()

        if which_game in coinflips:
            flipresult, score = play_coin()
            print("Coin Flips Game Result: " + flipresult + " = " + str(score) + " points")
            total_score += score

        elif which_game in numberguess:
            guess = int(input("Enter your guess: "))
            sumdiceroll, points = play_number_guess(guess)
            print("Number Guess: " + str(guess) + ", Actual result: " + str(sumdiceroll) + ", Points: " + str(points))
            total_score += points

        else:
            move = int(input("Enter your move number, Rock(1), Paper(2), Scissor(3), Lizard(4), Spock(5): "))
            computermove, rpsls_points = play_rpsls(move)
            print("RPSLS: Player move: " + moveset[move] + ", Computer move: " + moveset[computermove] + ", Points: " + str(rpsls_points))
            total_score += rpsls_points
        
        time.sleep(1)

    return total_score

n = int(input("How many games do you want to play?: "))
finalscore = games_room()
print("Your final points are: " + str(finalscore))