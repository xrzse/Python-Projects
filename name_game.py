import random
def name_game(name):
    choice = random.choice(range(1,11))
    if choice in range(1,4):
        print(name + " Is my fav name")
    else:
        print("I dont like the name "+ name)

name_game("Sam")

