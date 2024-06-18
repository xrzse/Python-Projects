import random
def lefunc(a,n):
    lecount = 0
    numerror = 0
    for l in a:
        if len(l) > n:
            a[lecount] = "ERROR"
            numerror += 1
        lecount+=1
    return a

for zxw in range(10):
    lofalps = []
    for idx in range(100):
        alp = "abcdefghijklmnopqrstuvwxyz"
        temp = ""
        for a in range(random.randint(1,8)):
            zz = random.choice(alp)
            temp += zz
        lofalps.append(temp)
    print(lefunc(lofalps,random.randint(1,6)))





    
print(lefunc(a,4))