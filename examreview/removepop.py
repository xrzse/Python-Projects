print("Remove***")
a = [4,534,23,2,42]
print(a)
a.remove(2) #.remove removes the given value not the given index
print(a)

print("\n\nPop***")
a = [4,534,23,2,42]
print(a)
a.pop(1) #.remove removes the given value not the given index
print(a)

#Remove second int 2 diff ways from a
a = [4,534,23,2,42]

#method 1:
a.pop(1)
print(a)

#method 2:
a = [4,534,23,2,42]
del a[1]
print(a)