from english_words import english_words_set
import random

def game():
    word = random.choice(list(english_words_set)).lower()
    list_letters = list(word)
    list_length = len(list(word))
    blank_list = ["_"] * list_length
    jeez = [""]
    print("Welcome to hangman, you have "+ str(list_length)+ " attempts to guess the word!")

    attempts = []
    x = 0

    while list_length > x:
        print("Enter your attempt " + str(x + 1) + "\n\n")
        print(blank_list)

        guess = input("\n\n: ")
        attempts.append(guess)
        if guess in list_letters:
            print("In list")
            blank_list = [letter if letter in attempts else "_" for letter in list_letters]
            
        elif guess not in list_letters:
            print("Not in list")
            x = x + 1

    playagain = input("Game Over, the word was " + word + " would you like to play again?: ").lower()
    if playagain == "yes":
        game()
game()



    
