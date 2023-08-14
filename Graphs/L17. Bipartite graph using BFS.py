#problem link(https://practice.geeksforgeeks.org/problems/bipartite-graph/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=bipartite-graph)
'''
Given an adjacency list of a graph adj  of V no. of vertices having 0 based index.
Check whether the graph is bipartite or not. 
'''
# Complexity
'''
TC-> O(V+E)
SC-> O(V)
'''

def BFS(color,adj,i):
    q=[]
    q.append(i)
    color[i]=0
    while q:
        node=q.pop(0)
        for i in adj[node]:
            if color[i]==-1:
                color[i]=not color[node]
                q.append(i)
            elif color[i]==color[node]:
                return 0
    return 1        

def isBipartite(V,adj):
    color=[-1]*V
    for i in range(V):
        if color[i]==-1:
            check=BFS(color,adj,i)
            if not check:
                return 0
    return 1

V=3
adj={0:[1],1:[0,2],2:[1]}
print(isBipartite(V,adj))
		
