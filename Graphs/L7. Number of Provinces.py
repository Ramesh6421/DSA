# problem link(https://practice.geeksforgeeks.org/problems/number-of-provinces/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=number_of_provinces)
# notes link(https://takeuforward.org/data-structure/number-of-provinces/)
'''
Given an undirected graph with V vertices.
We say two vertices u and v belong to a single province if there is a path from u to v or v to u.
Your task is to find the number of provinces.
'''
# Complexity
'''
TC-> O(N) + O(N+2E)
SC-> O(N) + O(N)
'''
def DFS(vis,adj,node):
    vis[node]=1
    if node in adj:
        for it in adj[node]:
            if vis[it]==0:
                DFS(vis,adj,it)

def Provinces(adj,N):
    vis=[0]*N
    count=0
    for i in range(N):
        if vis[i]==0:
            count+=1
            DFS(vis,adj,i)
    return count

N=8
adj={0:[1],
     1:[0,2],
     2:[1],
     3:[4],
     4:[3,5],
     5:[4],
     6:[7],
     7:[6]
    }
ans=Provinces(adj,N)
print(ans)
