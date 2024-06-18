haystack = "hejkdhsakneedledbsakdja"
if "needle" in haystack:
    print("found")

amtofas = 0
s = "hejkdhsakneedledbsakdAAAAdsAAAAaaaaja"
for i in s:
    if i.lower() =="a":
        amtofas+=1
print(amtofas)

d = [float(i) for i in range(100)]
print(d)


a = [i for i in (range(4,0,-1))] #range starts at 4 and goes back due to -1 and counts until zero but not including zero.
print(a)

arr = [1,2,3,4,5,6,7]
print(arr[2])
print(arr[-1])


listofbools = [[True, False],
               [False, True],
               [False,False]]

a = [1,2,3,4,5] 
a = a + [2,2,3] #Method 1 of adding numbers to the end of a list

b = [1,2,3,4,5]
for i in range(1,4): #Method 2
    b.append(i)
print(b)

print()
a = [4,534,23,2,42]
print(a)
a.remove(2) #.remove removes the given value not the given index
print(a)

