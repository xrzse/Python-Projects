julia = ("Julia", "Roberts", 1967, "Duplicity", 2009, "Actress", "Atlanta, Georgia") #tuple

try:
    julia[0] = 'X' #TypeError: 'tuple' object does not support item assignment
except:
    ValueError