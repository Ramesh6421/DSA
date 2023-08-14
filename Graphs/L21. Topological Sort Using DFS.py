# problem link(https://practice.geeksforgeeks.org/problems/topological-sort/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=topological-sort)
'''
Given a Directed Acyclic Graph (DAG) with V vertices and E edges,
Find any Topological Sorting of that Graph.
'''
# Complexity
'''
TC-> O(V+E)
SC-> O(V)
'''
def dfs(vis,stack,adj,node):
    vis[node]=1
    for i in adj[node]:
        if vis[i]==0:
            dfs(vis,stack,adj,i)
    stack.append(node)

def toposort(V,adj):  
    vis=[0]*V
    stack=[]
    for i in range(V):
        if vis[i]==0:
            dfs(vis,stack,adj,i)
    stack.reverse()
    return stack

V=4
adj={0:[],1:[0],2:[0],3:[0]}
print(toposort(V,adj))

V=6
adj={0:[],1:[3],2:[3],3:[],4:[0,1],5:[0,2]}
print(toposort(V,adj))
