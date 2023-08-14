# Problem link(https://practice.geeksforgeeks.org/problems/detect-cycle-in-an-undirected-graph/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=detect-cycle-in-an-undirected-graph)
'''
Given an undirected graph with V vertices and E edges,
check whether it contains any cycle or not. 
'''
# Complexity
'''
TC-> O(N+2E)+O(N)
SC-> O(N)+O(N) ~ O(N)
'''
def DFS(vis,adj,node,parent):
    vis[node]=1
    for i in adj[node]:
        if vis[i]==0:
            if DFS(vis,adj,i,node)==True:
                return True
        else:
            if i!=parent:
                return True
		    
		    
def IsCycle(V,adj):
    vis=[0]*V
    for i in range(V):
        if vis[i]==0:
            ans=DFS(vis,adj,i,-1)
            if ans==True:
                return True
    return False           
V=7
adj={0:[1,2],
     1:[0,4],
     2:[0,3,5],
     3:[2],
     4:[1,6],
     5:[2,6],
     6:[4,5]
     }

ans=IsCycle(V,adj)
print(ans)
