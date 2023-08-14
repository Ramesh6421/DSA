# problem link(https://practice.geeksforgeeks.org/problems/path-with-minimum-effort/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=path-with-minimum-effort)
'''
You are a hiker preparing for an upcoming hike.
You are given heights, a 2D array of size rows x columns,
where heights[row][col] represents the height of cell (row, col).
You are situated in the top-left cell, (0, 0),
and you hope to travel to the bottom-right cell, (rows-1, columns-1) (i.e., 0-indexed).
You can move up, down, left, or right, and you wish to find a route that requires the minimum effort.

A route's effort is the maximum absolute difference in heights between two consecutive cells of the route.

Example 1:

heights = [[1,2,2],[3,8,2],[5,3,5]]
Output: 2
Explaination: The route of [1,3,5,3,5] has a maximum absolute difference of 2 in consecutive cells.
This is better than the route of [1,2,2,2,5], where the maximum absolute difference is 3.

'''
# Complexity
'''
TC-> O(N*M)*log(N*M)
SC-> O(N*M)
'''

from heapq import heapify,heappush,heappop
def MinimumEffort(heights):
    minHeap=[]
    heapify(minHeap)
    n=len(heights)
    m=len(heights[0])

    dist=[[10**9 for j in range(m)] for i in range(n)]
    dist[0][0]=0
    heappush(minHeap,(0,(0,0)))
    
    dr=[-1,0,1,0]
    dc=[0,1,0,-1]
    
    while minHeap:
        diff,pair=heappop(minHeap)
        row,col=pair
        if row==n-1 and col==m-1:
            return diff
        for i in range(4):
            newr=row+dr[i]
            newc=col+dc[i]
            if newr>=0 and newr<n and newc>=0 and newc<m:
                newEffort=max(abs(heights[row][col]-heights[newr][newc]),diff)
                if newEffort<dist[newr][newc]:
                    dist[newr][newc]=newEffort
                    heappush(minHeap,(newEffort,(newr,newc)))
    
    
    return 0
    
heights = [[1,2,2],
           [3,8,2],
           [5,3,5]]

print(MinimumEffort(heights))

                





        
        
        





        





    
