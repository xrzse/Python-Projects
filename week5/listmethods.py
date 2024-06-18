mylist = []
mylist.append(5)
mylist.append(27)
mylist.append(3)
mylist.append(12)
print(mylist) #pretty straight forward [5, 27, 3, 12]

mylist.insert(1, 12)  # Insert 12 at pos 1, shift other items up, this is similar to mylist[1:1] = [12]
print(mylist) # [5, 12, 27, 3, 12]
print(mylist)

print(mylist.count(12))     # How many times is 12 in mylist?

print(mylist.index(3))   # Find index of first 3 in mylist
print(mylist.count(5))

mylist.reverse() #.reverse() reverses it.
print(mylist)

mylist.sort(reverse=True) #Sorts largest to smallest 
print(mylist) #[27, 12, 12, 5, 3]
mylist.sort() #Sorts smallest to largest
print(mylist) #[3, 5, 12, 12, 27]

mylist.remove(5) #[3, 12, 12, 27]
print(mylist)

lastitem = mylist.pop() #Returns last item in the list and removes last item from list
print(lastitem) #27
print(mylist)

"""
It is important to remember that methods like append, sort, and reverse all return None.
This means that re-assigning mylist to the result of sorting mylist will result in 
losing the entire list. 
Calls like these will likely never appear as part of an assignment statement
"""
print(mylist.sort()) #None

mylist.sort()
print(mylist) #[3, 12, 12] The correct way is to sort it and then print it

mylist = mylist.sort()
print(mylist) #None


alist = [4, 2, 8, 6, 5]
temp = alist.pop(2) #removes the value at INDEX 2, not 2 itself. And gives it to temp
temp = alist.pop() #removes the value at the end and gives it to temp
print(alist) #[4,2,6]

alist = [4, 2, 8, 6, 5]
alist = alist.pop(0) #removes 4 from the list since it is at index 0 and gives the value 4 to alist
print(alist) #4