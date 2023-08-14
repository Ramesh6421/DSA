# problem link(https://practice.geeksforgeeks.org/problems/detect-cycle-in-a-directed-graph/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=detect-cycle-in-a-directed-graph)
'''
Given a Directed Graph with V vertices (Numbered from 0 to V-1) and E edges,
check whether it contains any cycle or not.
'''
# Complexity
'''
TC-> O(V+E)
SC-> O(V)
'''
def topo_Bfs_Detect_Cycle(V,adj):
    indegree=[0]*V
    for i in range(V):
        for j in adj[i]:
            indegree[j]+=1
    q=[]
    for i in range(V):
        if indegree[i]==0:
            q.append(i)
        
    count=0
    while q:
        node=q.pop(0)
        count+=1
        for i in adj[node]:
            indegree[i]-=1
            if indegree[i]==0:
                q.append(i)
                
    if count==V:
        return 0
    return 1    


V=4
adj={0:[1],1:[2],2:[3],3:[3]}
print(topo_Bfs_Detect_Cycle(V,adj))

V=3
adj={0:[1],1:[2],2:[]}
print(topo_Bfs_Detect_Cycle(V,adj))

