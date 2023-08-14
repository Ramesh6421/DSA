# problem link(https://practice.geeksforgeeks.org/problems/number-of-enclaves/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=number-of-enclaves)
'''
You are given an n x m binary matrix grid, where 0 represents a sea cell and 1 represents a land cell.
A move consists of walking from one land cell to another adjacent (4-directionally) land cell or walking off the boundary of the grid.
Find the number of land cells in grid for which we cannot walk off the boundary of the grid in any number of moves.

Input:
grid[][] = {{0, 0, 0, 0},
            {1, 0, 1, 0},
            {0, 1, 1, 0},
            {0, 0, 0, 0}}
Output:
3
Explanation:
0 0 0 0
1 0 1 0
0 1 1 0
0 0 0 0
The highlighted cells represents the land cells.

'''

# Complexity
'''
TC-> ~ O(N*M)
SC-> ~ O(N*M)
'''

def number_of_enclaves(grid):
    q=[]
    n=len(grid)
    m=len(grid[0])
    vis=[[0 for j in range(m)]for i in range(n)]
        
    for i in range(n):
        for j in range(m):
            if i==0 or j==0 or i==n-1 or j==m-1:
                if grid[i][j]==1:
                    vis[i][j]=1
                    q.append((i,j))
                
        
    delrow=[-1,0,+1,0]
    delcol=[0,+1,0,-1]
        
    while q:
        row,col=q.pop(0)
        for i in range(4):
            nrow=row+delrow[i]
            ncol=col+delcol[i]
            if nrow>=0 and nrow<n and ncol>=0 and ncol<m and vis[nrow][ncol]==0 and grid[nrow][ncol]==1:
                vis[nrow][ncol]=1
                q.append((nrow,ncol))
        
    count=0
    for i in range(n):
        for j in range(m):
            if vis[i][j]==0 and grid[i][j]==1:
                count+=1
    return count            

grid = [[0, 0, 0, 0],
        [1, 0, 1, 0],
        [0, 1, 1, 0],
        [0, 0, 0, 0]]

print(number_of_enclaves(grid))
