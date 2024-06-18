def ints(a):
    if a == []:
        return []
    
    head = a[0] #first elem of list
    tail = a[1:] #rest of the elems - first elem
    
    if type(head) == int: #checks if first elem is int
        firstelem = True
    else:
        firstelem = False

    return [firstelem] + ints(tail) # Returns firstelem value + the recursion continued with the tail and so on until base case

a = [332.32, 1.3, 3232, 2, 323, 3.43, 32, 4, 334, 4, 232, 5]

print(ints(a))