origlist = [45, 76, 34, 55]
print(origlist * 3) #[45, 76, 34, 55, 45, 76, 34, 55, 45, 76, 34, 55]

newlist = origlist * 3 #[45, 76, 34, 55, 45, 76, 34, 55, 45, 76, 34, 55]
print(newlist)
newlist = [origlist] * 3 #Creates a new list with three lists in it, all three lists are referencing back to origlist
print(newlist) #[[45, 76, 34, 55], [45, 76, 34, 55], [45, 76, 34, 55]]

origlist[1] = "kaBoom"

print(newlist) #As you can see newlist will also change since newlist is referencing back to origlist.