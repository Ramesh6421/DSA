# Problem link(https://practice.geeksforgeeks.org/problems/distance-of-nearest-cell-having-1-1587115620/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=distance-of-nearest-cell-having-1)
'''
Given a binary grid of n*m. Find the distance of the nearest 1 in the grid for each cell.
The distance is calculated as |i1  - i2| + |j1 - j2|, where i1, j1 are the row number and column number of the current cell,
and i2, j2 are the row number and column number of the nearest cell having value 1.
 
'''
# Complexity
'''
TC-> O(N*M) + O(N*M)*4  ~ O(N*M)
SC-> O(N*M) + O(N*M) + O(N*M)
'''

def nearest(grid):
    n=len(grid)
    m=len(grid[0])
    vis=[[0 for j in range(m)]for i in range(n)]
    dist=[[0 for j in range(m)]for i in range(n)]
    q=[]
    for i in range(n):
        for j in range(m):
            if grid[i][j]==1:
                vis[i][j]=1
                q.append((i,j,0))
		
    delrow=[-1,0,+1,0]
    delcol=[0,+1,0,-1]
		
    while q:
        row,col,steps=q.pop(0)
        dist[row][col]=steps
        for i in range(4):
            nrow=row+delrow[i]
            ncol=col+delcol[i]
            if nrow>=0 and nrow<n and ncol>=0 and ncol<m and vis[nrow][ncol]==0:
                vis[nrow][ncol]=1
                q.append((nrow,ncol,steps+1))
		 
    return dist           

grid=[[0,0,0],
      [0,1,0],
      [1,0,1]
      ]
dis=nearest(grid)
print(dis)
		                  
	
