listz = [1,2,3,443,54]
print(len(listz)) #len does not start at 0

#therefore to find the last number in the list you can either do listz[-1] or listz[len(listz)-1]

print(listz[-1])
print(listz[len(listz)-1])

alist = ['a', 'b', 'c', 'd', 'e', 'f']
alist[1:3] = ['x', 'y'] #You can use the slice opertator to change values insideof a list
print(alist)
alist[1:3] = [] #Can also just remove em
print(alist)

alist = ['a', 'd', 'f'] 
alist[1:1] = ['b', 'c'] #This squeezes b,c after a into the list without mutating any other values
print(alist)
alist[4:4] = ['e'] #Squeezes in e at the end # 4:4, the first 4 is the 4th value counting up from 0
print(alist)