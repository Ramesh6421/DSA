# problem link(https://practice.geeksforgeeks.org/problems/find-the-number-of-islands/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=find_the_number_of_islands)
# notes link(https://takeuforward.org/graph/breadth-first-search-bfs-level-order-traversal/)
'''
Given a grid of size n*m (n is the number of rows and m is the number of columns in the grid) consisting of '0's (Water) and '1's(Land).
Find the number of islands.

Note: An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically or diagonally i.e., in all 8 directions.

'''
# Complexity
'''
TC-> O(N*N)
SC-> O(N*N) + O(N*N) 
'''
def BFS(vis,grid,i,j,n,m):
    q=[(i,j)]
    while q:
        row,col=q.pop(0)
        vis[row][col]=1
        for delrow in range(-1,2):
            for delcol in range(-1,2):
                nrow=row+delrow
                ncol=col+delcol
                if nrow>=0 and nrow<n and ncol>=0 and ncol<m:
                    if grid[nrow][ncol]==1 and vis[nrow][ncol]==0:
                        vis[nrow][ncol]=1 
                        q.append((nrow,ncol))
                                

def numIslands(grid):
    count=0
    n=len(grid)
    m=len(grid[0])
    vis=[[0 for j in range(m)] for i in range(n)]
    for i in range(n):
        for j in range(m):
            if grid[i][j]==1 and vis[i][j]==0:
                count+=1
                vis[i][j]=1
                BFS(vis,grid,i,j,n,m)
    return count            


grid=[[0,1,1,0],
      [0,1,1,0],
      [0,0,1,0],
      [0,0,0,0],
      [1,1,0,1]
      ]
ans=numIslands(grid)
print(ans)             # Output = 3
