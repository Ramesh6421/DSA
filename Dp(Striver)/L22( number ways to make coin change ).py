# number of ways to make coin change
# notes: link(https://takeuforward.org/data-structure/coin-change-2-dp-22/)
# problem: link(https://www.codingninjas.com/codestudio/problems/ways-to-make-coin-change_630471?source=youtube&campaign=striver_dp_videos&utm_source=youtube&utm_medium=affiliate&utm_campaign=striver_dp_videos&leftPanelTab=0)
'''
You are given an infinite supply of coins of each of denominations D = {D0, D1, D2, D3, ...... Dn-1}.
You need to figure out the total number of ways W,
in which you can make a change for value V using coins of denominations from D. Print 0, if a change isn't possible.

Example:
Input:              output:
n=3,k=4               4
arr=[1,2,3]          i.e,[1,1,1,1],[1,2,1],[2,2][1,3]

'''

# Recursion
'''
TC-> >O(2**N)
SC-> O(K)     X is target
'''

# Recursion+Memoization
'''
TC-> O(N*K)
SC-> O(N*K)+O(N)     
'''
def ways(ind,arr,k,dp):
    if ind==0:
        if k%arr[0]==0:
            return 1
        return 0
    if dp[ind][k]!=-1:
        return dp[ind][k]
    nonPick=ways(ind-1,arr,k,dp)
    pick=0
    if arr[ind]<=k:
        pick=ways(ind,arr,k-arr[ind],dp)
    dp[ind][k]=pick+nonPick  
    return pick+nonPick

n,k=3,4
arr=[1,2,3]
dp=[[-1 for j in range(k+1)] for i in range(n)]
print(ways(n-1,arr,k,dp))

# Tabulation
'''
TC-> O(N*K)
SC-> O(N*K)     
'''
def ways(n,arr,k,dp):
    for i in range(k+1):
        if i%arr[0]==0:
            dp[0][i]=1
    for i in range(1,n):
        for j in range(k+1):
            nonPick=dp[i-1][j]
            pick=0
            if arr[i]<=j:
                pick=dp[i][j-arr[i]]
            dp[i][j]=pick+nonPick
    return dp[n-1][k]
n,k=3,4
arr=[1,2,3]
dp=[[0 for j in range(k+1)] for i in range(n)]
print(ways(n,arr,k,dp))


# Space Optimization
'''
TC-> O(N*K)
SC-> O(K)     
'''
def ways(n,arr,k,prev):
    for i in range(k+1):
        if i%arr[0]==0:
            prev[i]=1
    for i in range(1,n):
        cur=[0 for j in range(k+1)]
        for j in range(k+1):
            nonPick=prev[j]
            pick=0
            if arr[i]<=j:
                pick=cur[j-arr[i]]
            cur[j]=pick+nonPick
        prev=cur    
    return prev[k]
n,k=3,4
arr=[1,2,3]
prev=[0 for j in range(k+1)]
print(ways(n,arr,k,prev))
        
        

        
