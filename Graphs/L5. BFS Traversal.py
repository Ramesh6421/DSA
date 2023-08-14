# BFS link(https://practice.geeksforgeeks.org/problems/bfs-traversal-of-graph/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=bfs_of_graph)
# notes link(https://takeuforward.org/graph/breadth-first-search-bfs-level-order-traversal/)
'''
Given a directed graph.
The task is to do Breadth First Traversal of this graph starting from 0.
'''
# Approach - 1
# Complexity
'''
TC-> O(N)+ 2E
SC-> O(3N)~ N
'''
def getBFS(adj,N):
    vis=[0]*N
    q=[]
    q.append(0)   # appending starting node
    bfs=[]
    while q:
        node=q.pop(0)
        bfs.append(node)
        for i in adj[node]:
            if vis[i]==0:
                vis[i]=1
                q.append(i)
    return bfs

N=5
adj={0:[1,2,3],
     1:[],
     2:[4],
     3:[],
     4:[]
     }
BFS=getBFS(adj,N)
print(BFS)            # output = [0,1,2,3,4]



#--------------------------------------------------------------------------
# Approach - 2
# Complexity
'''
TC-> O(N)+ 2E
SC-> O(3N)~ N
'''
def bfsOfGraph(adj,N):
    vis=[0]*N
    bfs=[]
    q=[] 
    q.append(0)
    while q:
        size=len(q)
        level=[]
        for i in range(size):
            node=q.pop(0)
            level.append(node)
            for i in adj[node]:
                if vis[i]==0:
                    vis[i]=1
                    q.append(i)
        bfs.append(level)
            
    return bfs        

N=5
adj={0:[1,2,3],
     1:[],
     2:[4],
     3:[],
     4:[]
     }
BFS=bfsOfGraph(adj,N)
print(BFS)            # output = [[0], [1, 2, 3], [4]]


                
    
