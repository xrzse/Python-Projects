def sinnumbercheck(sinnumber):
    digits = 0
    spaces = 0

    if len(sinnumber) == 9:
        for x in sinnumber:
            if x.isdigit():
                digits += 1
        if digits == 9:
            return sinnumber + " Is a valid SIN number"
        else:
            return sinnumbercheck(sinnumber=input("Try again: "))

    elif len(sinnumber) == 11:

        for x in sinnumber:
            if x.isdigit():
                digits+=1
        for x in sinnumber[3::4]:
            print(x)
            if x == " ":
                spaces += 1
        
        if digits == 9 and spaces == 2:
            return sinnumber + " Is a valid SIN number"
        else:
            return sinnumbercheck(sinnumber=input("Try again: "))
    
    else:
        return sinnumbercheck(sinnumber=input("Try again: "))
        
print(sinnumbercheck("123 456 789"))