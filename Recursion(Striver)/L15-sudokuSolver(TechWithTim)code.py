'''
Sudoku puzzle solving
This code is from TechWithTim channel
Input:
        7 8 0  | 4 0 0  | 1 2 0
        6 0 0  | 0 7 5  | 0 0 9
        0 0 0  | 6 0 1  | 0 7 8
        - - - - - - - - - - - - - 
        0 0 7  | 0 4 0  | 2 6 0
        0 0 1  | 0 5 0  | 9 3 0
        9 0 4  | 0 6 0  | 0 0 5
        - - - - - - - - - - - - - 
        0 7 0  | 3 0 0  | 0 1 2
        1 2 0  | 0 0 7  | 4 0 0
        0 4 9  | 2 0 6  | 0 0 7

Output:
        7 8 5  | 4 3 9  | 1 2 6
        6 1 2  | 8 7 5  | 3 4 9
        4 9 3  | 6 2 1  | 5 7 8
        - - - - - - - - - - - - - 
        8 5 7  | 9 4 3  | 2 6 1
        2 6 1  | 7 5 8  | 9 3 4
        9 3 4  | 1 6 2  | 7 8 5
        - - - - - - - - - - - - - 
        5 7 8  | 3 9 4  | 6 1 2
        1 2 6  | 5 8 7  | 4 9 3
        3 4 9  | 2 1 6  | 8 5 7

'''

def Solve(Board):
    Find=Find_empty(Board)
    if not Find:
        return True
    else:
        Row,Col=Find
                                         
    for Val in range(1,10):
        if isValid(Board,Row,Col,Val):
            Board[Row][Col]=Val
            if Solve(Board):                 # Backtracking         
                return True
            Board[Row][Col]=0
    return False

def Find_empty(Board):
    for Row in range(9):                # finding the empty Box 
        for Col in range(9):
            if Board[Row][Col]==0:
                return (Row,Col)
    return None

def isValid(Board,Row,Col,Val):
    for i in range(9):
        if Board[Row][i]==Val:          # for checking Row 
            return False
        if Board[i][Col]==Val:          # for checking Column 
            return False
        submatRow=(3*(Row//3))+(i//3)
        submatCol=(3*(Col//3))+(i%3)
        if Board[submatRow][submatCol]==Val:    # for checking submatrix 3*3 
            return False
    return True

def print_board(bo):
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")

        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")                       # printing the board 

            if j == 8:
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + " ", end="")

Board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]

print_board(Board)
print( )
print("--------------------------")
Solve(Board)
print_board(Board)
