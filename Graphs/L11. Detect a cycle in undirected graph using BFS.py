# problem
'''
Given an undirected graph with V vertices and E edges,
check whether it contains any cycle or not. 
'''

# Complexity
'''
TC-> O(N+2E)+O(N) ~ O(N+2E)
SC-> O(N)+O(N) ~ O(N)
'''

def BFS(vis,adj,node):
    vis[node]=1
    q=[]
    q.append((node,-1))
    while q:
        node,parent=q.pop(0)
        for i in adj[node]:
            if vis[i]==0:
                vis[i]=1
                q.append((i,node))
            else:
                if parent!=i:
                    return True
    return False

def IsCycle(V,adj):
    vis=[0]*V    
    for i in range(V):
        if vis[i]==0:
            ans=BFS(vis,adj,i)
            if ans==1:
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
