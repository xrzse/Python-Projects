def countOdd(lst):
    oddnumsfr = [i for i in lst if i%2 != 0]
    countofods = len(oddnumsfr)
    return countofods

print(countOdd([1,23,4,523,23,42,43,2]))