l= [1,2,3,4,4,5]
z = [332,3232,323,32,334,232,323,234]
xx = []

for i in zip(l,z):
    xx.append(i[1])
    xx.append(i[0])
    
print(xx)