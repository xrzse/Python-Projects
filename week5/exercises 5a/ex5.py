slist = [1,3,5,10,3,4,5,6]
for x in slist:
    if x % 2 ==0:
        indexofx = slist.index(x)
        slistnew = slist[:indexofx]
        summeds= 0
        for z in slistnew:
            summeds += z
        print(summeds)
        break

print("\n\n\n\n")
bigval = 0
slist = [1,3,5,10,3,4,5,6]
for x in slist:
    if x > bigval:
        bigval = x
print(bigval)
    
