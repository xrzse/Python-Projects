import random
import time
print("Welcome to rock paper scissor")
time.sleep(1)
options = ['rock', 'paper', 'scissor']
def game():
    value = input('Choose between rock/paper/scissor: ').lower()
    if value != 'rock' and value != 'paper' and value != 'scissor':
        game()
    else:
        pass
    time.sleep(1)
    print('rock...')
    time.sleep(1)
    print('paper...')
    time.sleep(1)
    print('scissors!!!')
    time.sleep(0.3)
    rps = random.choice(options)
    print('I got, '+ rps)
    if rps == value:
        print('Aw its a draw!!, retry!')
        game()
    elif rps == 'rock' and value == 'paper' or rps == 'paper' and value == 'scissor' or rps == 'scissor' and value == 'rock':
        print("Oh no, I lost")
        replay = input("Do you wish to play again?: ").lower()
        if replay == "yes":
            game()
        elif replay == "no":
            exit()
    else:
        print("I won")
        replay = input("Do you wish to play again?: ").lower()
        if replay == "yes":
            game()
        elif replay == 'no':
            exit()
game()