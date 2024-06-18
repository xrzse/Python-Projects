def recursivefib(n):
    # Base cases
    if n == 0:
        return 0
    elif n == 1:
        return 1
    # Recursive case
    else:
        return recursivefib(n - 1) + recursivefib(n - 2)

# Test the function
print(recursivefib(7))  # Should return 13
