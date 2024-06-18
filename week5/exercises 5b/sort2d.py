def sort2D(a):
    newarray = []
    for row in a:
        for col in row:
            newarray.append(col)
    print(newarray)
    newarray.sort()
    print(newarray)
    newarrarypt2 = [newarray[x:x+3] for x in range(0,len(newarray),3)]
    return newarrarypt2


array = [
    [1, 2, 3],
    [4, 32, 6],
    [7, 8, 9]
]
print(sort2D(array))