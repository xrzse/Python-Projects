Z = []
def number_check(L):
    for x in L:

        if x < 1:
            Z.append("Low")
        if x > 10:
            Z.append("High")
        else:
            Z.append("Normal")
    
    print(Z)

typelist = [2,4,5,6,2,1,23,43,34,-329,-1]

number_check(typelist)

