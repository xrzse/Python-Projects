def avgrecur(a):
    if a == []:
        return 0
    else:
        head = a[0]
        tail = a[1:]
        return head + avgrecur(tail)





print(avgrecur([1,2,3,3,3,3,3,4,34,43,2,32]))