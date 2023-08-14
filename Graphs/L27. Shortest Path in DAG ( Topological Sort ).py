def toposort_DFS(vis,stack,adj,node):
    vis[node]=1
    for v,w in adj[node]:
        if vis[v]==0:
            toposort_DFS(vis,stack,adj,v)
    stack.append(node)

def Shortest_Path_In_DAG(N,M,edges,src):
    adj={i:[] for i in range(N)}
    for i in edges:
        u,v,w=i
        adj[u].append((v,w))

    vis=[0]*N
    stack=[]
    for i in range(N):
        if vis[i]==0:
            toposort_DFS(vis,stack,adj,i)
    
    dist=[float("inf")]*N
    dist[src]=0
    while stack:
        node=stack.pop()
        for v,w in adj[node]:
            if dist[node]+w < dist[v]:
                dist[v]=dist[node]+w
    for i in range(N):
        if dist[i]==float("inf"):
            dist[i]=-1            # marking -1 as unreachable nodes
    return dist

N=6
M=7
src=0
edges=[[0,1,2],[0,4,1],[4,5,4],[4,2,2],[1,2,3],[2,3,6],[5,3,1]] #[u,v,w]
print(Shortest_Path_In_DAG(N,M,edges,src))

N=7
M=8
src=6
edges=[[0,1,2],[1,3,1],[2,3,3],[4,0,3],[4,2,1],[5,4,1],[6,4,2],[6,5,3]]
print(Shortest_Path_In_DAG(N,M,edges,src))
        
        
