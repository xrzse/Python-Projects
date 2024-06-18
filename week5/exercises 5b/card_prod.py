def cart_prod(a,b):
    c = []
    for elem in a:
        for z in b:
            c.append([elem,z])
    return c

print(cart_prod([1,2,4,6], [5,6,7]))
