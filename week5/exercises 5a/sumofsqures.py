xs = [2,3,4]
def sum_of_squares(xs):
    summedupsqs = [i**2 for i in xs]
    summ = 0
    for kundipokes in summedupsqs:
        summ += kundipokes
    return summ

print(sum_of_squares(xs))

