'''
Sudoku solver
'''
# this code is not executing perfectly, Go with TechWithTim channel code

def isValid(Board,Row,Col,Val):
    for i in range(9):
        if Board[Row][i]==Val:
            return False
        if Board[i][Col]==Val:
            return False
        submatRow=((3*(Row//3))+(i//3))
        submatCol=((3*(Col//3))+(i%3))
        if Board[submatRow][submatCol]==Val:
            return False
    return True    

def solve(Board):
    #print(Board)
    for Row in range(9):
        for Col in range(9):
            if Board[Row][Col]==".":
                for Val in range(1,10):
                    if isValid(Board,Row,Col,Val):
                        Board[Row][Col]=Val
                        if solve(Board):
                            #print(Board)
                            #for i in range(9):
                                #Output.append(Board[i])
                            return True
                        else:
                            Board[Row][Col]="."
                return False
    return True
Output=[]    
Board=[]
for i in range(9):
    Row=[x for x in input().split()]
    Board.append(Row)
print(solve(Board))
print(Board)
for i in Output:
    print(i)
