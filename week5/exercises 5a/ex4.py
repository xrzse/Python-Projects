myList = [76, 92.3, 'hello', True, 4, 76]

#Append “apple” and 76 to the list.
myList.append("apple")
myList.append(76)
print(myList)
#Insert the value “cat” at position 3.
myList[3:3] = ["cat"]
print(myList)
#Insert the value 99 at the start of the list.
myList[0:0] = [99]
print(myList)
#Find the index of “hello”.
indexhello = myList.index("hello")
print(indexhello)
#Count the number of 76s in the list.
count76 = myList.count(76)
print(count76)
#Remove the first occurrence of 76 from the list.
myList.pop(myList.index(76))
print(myList)
#Remove True from the list using pop and index.
myList.pop(myList.index(True))
print(myList)