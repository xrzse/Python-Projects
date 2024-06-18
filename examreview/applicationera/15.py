def isGood(s):
    if len(s) > 20 and s.lower() == s or s.upper() == s:
        return True
    else:
        return False


while True:
    z = isGood(s=input("Enter a string longer than 20 and all uppercase or all lowercase no mix: "))
    if z:
        break
    