def testMethod(v):
    for i in v:
        float(i)

v = [1.32,"a",432]
try:
    print(testMethod(v))
except IndexError as e: #Index error if ur tryna access a index that is not within a list for ex len[li] = 2 but you did print(li[4])
    print("Woopity poopty: "+ str(e.args))
except ValueError as e:
    print("Woofsdspity pofopty: " + str(e.args)) #Trying to convert a str to a float
except TypeError as e:
    print("Woopity poopty: " + str(e.args)) #Trying to add str to an int or float
