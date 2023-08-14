# Problem link()
'''
There are n cities numbered from 0 to n-1. Given the array edges where edges[i] = [fromi , toi ,weighti]
represents a bidirectional and weighted edge between cities fromi and toi,
and given the integer distance Threshold. You need to find out a city with the smallest number of cities
that are reachable through some path and whose distance is at most Threshold Distance,
If there are multiple such cities,our answer will be the city with the greatest number.

Note: that the distance of a path connecting cities i and j is equal to the sum of the edges' weights along that path.

Input:
N=4,M=4
edges = [[0,1,3],[1,2,1],[1,3,4],[2,3,1]]
distanceThreshold = 4
Output:3
Explaination:The neighboring cities at a distanceThreshold = 4 for each city are:
City 0 -> [City 1, City 2] 
City 1 -> [City 0, City 2, City 3] 
City 2 -> [City 0, City 1, City 3] 
City 3 -> [City 1, City 2] 
Cities 0 and 3 have 2 neighboring cities at a distanceThreshold = 4,
but we have to return city 3 since it has the greatest number.
'''

# Complexity
'''
TC-> O(N*N*N)+O(N*N) ~ O(N^3)
SC-> O(N*N)
'''

def findCity(n,m,edges,distanceThreshold):
    dist=[[10**9 for j in range(n)]for i in range(n)]
    for u,v,w in edges:
        dist[u][v]=w
        dist[v][u]=w
        
    for i in range(n):
        dist[i][i]=0
    for via in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][via]==10**9 or dist[via][j]==10**9:
                    continue
                else:
                    dist[i][j]=min(dist[i][j],dist[i][via]+dist[via][j])
                       
        
    cntcity=n
    cityno=-1
    for i in range(n):
        count=0
        for j in dist[i]:
            if j<=distanceThreshold:
                count+=1
        if count<=cntcity:
                cntcity=count
                cityno=i
            
    return cityno        
                
N=4
M=4
edges = [[0,1,3],[1,2,1],[1,3,4],[2,3,1]]
distanceThreshold = 4
print(findCity(N,M,edges,distanceThreshold))
