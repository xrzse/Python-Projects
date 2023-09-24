import time

encry = ("1","encrypt","en")
decry = ("2","decrypt","de")

alphabet = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',' ')
special_ = ('@', '#', '$', '!', '%', '&', '*', '(', ')', '[', ']', '{', '}', '<', '>', '|', '^', '`', '~', '+', '=', '-', '_', ':', ';', ',','.')

def intro():
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
    list_var = list(var)
    cryptedstr = ""
    try:
        for vr in list_var:
            indx = alphabet.index(vr)
            switcharoo = special_[indx]
            cryptedstr += switcharoo
        print("Your encrypted text is: "+cryptedstr)
    except:
        print("Unable to encrypt given text, please try again.")
        time.sleep(1)
        intro()

def decrypter(var):
    list_var = list(var)
    cryptedstr = ""
    try:
        for vr in list_var:
            indx = special_.index(vr)
            switcharoo = alphabet[indx]
            cryptedstr += switcharoo
        print("Your encrypted text is: "+cryptedstr)
    except:
        print("Unable to encrypt given text, please try again.")
        time.sleep(1)
        intro()
intro()