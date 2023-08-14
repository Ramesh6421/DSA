# problem
'''
Given a grid of dimension nxm where each cell in the grid can have values 0, 1 or 2 which has the following meaning:
0 : Empty cell
1 : Cells have fresh oranges
2 : Cells have rotten oranges

We have to determine what is the minimum time required to rot all oranges.
A rotten orange at index [i,j] can rot other fresh orange at indexes [i-1,j], [i+1,j], [i,j-1], [i,j+1] (up, down, left and right) in unit time. 

'''

# Complexity
'''
TC-> (O(N*M) + O(N*M)*4) ~ O(N*M)
SC-> O(N*M)
'''
def OrangesRotting(grid):

    count=0
    n=len(grid)
    m=len(grid[0])
		
    q=[]
		
    delrow = [-1,0,+1,0]
    delcol = [0,+1,0,-1]
		
    vis=[[0 for j in range(m)]for i in range(n)]
		
    cntfresh=0
    ones=0
		
    for i in range(n):
        for j in range(m):
            if grid[i][j]==2:
                vis[i][j]=1
                q.append((i,j))
            if grid[i][j]==1:
                ones+=1
		          
    while q:
        size=len(q)
        count+=1
        for i in range(size):
            row,col=q.pop(0)
            for j in range(4):
                nrow=row+delrow[j]
                ncol=col+delcol[j]
                if nrow>=0 and nrow<n and ncol>=0 and ncol<m:
                    if grid[nrow][ncol]==1 and vis[nrow][ncol]==0:
                        vis[nrow][ncol]=1
                        q.append((nrow,ncol))
                        cntfresh+=1
		                
    if cntfresh!=ones:
        return -1
    return count-1      


grid=[[0,1,2],
      [0,1,2],
      [2,1,1]
      ]
time=OrangesRotting(grid)
print(time)                # output =1
 
