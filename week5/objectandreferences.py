a = "banana"
b = "banana"

print(a is b) #True since strings are immutable

a = [1,2]
b = [1,2]

print(a is b) #False since lists are mutable and those two lists have different values within memory
print(a == b) #True since they share the same integers


a = [81, 82, 83]
b = a #Here you give b the exact same list even within memory
print(a is b) #True since a = b, if a is changed then b also changes and vice versa
a[0] = 5
print(b)