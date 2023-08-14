# burst balloons
# problem: link(https://www.codingninjas.com/codestudio/problems/mining-diamonds_4244494?source=youtube&campaign=striver_dp_videos&utm_source=youtube&utm_medium=affiliate&utm_campaign=striver_dp_videos)
'''
There are ‘N’ diamonds in a mine. The size of each diamond is given in the form of integer array ‘A’.
If the miner mines a diamond,
then he gets 'size of previous unmined diamond * size of currently mined diamond * size of next unmined diamond' number of coins.
If there isn’t any next or previous unmined diamond then their size is replaced by 1 while calculating the number of coins.
Vladimir, a dumb miner was assigned the task to mine all diamonds.
Since he is dumb he asks for your help to determine the maximum number of coins that he can earn by mining the diamonds in an optimal order.

For Example:
Suppose ‘N’ = 3, and ‘A’ = [7, 1, 8]

The optimal order for mining diamonds will be [2, 1, 3].
State of mine -    [7, 1, 8]    [7, 8]    [8]
Coins earned -    (7*1*8) + (1*7*8) + (1*8*1)  = 56 + 56 + 8 = 120
Hence output will be 120.

'''

# Recursion + Memoization
'''
TC-> O(N*N)*O(N)
SC-> O(N*N)+O(N)
'''
from sys import maxsize
def burst(i,j,dp):
    if i>j:
        return 0
    if dp[i][j]!=-1:
        return dp[i][j]
    maxx=-maxsize
    for k in range(i,j+1):
        cost=a[i-1]*a[k]*a[j+1]+burst(i,k-1,dp)+burst(k+1,j,dp)
        maxx=max(maxx,cost)
    dp[i][j]=maxx
    return maxx

n=3
a=[7,1,8]
a.insert(0,1)
a.insert(-1,1)
dp=[[-1 for j in range(n+1)]for i in range(n+1)]
print(burst(1,3,dp))


# Tabulation
'''
TC-> O(N*N)*O(N)
SC-> O(N*N)
'''
def burst(n,a):
    dp=[[0 for j in range(n+2)]for i in range(n+2)]
    for i in range(n,0,-1):
        for j in range(1,n+1):
            if i>j:
                dp[i][j]=0
            else:
                maxx=-maxsize
                for k in range(i,j+1):
                    cost=a[i-1]*a[k]*a[j+1]+dp[i][k-1]+dp[k+1][j]
                    maxx=max(maxx,cost)
                dp[i][j]=maxx
    return dp[1][n]

                
n=3
a=[7,1,8]
a.insert(0,1)
a.insert(-1,1)
print(burst(n,a))
                    
