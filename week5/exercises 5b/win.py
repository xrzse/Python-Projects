def win(board):
    for row in board: #Horizontal
        numofx = 0
        numofo = 0
        for col in row:
            if col =="x":
                numofx += 1
            elif col =="o":
                numofo += 1
        if numofx == 3:
            return "x"
        elif numofo == 3:
            return "o"
    
    i = 0
    for col in board:
        numofx = 0
        numofo = 0
        if col[i] == "x":
            numofx +=1
        elif col[i] == "o":
            numofo += 1
        
        if numofx == 3:
            return "x"
        elif numofo == 3:
            return "o"
    
    

    


array = [
    ["x","o","x"],
    ["x","x","o"],
    ["x","o","x"]
        ]

print(win(array))