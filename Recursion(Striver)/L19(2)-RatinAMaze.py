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
    
    for ind in range(n):
        nexti=i+di[ind]
        nextj=j+dj[ind]
        if nexti>=0 and nextj>=0 and nexti<n and nextj<n and mat[nexti][nextj]==1 and vis[nexti][nextj]==0:
            vis[i][j]=1
            solve(nexti,nextj,mat,n,vis,path+direction[ind])
            vis[i][j]=0
    

    
n=int(input())
mat=[]
vis=[]
for i in range(n):
    mat.append([int(x) for x in input().split()])
    vis.append([0 for i in range(n)])
ans=[]
di=[+1,0,0,-1]   # [Down(i),Left(i),Right(i),up(i)]
dj=[0,-1,+1,0]   # [Down(j),Left(j),Right(j),up(j)]
direction='DLRU'
if mat[0][0]==1:
    solve(0,0,mat,n,vis,'')
print(ans)    
    
