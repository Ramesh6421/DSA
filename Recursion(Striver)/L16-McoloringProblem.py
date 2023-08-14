'''
M-coloring problem
determine if the graph can be colored with at most M colors
such that no adjacent vertices of the graph are colored
with the same color.

'''
def isSafe(node,colourDict,graph,n,color):
    for edge in graph[node]:         
        if colourDict[edge]==color:                      # checking adjacent nodes {holding the same color or not}
            return False
    return True

def solve(node,coloutDict,m,n,graph):
    if node==n:                                          # if node reaches n means all the nodes are colored 
        return True
    for color in range(1,m+1):                            # iterating each color 
        if isSafe(node,colourDict,graph,n,color):         # checking which color is satisfied
            colourDict[node]=color
            if solve(node+1,colourDict,m,n,graph):        # recursive call with next node
                return True
            colourDict[node]=0                             # Backtracking
    return False        
        
graph={0:[1,2,3],1:[2,3,0],2:[0,1],3:[0,1]}
n=4
m=3
colourDict={0:0,1:0,2:0,3:0}
ans=solve(0,colourDict,m,n,graph)
#print(colourDict)
print(ans)
