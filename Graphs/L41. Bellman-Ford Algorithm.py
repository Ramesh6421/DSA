# Problem link()
'''
Given a weighted, directed and connected graph of V vertices and E edges,
Find the shortest distance of all the vertex's from the source vertex S.
Note: If the Graph contains a negative cycle then return an array consisting of only -1.

E = [[0,1,5],[1,0,3],[1,2,-1],[2,0,1]]
S = 2
Output:
1 6 0
Explanation:
For nodes 2 to 0, we can follow the path-
2-0. This has a distance of 1.
For nodes 2 to 1, we cam follow the path-
2-0-1, which has a distance of 1+5 = 6,

'''

# Complexity
'''
TC-> O(V*E)
SC-> O(V)
'''

def Bellman_Ford(V, edges, S):
    
    dist=[10**8]*V
    dist[S]=0
        
    for i in range(V-1):
        for u,v,w in edges:
            if dist[u]!=10**8 and dist[u]+w<dist[v]:
                dist[v]=dist[u]+w
                    
    for u,v,w in edges:
        if dist[u]!=10**8 and dist[u]+w<dist[v]:
            return [-1]
                
    return dist

V = 2
E = [[0,1,9]]
S = 0
print(Bellman_Ford(V, E, S))
