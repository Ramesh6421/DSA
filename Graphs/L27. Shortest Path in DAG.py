def toposort_DFS(vis,stack,adj,node):
    vis[node]=1
    for v,w in adj[node]:
        if vis[v]==0:
            toposort_DFS(vis,stack,adj,v)
    stack.append(node)

def Shortest_Path_In_DAG(N,M,edges):
    adj={i:[] for i in range(N)}
    for i in edges:
        u,v,w=i
        adj[u].append((v,w))

    vis=[0]*N
    stack=[]
    for i in range(N):
        if vis[i]==0:
            toposort_DFS(vis,stack,adj,i)
    
    dist=[10**9]*N
    src=0
    dist[src]=0
    while stack:
        node=stack.pop()
        for v,w in adj[node]:
            if dist[node]+w < dist[v]:
                dist[v]=dist[node]+w
    return dist

N=6
M=7
edges=[[0,1,2],[0,4,1],[4,5,4],[4,2,2],[1,2,3],[2,3,6],[5,3,1]] #[u,v,w]
print(Shortest_Path_In_DAG(N,M,edges))        
        
        
