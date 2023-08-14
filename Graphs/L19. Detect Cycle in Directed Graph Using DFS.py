# problem link(https://practice.geeksforgeeks.org/problems/detect-cycle-in-a-directed-graph/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=detect-cycle-in-a-directed-graph)
'''
Given a Directed Graph with V vertices (Numbered from 0 to V-1) and E edges,
check whether it contains any cycle or not.

'''
# Complexity
'''
TC-> O(V+E)
SC-> O(V)+O(V) ( you can optimize as O(V) )
'''

def DFS(vis,path,adj,node):
    vis[node]=1
    path[node]=1
    for i in adj[node]:
        if vis[i]==0:
            if DFS(vis,path,adj,i)==1:
                return 1
        elif path[i]==1:
            return 1
                    
    path[node]=0        
    return 0

def Detect(V,adj):        
    vis=[0]*V
    path=[0]*V
    for i in range(V):
        if vis[i]==0:
            if DFS(vis,path,adj,i)==1:
                return 1
    return 0

V=4
adj={0:[1],1:[2],2:[3],3:[3]}
print(Detect(V,adj))

V=3
adj={0:[1],1:[2],2:[]}
print(Detect(V,adj))
