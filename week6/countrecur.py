def count(start,end,step):
    #Base statement
    print(start)
    if start + step > end:
        lisdsa.extend([start])
        return lisdsa
    else:
        lisdsa.extend([start])
        return count(start+step,end,step)



lisdsa = []

print(count(12,20,3))