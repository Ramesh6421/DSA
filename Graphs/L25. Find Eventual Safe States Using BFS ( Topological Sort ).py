# Problem link(https://practice.geeksforgeeks.org/problems/eventual-safe-states/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=eventual-safe-states)
'''
A directed graph of V vertices and E edges is given in the form of an adjacency list adj.
Each node of the graph is labelled with a distinct integer in the range 0 to V - 1.
A node is a terminal node if there are no outgoing edges.
A node is a safe node if every possible path starting from that node leads to a terminal node.
You have to return an array containing all the safe nodes of the graph. The answer should be sorted in ascending order.
'''

# Complexity
'''
TC-> O(V+E) + (VlogV)
SC-> O(V) + O(V+E)
'''

def eventual_safe_States_BFS(V,adj):
    adjrev={}
    for i in range(V):
        adjrev[i]=[]
    for i in range(V):
        for j in adj[i]:
            adjrev[j].append(i)
                
    indegree=[0]*V
    for i in range(V):
        for j in adjrev[i]:
            indegree[j]+=1
    q=[]
    for i in range(V):
        if indegree[i]==0:
            q.append(i)
            
    topo=[]
    while q:
        node=q.pop(0)
        topo.append(node)
        for i in adjrev[node]:
            indegree[i]-=1
            if indegree[i]==0:
                q.append(i)
        
    topo.sort()            
    return topo

V=7
adj={0:[1,2],1:[2,3],2:[5],3:[0],4:[5],5:[],6:[]}
print(eventual_safe_States_BFS(V,adj))
        
