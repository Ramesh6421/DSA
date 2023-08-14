# Problem link(https://practice.geeksforgeeks.org/problems/shortest-path-in-weighted-undirected-graph/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=shortest-path-in-weighted-undirected-graph)
'''
You are given a weighted undirected graph having n vertices and m edges
describing there are edges between a to b with some weight,
find the shortest path between the vertex 1 and the vertex n and
if path does not exist then return a list consisting of only -1.

Example:
Input:
n = 5, m= 6
edges = [[1,2,2], [2,5,5], [2,3,4], [1,4,1],[4,3,3],[3,5,1]]
Output:
1 4 3 5
Explaination:
Shortest path from 1 to n is by the path 1 4 3 5
'''
# Complexity
'''
TC-> O(ElogV)
SC-> O(V)+O(V)
'''

from heapq import heapify,heappop,heappush

def shortestPath(n, m, edges):
    
    adj={}
    for i in range(n):
        adj[i+1]=[]
    for u,v,w in edges:
        if u in adj:
            adj[u].append((v,w))
        else:
            adj[u]=[(v,w)]
        if v in adj:
3            adj[v].append((u,w))
        else:
            adj[v]=[(u,w)]
            
    mark_parent={}
    for i in range(n):
        mark_parent[i+1]=i+1
        
    dist=[float("inf")]*(n+1)
    dist[1]=0
    minHeap=[]
    heapify(minHeap)
    heappush(minHeap,(0,1))
    
    while minHeap:
        dis,node=heappop(minHeap)
        for it in adj[node]:
            edgeWeight=it[1]
            adjNode=it[0]
            if dis+edgeWeight<dist[adjNode]:
                dist[adjNode]=dis+edgeWeight
                heappush(minHeap,(dist[adjNode],adjNode))
                mark_parent[adjNode]=node
                  
    res=[]
    if dist[n]==float("inf"):
        return [-1]
    else:
        path=[]
        node=n
        while mark_parent[node]!=node:
            path.append(node)
            node=mark_parent[node]
        path.append(node)
        path.reverse()
        return path      
           

n=5
m=6
edges=[[1,2,2],
       [2,5,5],
       [2,3,4],
       [1,4,1],
       [4,3,3],
       [3,5,1]
       ]

print(shortestPath(n,m,edges))







