# problem link(https://practice.geeksforgeeks.org/problems/replace-os-with-xs0052/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=replace-os-with-xs)
'''
Given a matrix mat of size N x M where every element is either ‘O’ or ‘X’.
Replace all ‘O’ with ‘X’ that are surrounded by ‘X’.
A ‘O’ (or a set of ‘O’) is considered to be by surrounded by ‘X’ if there are ‘X’ at locations just below, just above, just left and just right of it.

Input: n = 5, m = 4

mat = {{'X', 'X', 'X', 'X'}, 
       {'X', 'O', 'X', 'X'}, 
       {'X', 'O', 'O', 'X'}, 
       {'X', 'O', 'X', 'X'}, 
       {'X', 'X', 'O', 'O'}}
       
Output: ans = {{'X', 'X', 'X', 'X'}, 
               {'X', 'X', 'X', 'X'}, 
               {'X', 'X', 'X', 'X'}, 
               {'X', 'X', 'X', 'X'}, 
               {'X', 'X', 'O', 'O'}}
               
Explanation: Following the rule the above 
matrix is the resultant matrix.

'''

# Complexity
'''
TC-> ~ O(N*M)
SC-> ~ O(N*M)
'''

def dfs(mat,vis,row,col,dr,dc):
    vis[row][col]=1
        
    for i in range(4):
        nrow=row+dr[i]
        ncol=col+dc[i]
        if nrow>=0 and nrow<n and ncol>=0 and ncol<m and mat[nrow][ncol]=='O' and vis[nrow][ncol]==0:
            dfs(mat,vis,nrow,ncol,dr,dc)

def fill(n,m,mat):        
    dr=[-1,0,+1,0]
    dc=[0,+1,0,-1]
        
    vis=[[0 for j in range(m)]for i in range(n)]
        
    for i in range(n):
        for j in range(m):
            if (i==0 or i==n-1 or j==0 or j==m-1) and mat[i][j]=='O' and vis[i][j]==0:
                dfs(mat,vis,i,j,dr,dc)
        
    new_mat=mat.copy()              
    for i in range(n):
        for j in range(m):
            if mat[i][j]=='O' and vis[i][j]==0:
                new_mat[i][j]='X'
    return new_mat            

n = 5
m = 4
mat = [['X', 'X', 'X', 'X'], 
       ['X', 'O', 'X', 'X'], 
       ['X', 'O', 'O', 'X'], 
       ['X', 'O', 'X', 'X'], 
       ['X', 'X', 'O', 'O']]

res_mat=fill(n,m,mat)
for i in res_mat:
    print(*i)
