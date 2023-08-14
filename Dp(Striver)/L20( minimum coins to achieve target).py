# minimum coins to achieve target
# notes: link(https://takeuforward.org/data-structure/minimum-coins-dp-20/)
# priblem: link(https://www.codingninjas.com/codestudio/problems/minimum-elements_3843091?leftPanelTab=0)
'''
You are given an array of ‘N’ distinct integers and an integer ‘X’ representing the target sum.
You have to tell the minimum number of elements you have to take to reach the target sum ‘X’.

Note:
You have an infinite number of elements of each type.

For Example
If N=3 and X=7 and array elements are [1,2,3]. 
Way 1 - You can take 4 elements  [2, 2, 2, 1] as 2 + 2 + 2 + 1 = 7.
Way 2 - You can take 3 elements  [3, 3, 1] as 3 + 3 + 1 = 7.
Here, you can see in Way 2 we have used 3 coins to reach the target sum of 7.
Hence the output is 3.

'''
# Recursion
'''
TC-> >O(2**N)
SC-> O(X)     X is target
'''

# Recursion+Memoization
'''
TC-> O(N*X)
SC-> O(N*X)+O(N)     
'''
from sys import maxsize
def mincoins(ind,arr,k,dp):
    if ind==0:
        if k%arr[0]==0:
            return k//arr[0]
        return maxsize
    if dp[ind][k]!=-1:
        return dp[ind][k]
    nonTake=mincoins(ind-1,arr,k,dp)
    take=maxsize
    if arr[ind]<=k:
        take=1+mincoins(ind,arr,k-arr[ind],dp)
    dp[ind][k]=min(take,nonTake)
    return dp[ind][k]

n,target=3,7
nums=[1,2,3]
dp=[[-1 for i in range(target+1)]for j in range(n)]
ans=mincoins(n-1,nums,target,dp)
if ans>=maxsize:
    print(-1)
else:    
    print(ans)    


# Tabulation
'''
TC-> O(N*X)
SC-> O(N*X)     
'''
from sys import maxsize
def mincoins(n,arr,k,dp):
    for i in range(k+1):
        if i%arr[0]==0:
            dp[0][i]=i//arr[0]
        else:
            dp[0][i]=maxsize
    for i in range(1,n):
        for j in range(k+1):
            nonTake=dp[i-1][j]
            take=maxsize
            if arr[i]<=j:
                take=1+dp[i][j-arr[i]]
            dp[i][j]=min(take,nonTake)     
    return dp[n-1][k]

n,target=3,7
nums=[1,2,3]
dp=[[0 for i in range(target+1)]for j in range(n)]
ans=mincoins(n,nums,target,dp)
if ans>=maxsize:
    print(-1)
else:    
    print(ans)    


# Space Optimization
'''
TC-> O(N*X)
SC-> O(X)     
'''
from sys import maxsize
def mincoins(n,arr,k,prev):
    for i in range(k+1):
        if i%arr[0]==0:
            prev[i]=i//arr[0]
        else:
            prev[i]=maxsize
    for i in range(1,n):
        cur=[0 for i in range(k+1)]
        for j in range(k+1):
            nonTake=prev[j]
            take=maxsize
            if arr[i]<=j:
                take=1+cur[j-arr[i]]
            cur[j]=min(take,nonTake)
        prev=cur    
    return prev[k]

n,target=3,7
nums=[1,2,3]
prev=[0 for i in range(target+1)]
ans=mincoins(n,nums,target,prev)
if ans>=maxsize:
    print(-1)
else:    
    print(ans)    
