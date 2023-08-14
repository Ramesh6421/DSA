# Problem link(https://practice.geeksforgeeks.org/problems/number-of-ways-to-arrive-at-destination/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=/number-of-ways-to-arrive-at-destination)
'''
You are in a city that consists of n intersections numbered from 0 to n - 1
with bi-directional roads between some intersections.
The inputs are generated such that you can reach any intersection from any other intersection
and that there is at most one road between any two intersections.

You are given an integer n and a 2D integer array roads where roads[i] = [ui, vi, timei]
means that there is a road between intersections ui and vi that takes timei minutes to travel.
You want to know in how many ways you can travel from intersection 0 to intersection n - 1 in the shortest amount of time.

Return the number of ways you can arrive at your destination in the shortest amount of time.
Since the answer may be large, return it modulo 109 + 7.

Example 1:

Input:
n=7, m=10
edges= [[0,6,7],[0,1,2],[1,2,3],[1,3,3],[6,3,3],[3,5,1],[6,5,1],[2,5,1],[0,4,5],[4,6,2]]

Output:
4
Explaination:

The four ways to get there in 7 minutes are:
- 0  6
- 0  4  6
- 0  1  2  5  6
- 0  1  3  5  6

'''

# Complexity
'''
TC-> O(ElogV)
SC-> O(V)+O(V)
'''


from heapq import heapify,heappush,heappop

def countPaths(n,roads):
    
    adj={}
    for u,v,w in roads:
        
        if u in adj:
            adj[u].append((v,w))
        else:
            adj[u]=[(v,w)]
            
        if v in adj:
            adj[v].append((u,w))
        else:
            adj[v]=[(u,w)]
        
    minHeap=[]
    heappush(minHeap,(0,0))
    
    dist=[10**9]*n
    ways=[0]*n
    dist[0]=0
    ways[0]=1
        
    while minHeap:
        dis,node=heappop(minHeap)
        
        if node in adj:
            for v,w in adj[node]:
                
                if dis+w<dist[v]:
                    dist[v]=dis+w
                    heappush(minHeap,(dist[v],v))
                    ways[v]=ways[node]
                    
                elif dis+w==dist[v]:
                    ways[v]=ways[v]+ways[node]
                    
    return ways[n-1]            
                    

n=7
m=10
edges= [[0,6,7],[0,1,2],[1,2,3],[1,3,3],[6,3,3],[3,5,1],[6,5,1],[2,5,1],[0,4,5],[4,6,2]]
print(countPaths(n,edges))

    
