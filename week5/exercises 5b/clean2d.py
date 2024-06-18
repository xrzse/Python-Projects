def clean2D(a):
    rownum = 0
    for row in a:
        colnum = 0
        for col in row:
            if col == None or col < 0:
                a[rownum][colnum] = 0
            elif col > 100:
                a[rownum][colnum] = 100
            elif type(col) == float:
                a[rownum][colnum] = int(col)
            else:
                a[rownum][colnum] = col

            colnum +=1
        rownum += 1
    return a


test_data = [[3.5, 2, 1, -6, None], [None, 12.2, -5, 1, None, None]]

print(clean2D(test_data))