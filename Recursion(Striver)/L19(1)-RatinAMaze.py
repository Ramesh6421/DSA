'''
Rat in a Maze problem

Consider a rat placed at (0, 0) in a square matrix of order N * N.
It has to reach the destination at (N - 1, N - 1).
Find all possible paths that the rat can take to reach from source to destination.
The directions in which the rat can move are 'U'(up), 'D'(down), 'L' (left), 'R' (right).
Value 0 at a cell in the matrix represents that it is blocked and rat cannot move to it
while value 1 at a cell in the matrix represents that rat can be travel through it.
Note: In a path, no cell can be visited more than one time.

N = 4
m[][] = {{1, 0, 0, 0},
         {1, 1, 0, 1}, 
         {1, 1, 0, 0},
         {0, 1, 1, 1}}
Output:
DDRDRR DRDDRR

'''

def solve(i,j,mat,n,vis,path):
    if i==n-1 and j==n-1:
        ans.append(path)
        return
    if i+1<n and vis[i+1][j]==0 and mat[i+1][j]==1:      # moving Down
        vis[i][j]=1
        solve(i+1,j,mat,n,vis,path+"D")
        vis[i][j]=0
    if j-1>=0 and vis[i][j-1]==0 and mat[i][j-1]==1:    # moving Left
        vis[i][j]=1
        solve(i,j-1,mat,n,vis,path+"L") 
        vis[i][j]=0
    if j+1<n and vis[i][j+1]==0 and mat[i][j+1]==1:      # moving Right
        vis[i][j]=1
        solve(i,j+1,mat,n,vis,path+"R")
        vis[i][j]=0
    if i-1>=0 and vis[i-1][j]==0 and mat[i-1][j]==1:    # moving Up
        vis[i][j]=1
        solve(i-1,j,mat,n,vis,path+"U")
        vis[i][j]=0
        

n=int(input())
mat=[]
vis=[]
for i in range(n):
    mat.append([int(x) for x in input().split()])
    vis.append([0 for i in range(n)])
ans=[]
if mat[0][0]==1:
    solve(0,0,mat,n,vis,'')
print(ans)    
    
