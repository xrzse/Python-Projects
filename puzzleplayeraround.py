
def word_search(board, words):

    words = [words.upper()] if isinstance(words, str) else [word.upper for word in words]
    board = [b.upper() for b in board]

    #Horizontal both ways
    for row in board: # goes over each row in BOARD
        for word in words: # goes over each WORD
            if word in row or word in row[::-1]:
                return True
    
    #Transposed board
    boardflipped = [""] * len(board[0])
    for col in range(len(board[0])): # Amt of times it goes over columns
        for row in range(len(board)): # Amt of time it goes over rows
            boardflipped[col] += board[row][col] # flips them 
    
    #Vertical both ways
    for row in boardflipped:
        for word in words:
            if word in row or word in row[::-1]:
                return True
    
    def board_diagonal(board):
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
  
        for j in range(length): #Loop of diagonals (top left to top right)
            diagonal = []
            k = 0
            for i in range(size):
                if k + j < size:
                    diagonal.append(board[i][k+j])
                    k += 1
            diagonals.append(''.join(diagonal))

        for j in range(length): #Loop of diagonals (bottom left to bottom right)
            diagonal = []
            k = length - 1
            for i in range(size):
                if k - i >= 0 and j + i < length:
                    diagonal.append(board[k-i][j+i])
        
            diagonals.append(''.join(diagonal))

        for i in range(size): #Loop of diagonals (bottom left to top left)
            diagonal = []
            k = size - 1
            for j in range(length):
                if k - i >= 0:
                    diagonal.append(board[k-i][j])  
                k -=1
            diagonals.append(''.join(diagonal))
        return diagonals
    
    list_of_diagonals = board_diagonal(board)
    for row in list_of_diagonals: # goes over each row in BOARD
        for word in words: # goes over each WORD
            if word in row or word in row[::-1]:
                return True
    
    return False

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

for word in words:
    print(word_search(puzzle,word))