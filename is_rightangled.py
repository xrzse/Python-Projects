def is_rightangled(x,y,z):
    calc = round((x**2 + y**2)**0.5,2)
    print(calc)
    if z == calc:
        print("Right angle triangle")
    else:
        print("Not right angle triangle")

is_rightangled(19,32,37.22)

