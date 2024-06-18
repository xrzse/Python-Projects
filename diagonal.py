def board_diagonal(board, words):
    diagonals = []#
    size = len(board)#
    length = len(board[0])#

    for i in range(size): #Loop of diagonals (top left to bottom left)
        diagonal = []
        k = 0
        for j in range(length):
            if k + i < length:
                diagonal.append(board[k+i][j])
                k += 1
        diagonals.append(''.join(diagonal))
    print("First loop done")
    print(len(diagonals))    
    for j in range(length): #Loop of diagonals (top left to top right)
        diagonal = []
        k = 0
        for i in range(size):
            if k + j < size:
                diagonal.append(board[i][k+j])
                k += 1
        diagonals.append(''.join(diagonal))
    print("Second loop done")
    print(len(diagonals))

    for j in range(length): #Loop of diagonals (bottom left to bottom right)
        diagonal = []
        k = length - 1
        for i in range(size):
            if k - i >= 0 and j + i < length:
                diagonal.append(board[k-i][j+i])
    
        diagonals.append(''.join(diagonal))
    print("Third loop done")  

    for i in range(size): #Loop of diagonals (bottom left to top left)
        diagonal = []
        k = size - 1
        for j in range(length):
            if k - i >= 0:
                diagonal.append(board[k-i][j])  
            k -=1
        print(diagonal)
        diagonals.append(''.join(diagonal))
    print("Fourth loop done")
      
    print(diagonals)
    print(len(diagonals))


puzzle = [ #17 x 17
"KLIMTSEINWORBCHOC",
"CGOLYNASEMISWEETT",
"EHNCSDENETEEWSNUO",
"RCIIOENIIGFILLING",
"SIOPKCLADNABFTESE",
"KFRNSAOFCEIOOMCTV",
"NRHEFDBAFTRSOEHEI",
"ICATAERTTUIGDDOGT",
"RORDSNCECCRONSCNC",
"DOWEFTRTEUTTUIOII",
"GKHTASPCIRPOHFLDD",
"NIIEWMRUEOICOTADD",
"IETESEPSRCNNAHTUA",
"CSESAESIIYDEBKIPO",
"ITIMBERLEUSAROEAM",
"AWFUDGECEARCAYRSO",
"SUGARDTESSUOMRSEE"
]
words = [
"ADDICTIVE",
"BAKING",
"BARS",
"BITTERSWEET",
"BROWNIES",
"CAKES",
"CANDY",
"CHIPS",
"CHOCOLATIERS",
"COCOA",
"CONFECTIONERY",
"COOKIES",
"CREAM PIE",
"CUPCAKE",
"DARK",
"DECADENT",
"DELICIOUS",
"DESSERT",
"DRINKS",
"FILLING",
"FONDUE",
"FOOD",
"FUDGE",
"ICE CREAM",
"ICING",
"INGREDIENT",
"MILK",
"MOUSSE",
"PUDDING",
"SEMISWEET",
"SUGAR",
"SWISS",
"SYRUP",
"TREAT",
"TRUFFLES",
"UNSWEETENED",
"WHITE",
]
board_diagonal(puzzle,words)