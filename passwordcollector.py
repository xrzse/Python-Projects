import random

all_characters = (
    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
    'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
    'U', 'V', 'W', 'X', 'Y', 'Z',
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
    'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
    'u', 'v', 'w', 'x', 'y', 'z',
    '!', '@', '#', '$', '%', '^', '&', '*', '(', ')',
    '-', '_', '+', '=', '[', ']', '{', '}', '|',
    ';', ':', "'", '"', ',', '.', '<', '>', '/', '?',
    '`', '~'
)

def passcol():
    random_pass = random.sample(all_characters, 12)
    random_passw = ''.join(random_pass)
    print("Your random password is" + random_passw)
    title = input("Now give a name to that password to remember it by: ")
    with open('passes.txt', 'a+') as file:
        file.write(random_passw + "|" + title +"\n")
passcol()