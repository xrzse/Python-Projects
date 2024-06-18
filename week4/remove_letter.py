def remove_letter(theLetter, theString):
    newstring = ""
    for x in theString:
        if x != theLetter:
            newstring += x
    return newstring


theLetter = "e"
theString = "Hey there stuepdh"
print(remove_letter(theLetter, theString))