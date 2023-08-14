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
TC-> O(V+E)+O(V)
SC-> O(V)*3
'''
def DFS(vis,path,check,adj,node):
    vis[node]=1
    path[node]=1
    check[node]=0
    for i in adj[node]:
        if vis[i]==0:
            if DFS(vis,path,check,adj,i)==1:
                check[i]=0                      # marking cycle nodes as 0
                return 1
        elif path[i]==1:
            check[i]=0            # marking cycle nodes as 0
            return 1
                    
    check[node]=1              # marking no cycle nodes as 1            
    path[node]=0        
    return 0

def eventualSafeNodes(V,adj):        
    vis=[0]*V
    path=[0]*V
    check=[0]*V
    for i in range(V):
        if vis[i]==0:
            DFS(vis,path,check,adj,i)
                    
    safenodes=[]
    for i in range(V):
        if check[i]==1:
            safenodes.append(i)
    return safenodes        

V=7
adj={0:[1,2],1:[2,3],2:[5],3:[0],4:[5],5:[],6:[]}
print(eventualSafeNodes(V,adj))
