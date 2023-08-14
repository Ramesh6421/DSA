# problem: link(https://www.codingninjas.com/codestudio/problems/partition-a-set-into-two-subsets-such-that-the-difference-of-subset-sums-is-minimum_842494?source=youtube&campaign=striver_dp_videos&utm_source=youtube&utm_medium=affiliate&utm_campaign=striver_dp_videos&leftPanelTab=0)
# notes: (https://takeuforward.org/data-structure/partition-set-into-2-subsets-with-min-absolute-sum-diff-dp-16/)
'''
You are given an array containing N non-negative integers.
Your task is to partition this array into two subsets such that the absolute difference between subset sums is minimum.
You just need to find the minimum absolute difference considering any valid division of the array elements.
Note:
1. Each element of the array should belong to exactly one of the subset.
2. Subsets need not be contiguous always. For example,
   for the array : {1,2,3}, some of the possible divisions are a) {1,2} and {3}  b) {1,3} and {2}.
3. Subset-sum is the sum of all the elements in that subset. 

Input:            output:
N=4                  0
arr=[1,2,3,4]
'''
#Recursion + Memoization
'''
TC-> O(N*K)+O(K)+O(K)
SC-> O(N*K)+O(K)
'''
def minparti(ind,arr,target,dp):
    if target==0:
        dp[ind][target]=True
        return True
    if ind==0:
        if target==arr[ind]:
            dp[ind][target]=True
            return True 
        return False
    if dp[ind][target]!=-1:
        return dp[ind][target]
    notTake = minparti(ind-1,arr,target,dp)
    take = False
    if target>=arr[ind]:
        take = minparti(ind-1,arr,target-arr[ind],dp)
    dp[ind][target] = take or notTake
    return dp[ind][target]
n= 3
arr = [2,3,7]
k=sum(arr)
if n==0 or k==0:
    print(0)
else:    
    dp=[[-1 for j in range(k+1)] for i in range(n+1)]
    dummy=[True]*(k+1)
    for i in range(1,k+1):
        dummy[i]=minparti(n-1,arr,i,dp)
    minn=10**9
    for i in range(k):
        if dummy[i]==True:
            diff=abs((k-i)-i)
            minn=min(diff,minn)
    print(minn)        
    


# Tabulation
'''
TC-> O(N*K)+O(K)
SC-> O(N*K)
'''
def minparti(n,arr,k,dp):
    for i in range(n):
        dp[i][0]=True
    if arr[0]<=k:    
        dp[0][arr[0]]=True
    for ind in range(1,n):
        for target in range(1,k+1):
            
            notTake = dp[ind-1][target]
            take = False
            if target>=arr[ind]:
                take = dp[ind-1][target-arr[ind]]
            dp[ind][target] = take or notTake
    minn=10**9
    for i in range(k):
        if dp[n-1][i]==True:
            diff=abs(i-(k-i))
            minn=min(minn,diff)
    return minn        
n= 3
arr = [2,3,7]
k=sum(arr)
if n==0 or k==0:
    print(0)
else:    
    dp=[[0 for j in range(k+1)] for i in range(n+1)]
    print(minparti(n,arr,k,dp))
