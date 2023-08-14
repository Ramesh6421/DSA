'''
Given a weighted, undirected and connected graph of V vertices and E edges.
The task is to find the sum of weights of the edges of the Minimum Spanning Tree.

Example 1:

Input:

V=3
adj=[[(1,5),(2,1)],[(0,5),(2,3)],[(1,3),(0,1)]]

Output:
4
Explanation:

The Spanning Tree resulting in a weight
of 4 is shown above.


'''

# Complexity
'''
Tc-> ~ O(ElogE)
Sc-> ~ O(E)
'''
from heapq import heapify,heappush,heappop

def spanningTree(V, adj):
    minHeap=[]
    heapify(minHeap)
    vis=[0]*V
    heappush(minHeap,(0,0))
    Sum=0
    while minHeap:
        weight,node=heappop(minHeap)
        if vis[node]==1:
            continue
        vis[node]=1
        Sum+=weight
        for it in adj[node]:
            adjNode,edW=it
            if vis[adjNode]==0:
                heappush(minHeap,(edW,adjNode))
    return Sum

V=3
adj=[[(1,5),(2,1)],[(0,5),(2,3)],[(1,3),(0,1)]]

print(spanningTree(V, adj))
