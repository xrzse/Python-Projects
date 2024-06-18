import random
for x in range(-100,0,3): 
    print(abs(x))




for x in range(1,10):# the second number needs to be a lil bigger.
    print(x)



count = 0
mylist = [0,3,2,1,0,0]

for x in mylist:
    if x ==0:
        count += 1
print(count)



i = 12345
right_digit = i % 10
print(right_digit)



p = 1
r = 2
n = 3

Amount = p*(1+r)**n

print(Amount)




r = random.choice(range(7,13))
print(r)

r = random.randint(7,13)
print(r)


age = 32

age < 18 or age > 35

tirePressure = 37
if tirePressure not in range(33,38):
    print("Tirepressure bad")
else:
    print("We good")


def avg_value(a,b,c):
    avgvalue = (a+b+c)/3
    print(avgvalue)
    return avgvalue

avg_value(3,3,3)

def sumn(n):
    ans = 0
    for x in range(n):
        ask = int(input("Enter: "))
        ans += ask

    return ans

print(sumn(6))

def string_float(s,f):
    stringlen = int(len(list(s)))
    return stringlen * f

print(string_float("Kundi",5))

def adder3000():
    ans = 0
    while True:
        addition = int(input("give: "))
        ans += addition
        if addition < 0:
            break
    
    return ans

print(adder3000())



amtofcoin = int(input("Enter cents: "))

Unit = 1
Mod = 15
Module = 35
count = 0
if amtofcoin // Module > 0:
    count += amtofcoin // Module
    amtofcoin = amtofcoin - Module*(amtofcoin//Module)

if amtofcoin // Mod > 0:
    count += amtofcoin // Mod
    amtofcoin = amtofcoin - Module*(amtofcoin//Module)

if amtofcoin // Unit > 0:
    count += amtofcoin // Unit
    amtofcoin = amtofcoin - Module*(amtofcoin//Module)

print(count)


