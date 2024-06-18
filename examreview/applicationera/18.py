def getints(n):
    num = n[-1]
    count = 0
    for z in n:
        if z == num:
            count += 1
    return count


