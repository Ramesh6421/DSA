'''
N-Queens placing in a N*N chess board

N = 4
Output:
[0, 0, 'Q', 0]
['Q', 0, 0, 0]
[0, 0, 0, 'Q']
[0, 'Q', 0, 0]

[0, 'Q', 0, 0]
[0, 0, 0, 'Q']
['Q', 0, 0, 0]
[0, 0, 'Q', 0]


'''
def isSafe(row,col,board,n):
    duprow,dupcol=row,col
    while row>=0 and col>=0:      # for checking left upper diagonal 
        if board[row][col]=='Q':
            return False
        row=row-1
        col=col-1
    row,col=duprow,dupcol         # for checking left side horizontally 
    while col>=0:
        if board[row][col]=='Q':
            return False
        col=col-1
    row,col=duprow,dupcol         # for checking left lower diagonal
    while row<n and col>=0:
        if board[row][col]=='Q':
            return False
        row=row+1
        col=col-1   
    return True    
        

def solve(col,board,n):
    if col==n:
        A=[]
        for i in board:
            B=[]
            for j in i:
                B.append(j)
            A.append(B)    
            #print(i)
        #print( )
        Answer.append(A)
        return
    for row in range(n):
        if isSafe(row,col,board,n):
            board[row][col]='Q'
            solve(col+1,board,n)
            board[row][col]=0
n=int(input())
Board=[[0 for i in range(n)]for j in range(n)]
Answer=[]
solve(0,Board,n)
#print(Answer)
for i in Answer:
    for j in i:
        print(j)
    print( )    
