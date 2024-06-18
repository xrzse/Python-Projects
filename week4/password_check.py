def password_check(password):
    upper = lower = digit = False  # Initialize the flags to False
    
    if len(password) > 8:
        for x in password:
            if x.isupper():
                upper = True
                print("Upper check")
            elif x.islower():
                lower = True
                print("Lower check")
            elif x.isdigit():
                digit = True
                print("Digit check")
                
        if upper and lower and digit:
            return "Password Accepted"
        else:
            print("Invalid password, try again.")
            return password_check(input("Enter a password, with one uppercase, one lowercase and a number: "))
    
    else:
        print("Invalid password, try again.")
        return password_check(input("Enter a password, with one uppercase, one lowercase and a number: "))

print(password_check(input("Enter a password, with one uppercase, one lowercase and a number: ")))
