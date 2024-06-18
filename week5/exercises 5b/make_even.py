def make_even(a):
    newa = []
    for i in a:
        if i%2!=0:
            newa.append(i+1)
        else:
            newa.append(i)
    print(newa)

def sumColumn(a, col):
    sumofcols = 0
    for obj in a:
        objlist = list(str(obj))
        sumofcols += int(objlist[col])
    print(sumofcols)

a = [143,223,323,322,374,263,273,462]
make_even(a)
sumColumn(a,2)

    