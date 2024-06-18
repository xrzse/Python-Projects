def scramble(s):
    evenchars = s[0::2]
    oddchars = s[1::2]
    return evenchars + oddchars

print(scramble("Kundi oaks"))