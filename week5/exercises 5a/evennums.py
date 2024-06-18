def sumEven(lst):
    countleeven = [i for i in lst if abs(i) % 2 == 0]
    summedupeven = 0
    for i in countleeven:
        summedupeven += i
    return summedupeven

print(sumEven([1,23,2,43,4,3,42,424,2,344,23,2]))

