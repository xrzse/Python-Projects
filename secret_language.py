import time

encry = ("1","encrypt","en") # Elements that activate encryption
decry = ("2","decrypt","de") # Elements that activate decryption

alphabet = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',' ')
special_ = ('@', '#', '$', '!', '%', '&', '*', '(', ')', '[', ']', '{', '}', '<', '>', '|', '^', '`', '~', '+', '=', '-', '_', ':', ';', ',','.')

def intro(): # Introduction function, also used as fallback if an error occurs.
    decrypt_or_encrypt = input("Would you want to encrypt(1) or decrypt(2) your text?: ").lower()

    if decrypt_or_encrypt in decry:
        cryptiontxt = input("Input the text: ").lower()
        decrypter(cryptiontxt)

    elif decrypt_or_encrypt in encry:
        cryptiontxt = input("Input the text: ").lower()
        encrypter(cryptiontxt)

    else:
        intro()

def encrypter(var):
    list_var = list(var) # Makes inputted text into a list for mutation purposes
    cryptedstr = "" # Empty string to add to the mutated text
    try:
        for vr in list_var: # Goes through every element in the list one by one
            indx = alphabet.index(vr) # Finds the index of the element in alphabet list
            switcharoo = special_[indx] # Then replaces with the same index from the special_ list
            cryptedstr += switcharoo # Joins each instance together
        print("Your encrypted text is: "+cryptedstr) 
    except: # Incase error occurs it fallsback
        print("Unable to encrypt given text, please try again.")
        time.sleep(1) # For fun
        intro()

def decrypter(var):
    list_var = list(var) # Makes inputted text into a list for mutation purposes
    cryptedstr = ""  # Empty string to add to the mutated text
    try:
        for vr in list_var: # Goes through every element in the list one by one
            indx = special_.index(vr) # Finds the index of element in special_ list
            switcharoo = alphabet[indx] # Then replaces with the same index from the alphabet list
            cryptedstr += switcharoo # Joins each instance together
        print("Your encrypted text is: "+cryptedstr)
    except: # Incase error occurs it fallsback
        print("Unable to encrypt given text, please try again.")
        time.sleep(1) # For fun
        intro()
intro()
