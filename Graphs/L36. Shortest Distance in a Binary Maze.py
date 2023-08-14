# Problem link(https://practice.geeksforgeeks.org/problems/shortest-path-in-a-binary-maze-1655453161/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=shortest-path-in-a-binary-maze)
'''
Given a n * m matrix grid where each element can either be 0 or 1.
You need to find the shortest distance between a given source cell to a destination cell.
The path can only be created out of a cell if its value is 1. 

If the path is not possible between source cell and destination cell, then return -1.

Note : You can move into an adjacent cell if that adjacent cell is filled with element 1.
Two cells are adjacent if they share a side.
In other words, you can move in one of the four directions, Up, Down, Left and Right.

Example 1:

Input:
grid[][] = {{1, 1, 1, 1},
            {1, 1, 0, 1},
            {1, 1, 1, 1},
            {1, 1, 0, 0},
            {1, 0, 0, 1}}
source = {0, 1}
destination = {2, 2}
Output:
3
Explanation:
1 1 1 1
1 1 0 1
1 1 1 1
1 1 0 0
1 0 0 1
The highlighted part in the matrix denotes the 
shortest path from source to destination cell.
Example 2:

Input:
grid[][] = {{1, 1, 1, 1, 1},
            {1, 1, 1, 1, 1},
            {1, 1, 1, 1, 0},
            {1, 0, 1, 0, 1}}
source = {0, 0}
destination = {3, 4}
Output:
-1
Explanation:
The path is not possible between source and 
destination, hence return -1.
'''

# Complexity
'''
TC-> O(N*M)
SC-> O(N*M)
'''

def shortestPath(grid, src, dest):
    if src[0]==dest[0] and src[1]==dest[1]:
        return 0
            
    n=len(grid)
    m=len(grid[0])
    dist=[[10**9 for j in range(m)] for i in range(n)]
    q=[]

    q.append((0,src[0],src[1]))

    dr=[-1,0,1,0]
    dc=[0,1,0,-1]
    
    while q:
        dis,r,c=q.pop(0)
        for i in range(4):
            newr=r+dr[i]
            newc=c+dc[i]
            if newr>=0 and newr<n and newc>=0 and newc<m and grid[newr][newc]==1:
                if dis+1<dist[newr][newc]:
                    dist[newr][newc]=dis+1
                    if newr==dest[0] and newc==dest[1]:
                        return dis+1
                    q.append((dis+1,newr,newc))
                        
    return -1                

grid = [[1, 1, 1, 1],
        [1, 1, 0, 1],
        [1, 1, 1, 1],
        [1, 1, 0, 0],
        [1, 0, 0, 1]]

source = [0, 1]
destination = [2, 2]

print(shortestPath(grid,source,destination))
