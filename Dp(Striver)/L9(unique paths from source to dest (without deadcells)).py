# unique paths in grid
# problem : link(https://www.codingninjas.com/codestudio/problems/maze-obstacles_977241?source=youtube&campaign=striver_dp_videos&utm_source=youtube&utm_medium=affiliate&utm_campaign=striver_dp_videos&leftPanelTab=0)
'''
Given a ‘N’ * ’M’ maze with obstacles, count and return the number of paths to reach the right-bottom cell from the top-left cell.
A cell in the given maze has a value -1 if it is a blockage or dead-end, else 0.
From a given cell, we are allowed to move to cells (i+1, j) and (i, j+1) only.
Since the answer can be large, print it modulo 10^9 + 7.

Example:
Consider the maze below :
0 0 0 
0 -1 0 
0 0 0

There are two ways to reach the bottom left corner - 

(1, 1) -> (1, 2) -> (1, 3) -> (2, 3) -> (3, 3)
(1, 1) -> (2, 1) -> (3, 1) -> (3, 2) -> (3, 3)

Hence the answer for the above test case is 2.

Input:
m,n = 3,3
arr=[[0,0,0],[0,-1,0],[0,0,0]]

output:
2
'''
# Recursion + Memoization
'''
TC-> O(M*N)
SC-> O((M-1)+(N-1))+O(M*N)
'''
def paths(mat,row,col,dp):
    if row==0 and col==0:
        return 1
    if row<0 or  col<0:
        return 0
    if dp[row][col]!=-1:
        return dp[row][col]
    up,left=0,0
    if row-1>=0 and mat[row-1][col]==0:
        up=paths(mat,row-1,col,dp)
    if col-1>=0 and mat[row][col-1]==0:    
        left=paths(mat,row,col-1,dp)
    dp[row][col]=up+left    
    return up+left

mat=[[0,0,0],[0,-1,0],[0,0,0]]
m,n=3,3
dp=[[-1 for i in range(n)] for j in range(m)]
print(paths(mat,m-1,n-1,dp))

# Tabulation
'''
TC-> O(M*N)
SC-> O(M*N)
'''
def paths(mat,m,n,dp):
    for row in range(m):
        for col in range(n):
            if row==0 and col==0:
                dp[row][col]=1
            else:
                down,right=0,0
                if row>0 and mat[row-1][col]==0:
                    down = dp[row-1][col]
                if col>0 and mat[row][col-1]==0:
                    right = dp[row][col-1]
                dp[row][col]=down+right
    return dp[m-1][n-1]
mat=[[0,0,0],[0,-1,0],[0,0,0]]
m,n=3,3
dp=[[-1 for i in range(n)] for j in range(m)]
print(paths(mat,m-1,n-1,dp))

# space optimization
'''
TC-> O(M*N)
SC-> O(M)
'''
def paths(mat,m,n,prev):
    for row in range(m):
        temp=[-1 for i in range(n)]
        for col in range(n):
            if row==0 and col==0:
                temp[col]=1
            else:
                down,right=0,0
                if row>0 and mat[row-1][col]==0:
                    down = prev[col]
                if col>0 and mat[row][col-1]==0:
                    right = temp[col-1]
                temp[col]=down+right
        prev=temp        
    return prev[n-1]
mat=[[0,0,0],[0,-1,0],[0,0,0]]
m,n=3,3
prev=[-1 for i in range(n)] 
print(paths(mat,m,n,prev))
        
