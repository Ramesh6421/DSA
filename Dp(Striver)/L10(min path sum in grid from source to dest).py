# minimum path sum in grid ,directions={down,right}
# problem : link()
'''
Ninjaland is a country in the shape of a 2-Dimensional grid 'GRID', with 'N' rows and 'M' columns.
Each point in the grid has some cost associated with it.
Find a path from top left i.e. (0, 0) to the bottom right i.e. ('N' - 1, 'M' - 1)
which minimizes the sum of the cost of all the numbers along the path.
You need to tell the minimum sum of that path.
Note:
You can only move down or right at any point in time.

Input:                           output:
m,n = 2,3                           21
grid = [[5,9,6],[11,5,2]]        i.e,(0,0) -> (0,1) -> (1,1) -> (1,2)
'''

# Recursion + memoization
'''
TC-> O(M*N)
SC-> O((M-1)+(N-1)) + O(M*N)
'''
def paths(mat,row,col,dp):
    if row==0 and col==0:
        return mat[row][col]
    if row<0 or col<0:
        return 10**9+7
    if dp[row][col]!=-1:
        return dp[row][col]
    up=mat[row][col]+paths(mat,row-1,col,dp)
    left=mat[row][col]+paths(mat,row,col-1,dp)
    dp[row][col]=min(up,left)
    return min(up,left)

mat=[[5,9,6],[11,5,2]]
m,n=2,3
dp=[[-1 for i in range(n)]for j in range(m)]
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
                dp[row][col]=mat[row][col]
            else:
                up=mat[row][col]
                if row>0:
                    up+=dp[row-1][col]
                else:
                    up+=10**9+7
                left=mat[row][col]
                if col>0:
                    left+=dp[row][col-1]
                else:
                    left+=10**9+7    
                dp[row][col]=min(up,left)
    return dp[m-1][n-1]
    
mat=[[5,9,6],[11,5,2]]
m,n=2,3
dp=[[-1 for i in range(n)]for j in range(m)]
print(paths(mat,m,n,dp))

# Space Optimization
'''
TC-> O(M*N)
SC-> O(N)
'''
def paths(mat,m,n,prev):
    for row in range(m):
        temp=[-1 for i in range(n)]
        for col in range(n):
            if row==0 and col==0:
                temp[col]=mat[row][col]
            else:
                up=mat[row][col]
                if row>0:
                    up+=prev[col]
                else:
                    up+=10**9+7
                left=mat[row][col]
                if col>0:
                    left+=temp[col-1]
                else:
                    left+=10**9+7    
                temp[col]=min(up,left)
        prev=temp        
    return prev[n-1]
    
mat=[[5,9,6],[11,5,2]]
m,n=2,3
prev=[-1 for i in range(n)]
print(paths(mat,m,n,prev))

