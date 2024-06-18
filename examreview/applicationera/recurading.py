def addrecur(a):
    #Base Case
    if a == 1:
        return 1
    #Recur
    else:
        return a + addrecur(a-1)

def addrecurlist(a):
    if a == []:
        return 0
    else:
        head = a[0]
        tail = a[1:]
        return int(head) + int(addrecurlist(tail))

a = 5
print(addrecurlist(list(range(1,a+1))))



