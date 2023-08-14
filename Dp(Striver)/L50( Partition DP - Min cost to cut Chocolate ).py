# problem: link(https://www.codingninjas.com/codestudio/problems/cost-to-cut-a-chocolate_3208460?source=youtube&campaign=striver_dp_videos&utm_source=youtube&utm_medium=affiliate&utm_campaign=striver_dp_videos&leftPanelTab=0)
'''
You are given chocolate of ‘N’ length. The chocolate is labeled from 0 to ‘N’.
You are also given an array ‘CUTS’ of size ‘C’, denoting the positions at which you can do a cut.
The order of cuts can be changed. The cost of one cut is the length of the chocolate to be cut.
Therefore, the total cost is the sum of all the cuts. Print the minimum cost to cut the chocolate.

Note:
All the integers in the ‘CUTS’ array are distinct.

For Example:
Let ‘N’ be: 4
Let the ‘CUTS’ array be: [1, 3].

Let the order of doing the cut be [1, 3].
The first cut of 1 on length 4 results in a cost of 4,
and chocolate is split into two parts of the length of 1 and 3.
The second cut of 3 on length 3 results in a cost of 3,
and chocolate is split into two parts again of the length of 2 and 1. So the total cost is 7.

The cost will remain the same if we change the order of cutting. So the result is 7.

'''

# Recursion+Memoization
'''
TC-> O(N*N)*O(N)
SC-> O(N*N)+O(N)
'''
from sys import maxsize
def min_cuts(i,j,dp):
    if i>j:
        return 0
    if dp[i][j]!=-1:
        return dp[i][j]
    minn=maxsize
    for k in range(i,j+1):
        cost=cuts[j+1]-cuts[i-1]+min_cuts(i,k-1,dp)+min_cuts(k+1,j,dp)
        minn=min(minn,cost)
    dp[i][j]=minn
    return minn
cuts=[1,3,4]
c=len(cuts)
n=5
cuts.insert(0,0)
cuts.insert(-1,n)
cuts.sort()
dp=[[-1 for j in range(c+1)]for i in range(c+1)]
print(min_cuts(1,c,dp))


# Tabulation
'''
TC-> O(N*N)*(N)
SC-> O(N*N)
'''
def min_cuts(n,c,cuts):
    dp=[[0 for j in range(c+2)]for i in range(c+2)]
    for i in range(c,0,-1):
        for j in range(1,c+1):
            if i>j:
                dp[i][j]=0
            else:
                minn=maxsize
                for k in range(i,j+1):
                    cost=cuts[j+1]-cuts[i-1]+dp[i][k-1]+dp[k+1][j]
                    minn=min(cost,minn)
                dp[i][j]=minn
    return dp[1][c]            
                    
cuts=[1,3,4]
c=len(cuts)
n=5
cuts.insert(0,0)
cuts.insert(-1,n)
cuts.sort()
print(min_cuts(n,c,cuts))
                
