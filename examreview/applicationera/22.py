def functake(a):
    biggestnum = 0
    for row in a:
        for colchk in row:
            if colchk > biggestnum:
                biggestnum = colchk
    
    i = 1
    j = 1
    for row in a:
        for knd in row:
            j +=1
            if knd == biggestnum:
                return ("row: " +str(i) +", column: "+str(j))
        j = 0
        i+=1

    
a = [[1,2,4,5,6],
     [3,4,433,3,4],
     [5,3,54,3,6]]
print(functake(a))