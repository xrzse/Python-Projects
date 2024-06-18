word = "z"

if word < "banana":
    print("Your word, " + word + ", comes before banana.")
elif word > "banana":
    print("Your word, " + word + ", comes after banana.")
else:
    print("Yes, we have no bananas!")

#When doing string comparsion, python starts at the beginning of each string
#If the first alphabet of a string A is z and string B is f, python will say string A > string B
#Think of alphabets like a = 1
print(ord("a")) 
print(ord("b"))
print(ord("z")) #As you can see c has higher value

#What about if the strings are the same but its Apple vs apple?
Apple = "Apple"
apple = "apple"
print(apple > Apple) #True Python gives a higher value to those with lower case letters
print(ord("a")) #97
print(ord("A")) #65

# What about same string but one is longer?
print("Dog" < "Doghouse") #True
#Python gives higher value to the string if its longer

zz = "Hey there deliahah"



# import string library function  
import string  
  
print("Hello") 
# Storing the characters space, tab etc 
result = string.whitespace 
