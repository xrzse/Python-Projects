valid = range(35,45)
def tire_pressure_checker(q,w,e,r):
    if q in valid and w in valid and e in valid and r in valid and abs(q - w) < 2 and abs(e - r) <2:
        return True
    else:
        return False

print(tire_pressure_checker(35,36,43,42))
