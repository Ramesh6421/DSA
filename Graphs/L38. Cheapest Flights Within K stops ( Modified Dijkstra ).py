# problem link(https://practice.geeksforgeeks.org/problems/cheapest-flights-within-k-stops/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=cheapest-flights-within-k-stops)
'''
There are n cities and m edges connected by some number of flights.
You are given an array flights where flights[i] = [fromi, toi, pricei]
indicates that there is a flight from city fromi to city toi with cost pricei.

You are also given three integers src, dst, and k,
return the cheapest price from src to dst with at most k stops. If there is no such route, return -1.

Example 1:
Input:
n = 4
flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]]
src = 0
dst = 3
k = 1
Output:
700
Explaination:
The optimal path with at most 1 stop from city 0 to 3 is marked in red and has cost 100 + 600 = 700.
Note that the path through cities [0,1,2,3] is cheaper but is invalid because it uses 2 stops.

'''
# Complexity
'''
TC-> O(E)
SC-> O(V)
'''


def CheapestFlight(n,flights,src,dest,k):
    
    adj={}
    for it in flights:
        start,end,price=it
        if start in adj:
            adj[start].append((end,price))
        else:
            adj[start]=[(end,price)]
            
    q=[]
    q.append((0,(src,0)))
    dist=[10**9]*n
    dist[src]=0
    
    while q:
        
        stops,pair=q.pop(0)
        node,cost=pair
        
        if stops>k:
            continue

        for it in adj[node]:
            adjNode,weight=it

            if cost+weight<dist[adjNode]:
                dist[adjNode]=cost+weight
                q.append((stops+1,(adjNode,dist[adjNode])))
                
    if dist[dest]==10**9:
        return -1
    return dist[dest]

n = 4
flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]]
src = 0                      
dest = 3
k = 1                          
print(CheapestFlight(n,flights,src,dest,k))            
            
        
    
