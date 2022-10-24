calcinput = input("Type in your equation(seperated by spaces): ")

calcinput = calcinput.split()

operation = calcinput[1]
firstnum = int(calcinput[0])
secondnum = int(calcinput[2])
if operation == "+":
    ans = firstnum + secondnum
    print (ans)

elif operation == "-":
    ans = firstnum - secondnum
    print (ans)
    
elif operation == "/":
    ans = firstnum/secondnum
    print (ans)

elif operation == "x" or operation == "*":
    ans = firstnum*secondnum
    print (ans)

