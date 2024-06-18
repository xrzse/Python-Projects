def factorial(n):
    #Base care
    if n <= 1:
        return 1 #here there is no factorial(n-1 so it returns a 1 which then the function goes back and solves all the waiting n's)
    else:
        return n * factorial(n-1) # the n stays here waiting for factorial(n-1) to compute and so on...

print(factorial(9))