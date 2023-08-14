# problem link(https://practice.geeksforgeeks.org/problems/flood-fill-algorithm1856/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=flood-fill-algorithm)
# notes link(https://takeuforward.org/graph/flood-fill-algorithm-graphs/)
'''
An image is represented by a 2-D array of integers, each integer representing the pixel value of the image.
Given a coordinate (sr, sc) representing the starting pixel (row and column) of the flood fill,
and a pixel value newColor, "flood fill" the image.
To perform a "flood fill", consider the starting pixel,
plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel,
plus any pixels connected 4-directionally to those pixels (also with the same color as the starting pixel), and so on.
Replace the color of all of the aforementioned pixels with the newColor.
'''
# Complexity
'''
TC-> O(N*M + N*M) ~ O(N*M)
SC-> O(N*M) + O(N*M)
'''

def dfs(row,col,grid,image,iniColor,newColor,delrow,delcol,n,m):
    grid[row][col]=newColor
    for i in range(4):
        nrow=row+delrow[i]
        ncol=col+delcol[i]
        if nrow>=0 and nrow<n and ncol>=0 and ncol<m:
            if image[nrow][ncol]==iniColor and grid[nrow][ncol]!=newColor:
                dfs(nrow,ncol,grid,image,iniColor,newColor,delrow,delcol,n,m)

def floodFill(image,sr,sc,newColor):
    grid = image
    n=len(grid)
    m=len(grid[0])
    delrow = [-1,0,+1,0]
    delcol = [0,+1,0,-1]
    iniColor=grid[sr][sc]
    dfs(sr,sc,grid,image,iniColor,newColor,delrow,delcol,n,m)
    return grid

image=[[1,1,1],
       [2,2,0],
       [2,2,2]
       ]

sr,sc = 2,0
newColor = 3
res=floodFill(image,sr,sc,newColor)
print(res)
