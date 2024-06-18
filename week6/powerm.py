def power(m,n):
    if m**n == 1:
        return 1
    else:
        return m * power(m,n-1)




print(power(5,21))
print(5**21)