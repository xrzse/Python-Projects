def reverseList(list):
    if list == []:
        return list
    else:
        headlist = list[0]
        taillist = list[1:]
        return reverseList(taillist) + [headlist]
    
print(reverseList([2,3,4,3,32,3,4]))
