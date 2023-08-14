'''
N-Queens placing (APPROACH-2)
'''
def solve(Col,Board,N,RowDict,UpdiagDict,LowdiagDict):
    if Col==N:
        #print(Board)
        A=[]
        for i in Board:
            B=[]
            for j in i:
                B.append(j)
            A.append(B)    
        Answer.append(A)
    for Row in range(N):
        X=Row+Col
        Y=(N-1)+(Col-Row)
        if Row not in RowDict and X not in LowdiagDict and Y not in UpdiagDict:
            RowDict[Row]=1      # Left Row Hash table
            LowdiagDict[X]=1    # Lower diagonal Hash table
            UpdiagDict[Y]=1     # Upper diagonal Hash table
            Board[Row][Col]='Q'
            #print(Board)
            solve(Col+1,Board,N,RowDict,UpdiagDict,LowdiagDict)
            RowDict.pop(Row)
            LowdiagDict.pop(X)
            UpdiagDict.pop(Y)
            Board[Row][Col]=0
        

n=int(input())
Board=[[0 for i in range(n)]for j in range(n)]
Answer=[]
RowDict={}
UpdiagDict={}
LowdiagDict={}
solve(0,Board,n,RowDict,UpdiagDict,LowdiagDict)
#print(Answer)
for Row in Answer:
    for Col in Row:
        print(Col)
    print( )    
        
