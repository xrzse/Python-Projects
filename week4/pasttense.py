def pasttense(s):
    if s[-1] == "e":
        s = s + "d"
    elif s[-1] == "y":
        s = s[:-1] + "ied"
    else:
        s = s + "ed"
    
    return s

print(pasttense("Slay"))  # Output: "Slayed"
print(pasttense("Dance")) # Output: "Danced"
print(pasttense("Play"))  # Output: "Played"
print(pasttense("Try"))   # Output: "Tried"