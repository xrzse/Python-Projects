person = "Healie"
cook = "231"
greeting = "Hello {}, {}".format(person, cook)

print(greeting)

a = 5
b = 9

letter = "Dear {0} {2}. {0}, I have an interesting money-making proposition for you! If you deposit $10 million into my bank account, I can double your money ..."

print(letter.format("Bill","Curry","Gates"))

x = 2
y = 6
print('sum of {} and {} is {}; product: {}.'.format( x, y, x+y, x*y))
v = 2.34567
print('{:.1f} {:.2f} {:.7f}'.format(v, v, v)) # 1f is 1 digit after decimal and so on.
#2.3 2.35 2.3456700

s = "python rocks" #len function starts counting at 1
print(len(s)) 
s = s.split(" ")
print(s)
print(len(s)) 

