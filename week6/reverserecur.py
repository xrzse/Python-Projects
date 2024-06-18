def reverserecur(a):
    if a == []:
        return []
    else:
        head = a[0]
        tail = a[1:]
        return reverserecur(tail) + [head]

print(reverserecur([1,2,3,4,3,3,2,1,2,3,32,2]))