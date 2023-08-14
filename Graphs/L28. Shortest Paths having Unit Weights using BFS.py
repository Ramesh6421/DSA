# problem link()
'''
You are given an Undirected Graph having unit weight,
Find the shortest path from src(0) to all the vertex and if it is unreachable to reach any vertex,
then return -1 for that vertex.

Input:

V=9
adj={0:[1,3],1:[0,2,3],2:[1,6],3:[0,4],4:[3,5],5:[4,6],6:[2,5,7,8],7:[6,8],8:[6]}
src=0

Output:

[0, 1, 2, 1, 2, 3, 3, 4, 4]

'''

# Complexity
'''
TC-> O(V+2E)
SC-> O(V)+O(V)
'''
def ShortestPath_having_unitWeights_BFS(V,adj,src):
    dist=[float("inf")]*V
    dist[src]=0
    q=[]
    q=[src]
    while q:
        node=q.pop(0)
        for v in adj[node]:
            if dist[node]+1 < dist[v]:
                dist[v]=dist[node]+1
                q.append(v)
    
    for i in range(V):
        if dist[i]==float("inf"):
            dist[i]=-1
    return dist

V=9
adj={0:[1,3],1:[0,2,3],2:[1,6],3:[0,4],4:[3,5],5:[4,6],6:[2,5,7,8],7:[6,8],8:[6]}
src=0
print(ShortestPath_having_unitWeights_BFS(V,adj,src))
    
