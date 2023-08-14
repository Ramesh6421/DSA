# max path sum in matrix from multiple sources to multiple destinations
# problem: link(https://www.codingninjas.com/codestudio/problems/maximum-path-sum-in-the-matrix_797998?source=youtube&campaign=striver_dp_videos&utm_source=youtube&utm_medium=affiliate&utm_campaign=striver_dp_videos&leftPanelTab=0)
'''
You have been given an N*M matrix filled with integer numbers,
find the maximum sum that can be obtained from a path starting from any cell in the first row to any cell in the last row.
From a cell in a row, you can move to another cell directly below that row, or diagonally below left or right.
So from a particular cell (row, col), we can move in three directions i.e.
Down: (row+1,col)
Down left diagonal: (row+1,col-1)
Down right diagonal: (row+1, col+1)

Input:                output:
1
3 3                     25
10 2 3
3 7 2
8 1 5
'''

#Recursion + Memoization
'''
TC-> O(N*M) + O(M)
SC-> O(N) + O(N*M)
'''
def maxx(mat,row,col,n,m,dp):
    if col<0 or col>=m:
        return -(10**9+7)
    if row==0:
        return mat[row][col]
    if dp[row][col]!=-(10**9+7):
        return dp[row][col]
    up=mat[row][col]+maxx(mat,row-1,col,n,m,dp)
    left_diagonal=mat[row][col]+maxx(mat,row-1,col-1,n,m,dp)
    right_diagonal=mat[row][col]+maxx(mat,row-1,col+1,n,m,dp)
    dp[row][col]=max(up,left_diagonal,right_diagonal)
    return max(up,left_diagonal,right_diagonal)
mat=[[10,2,3],[3,7,2],[8,1,5]]
n,m=3,3
ans=-(10**9+7)
dp=[[-(10**9+7) for j in range(m)]for i in range(n)]
for i in range(m):
    cur=maxx(mat,n-1,i,n,m,dp)
    ans=max(ans,cur)
print(ans)    


# Tabulation
'''
TC-> O(N*M) 
SC-> O(N*M)
'''
def maxx(mat,n,m,dp):
    for j in range(m):
        dp[0][j]=mat[0][j]
    for i in range(1,n):
        for j in range(m):
            up=mat[i][j]+dp[i-1][j]
            left_diagonal=mat[i][j]
            if j-1>=0:
                left_diagonal+=dp[i-1][j-1]
            else:
                left_diagonal+=-(10**9+7)
            right_diagonal=mat[i][j]    
            if j+1<m:    
                right_diagonal+=dp[i-1][j+1]
            else:
                right_diagonal+=-(10**9+7)    
            dp[i][j]=max(up,left_diagonal,right_diagonal)
    
mat=[[10,2,3],[3,7,2],[8,1,5]]
n,m=3,3
dp=[[-(10**9+7) for j in range(m)]for i in range(n)]
maxx(mat,n,m,dp)
print(max(dp[n-1]))

# Space Optimization
'''
TC-> O(N*M)
SC-> O(M)
'''
def maxx(mat,n,m,prev):
    for j in range(m):
        prev[j]=mat[0][j]   
    for i in range(1,n):
        temp=[-(10**9+7) for j in range(m)]
        for j in range(m):
            up=mat[i][j]+prev[j]
            left_diagonal=mat[i][j]
            if j-1>=0:
                left_diagonal+=prev[j-1]
            else:
                left_diagonal+=-(10**9+7)
            right_diagonal=mat[i][j]    
            if j+1<m:    
                right_diagonal+=prev[j+1]
            else:
                right_diagonal+=-(10**9+7)    
            temp[j]=max(up,left_diagonal,right_diagonal)
        prev=temp
    return max(prev)    
    
mat=[[10,2,3],[3,7,2],[8,1,5]]
n,m=3,3
prev=[-(10**9+7) for j in range(m)]
print(maxx(mat,n,m,prev))



