""" 
Student Number: 400451088
Full Name: Manav Sharma 
This file showcases the work for assignment 3 of COMPSCI 1MD3.
"""

## Calcualtor function
def calculator():
    print("Welcome to the calculator.")
    currentvalue = 0.0

    while True: # Used so user can quit using break.
        print(currentvalue)
        operation = input("(+)add, (-)subtract, (*)multiply, (/)divide, (C)clear, (Q)quit: ").lower()

        if operation not in ['+', '-', '*', '/', 'c', 'q']:
            print("*** Invalid option ***")
            continue # Skip the rest of the code and restart the loop

        if operation == "q":
            print("Goodbye!")
            break # Exit the loop and end the function

        if operation == 'c':
            currentvalue = 0.0
            continue # Skip the rest of the code and restart the loop

        try:
            number = float(input("Enter a number: "))
        except ValueError:
            print("Invalid number. Try again.")
            continue # Skip the rest of the code and restart the loop

        if operation == "+":
            currentvalue += number
        elif operation == "-":
            currentvalue -= number
        elif operation == "*":
            currentvalue *= number
        elif operation == "/":
            if number != 0:
                currentvalue /= number
            else:
                print("Cannot divide by zero. Try again.")

calculator()



## Converter
def convert_base(d, b):
    if b < 2 or b > 36: # Base needs to be > 2 and < 36
        return False
    
    if d == 0:
        return '0'

    s = ''

    # Convert digits greater than 9 to characters
    def to_char(n):
        if n < 10:
            return str(n)
        else:
            return chr(ord('A') + n - 10)

    # Iterate until d becomes 0
    while d:
        # Get the next digit
        digit = d % b
        # Convert the digit to character
        char_digit = to_char(digit)
        # Add to the left side of s
        s = char_digit + s
        # Update d
        d //= b
    
    return s

print(convert_base(10, 2))  # Output: 1010
print(convert_base(30, 16)) # Output: 1E
print(convert_base(100, 8)) # Output: 144
print(convert_base(255, 16)) # Output: FF
print(convert_base(0, 2)) # Output: 0
print(convert_base(12345, 7)) # Output: 50664
print(convert_base(100, 1)) # Output: False
print(convert_base(100, 37)) # Output: False
print(convert_base(2, 2)) # Output: 10


