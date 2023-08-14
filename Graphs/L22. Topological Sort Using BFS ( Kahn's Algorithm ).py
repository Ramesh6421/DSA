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
def topo_BFS(V,adj):
    indegree=[0]*V
    for i in range(V):
        for j in adj[i]:
            indegree[j]+=1
            
    q=[]
    for i in range(V):
        if indegree[i]==0:
            q.append(i)
        
    topo=[]
    while q:
        node=q.pop(0)
        topo.append(node)
        for i in adj[node]:
            indegree[i]-=1
            if indegree[i]==0:
                q.append(i)
    return topo

V=4
adj={0:[],1:[0],2:[0],3:[0]}
print(topo_BFS(V,adj))

V=6
adj={0:[],1:[3],2:[3],3:[],4:[0,1],5:[0,2]}
print(topo_BFS(V,adj))
