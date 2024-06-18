def get_front_list(a,target):
    summ = 0
    indexx = 0
    for elem in a:
        if a[0]:
            return -1
        elif summ + elem > target:
            return summ
        else:
            indexx +=1
            summ += elem


a = [1232,3,23,2,3,2,43,42,3434,24,234,24,3,42,34,234,23,42,5,46,456,46,456,456,45,645,7,67,56,75,757,57,57,575,75,757,575,757,5]
target = 500
print(get_front_list(a,target))