# Problem link(https://practice.geeksforgeeks.org/problems/depth-first-traversal-for-a-graph/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=dfs_of_graph)
# notes link(https://takeuforward.org/data-structure/depth-first-search-dfs/)
'''
Given a connected undirected graph.
Perform a Depth First Traversal of the graph.
'''
# Complexity
'''
TC-> O(N) + 2E
SC-> O(3N) ~ N
'''
def DFS(vis,adj,node,dfs):
    vis[node]=1
    dfs.append(node)
    for it in adj[node]:
        if vis[it]==0:
            DFS(vis,adj,it,dfs)
    return dfs

N = 5
adj = {0:[1,2,3],
       1:[0],
       2:[0,4],
       3:[0],
       4:[2]
       }
dfs=[]
vis=[0]*N
print(DFS(vis,adj,0,dfs))
