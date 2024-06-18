def sumNegatives(lst):
    bukari = [i for i in lst if 1 + i < 1]
    summedneg = 0
    for x in bukari:
        summedneg += x
    
    return summedneg

