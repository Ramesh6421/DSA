# Problem link(https://practice.geeksforgeeks.org/problems/implementing-floyd-warshall2042/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=implementing-floyd-warshall)
'''
The problem is to find the shortest distances between every pair of vertices in a given edge-weighted directed Graph.
The Graph is represented as an adjacency matrix, and the matrix denotes the weight of the edges (if it exists) else -1.
Do it in-place.
 
Example 1:

Input: matrix = {{0,25},{-1,0}}
Output: {{0,25},{-1,0}}
Explanation: The shortest distance between
every pair is already given(if it exists).
Example 2:

Input: matrix = {{0,1,43},{1,0,6},{-1,-1,0}}
Output: {{0,1,7},{1,0,6},{-1,-1,0}}
Explanation: We can reach 3 from 1 as 1->2->3
and the cost will be 1+6=7 which is less than 
43.

'''
# Complexity
'''
Tc-> O(N*N*N)
Sc-> O(N*N)
'''

def shortest_distance(matrix):
    
    n=len(matrix)

    for i in range(n):
        for j in range(n):
            if matrix[i][j]==-1:
                matrix[i][j]=10**9
            if i==j:
                matrix[i][j]=0
		            
    for via in range(n):
        for i in range(n):
            for j in range(n):
                matrix[i][j]=min(matrix[i][j], matrix[i][via]+matrix[via][j])
            
		                
    for i in range(n):
        for j in range(n):
            if matrix[i][j]==10**9:
                matrix[i][j]=-1

    return matrix                

matrix = [[0,2,-1,-1],[1,0,3,-1],[-1,-1,0,-1],[3,5,4,0]]
print(shortest_distance(matrix))
