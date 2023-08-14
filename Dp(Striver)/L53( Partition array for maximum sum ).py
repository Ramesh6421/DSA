# problem
'''
Given an integer array arr, partition the array into (contiguous) subarrays of length at most k.
After partitioning, each subarray has their values changed to become the maximum value of that subarray.
Return the largest sum of the given array after partitioning.

Example 1:

Input: arr = [1,15,7,9,2,5,10], k = 3
Output: 84
Explanation: arr becomes [15,15,15,9,10,10,10]
Example 2:

Input: arr = [1,4,1,5,7,3,6,1,9,9,3], k = 4
Output: 83
Example 3:

Input: arr = [1], k = 1
Output: 1
'''

# Recursion+Memoization
'''
TC-> O(N)*O(K)
SC-> O(N)+O(N)
'''
def max_parti(i,n,dp):
    if i==n:
        return 0
    if dp[i]!=-1:
        return dp[i]
    ans=0
    Len=0
    maxele=0
    for j in range(i,min(n,i+k)):
        Len+=1
        maxele=max(arr[j],maxele)
        cur=(maxele*Len)+max_parti(j+1,n,dp)
        ans=max(ans,cur)
    dp[i]=ans
    return ans
arr=[1,15,7,9,2,5,10]
k=3
n=len(arr)
dp=[-1 for j in range(n)]
print(max_parti(0,n,dp))


#Tabulation
'''
TC-> O(N)*O(K)
SC-> O(N)
'''
def max_parti(n,arr):
    dp=[0 for i in range(n+1)]
    for i in range(n-1,-1,-1):
        ans=0
        Len=0
        maxele=0
        for j in range(i,min(n,i+k)):
            Len+=1
            maxele=max(arr[j],maxele)
            cur=(maxele*Len)+dp[j+1]
            ans=max(ans,cur)
        dp[i]=ans
    return dp[0]

arr=[1,15,7,9,2,5,10]
k=3
n=len(arr)
print(max_parti(n,arr))
