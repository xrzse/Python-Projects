def string_reverser(string):
    reversedstring = ""
    for x in string:
        reversedstring = x + reversedstring 
    return reversedstring


print(string_reverser(string=input("enter string: ")))