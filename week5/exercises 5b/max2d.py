def max2D(a):
    largestnum = 0
    for row in array:
        for col in row:
            if col > largestnum:
                largestnum = col
    return largestnum



array = [
    [1, 2, 3],
    [4, 32, 6],
    [7, 8, 9]
]

print(max2D(array))