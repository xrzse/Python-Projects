def passrecur():
    password = input("Enter a password: ")
    passwordverification = input("Enter password again: ")
    #Base case
    if password == passwordverification and len(password) >= 8:
        return password
    else:
        print("No good")
        return passrecur()

print(passrecur())
