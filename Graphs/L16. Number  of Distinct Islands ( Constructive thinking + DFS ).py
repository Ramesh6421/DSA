# problem link()
'''
Given a boolean 2D matrix grid of size n * m.
You have to find the number of distinct islands where a group of connected 1s (horizontally or vertically) forms an island.
Two islands are considered to be distinct if and only if one island is equal to another (not rotated or reflected).

Input:
grid[][] = {{1, 1, 0, 0, 0},
            {1, 1, 0, 0, 0},
            {0, 0, 0, 1, 1},
            {0, 0, 0, 1, 1}}
Output:
1
Explanation:
Island 1, 1 at the top left corner is same as island
1, 1 at the bottom right corner.
Example 2:

Input:
grid[][] = {{1, 1, 0, 1, 1},
            {1, 0, 0, 0, 0},
            {0, 0, 0, 0, 1},
            {1, 1, 0, 1, 1}}
Output:
3
Explanation:
Distinct islands are: 1, 1 at the top left corner;
1, 1 at the top right corner and 1 at the bottom 
right corner. We ignore the island 1, 1 at the 
bottom left corner since 1, 1 it is identical to the 
top right corner.

'''

# Complexity
'''
TC-> ~ O(N*M)
SC-> ~ O(N*M)
'''

def dfs(row,col,n,m,vis,grid,island,baserow,basecol):

    vis[row][col]=1
    island.append((row-baserow,col-basecol))

    delrow=[-1,0,+1,0]
    delcol=[0,+1,0,-1]
    
    for i in range(4):
        nrow=row+delrow[i]
        ncol=col+delcol[i]
        if nrow>=0 and nrow<n and ncol>=0 and ncol<m and grid[nrow][ncol]==1 and vis[nrow][ncol]==0:
             dfs(nrow,ncol,n,m,vis,grid,island,baserow,basecol)


def number_of_Distinct_Islands(grid):        
    n=len(grid)
    m=len(grid[0])
    vis=[[0 for j in range(m)]for i in range(n)]
    st=set()
            
    for i in range(n):
        for j in range(m):
            if vis[i][j]==0 and grid[i][j]==1:
                island=[]
                dfs(i,j,n,m,vis,grid,island,i,j)
                st.add(tuple(island))
                    
    return len(st)            

grid = [[1, 1, 0, 0, 0],
        [1, 1, 0, 0, 0],
        [0, 0, 0, 1, 1],
        [0, 0, 0, 1, 1]]

print(number_of_Distinct_Islands(grid))
