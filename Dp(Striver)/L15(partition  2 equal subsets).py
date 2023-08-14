# problem link (link:https://www.codingninjas.com/codestudio/problems/partition-equal-subset-sum_892980?source=youtube&campaign=striver_dp_videos&utm_source=youtube&utm_medium=affiliate&utm_campaign=striver_dp_videos&leftPanelTab=0)
# notes : (https://takeuforward.org/data-structure/partition-equal-subset-sum-dp-15/)
'''
You are given an array 'ARR' of 'N' positive integers.
Your task is to find if we can partition the given array into two subsets such that the sum of elements in both subsets is equal.
For example, let’s say the given array is [2, 3, 3, 3, 4, 5],
then the array can be partitioned as [2, 3, 5], and [3, 3, 4] with equal sum 10.

Input:                        Ouput:
n = 6                         True                             
arr=[2,3,3,3,4,5]

'''
# ( SIMILAR TO PREVIOUS LECTURE L14)


# Recursion + Memoization
def partition(ind,arr,target,dp):
    if target==0:
        return True
    if ind==0:
        if target == arr[0]:
            return True
        return False
    if dp[ind][target]!=-1:
        return dp[ind][target]
    nonTake = partition(ind-1,arr,target,dp)
    take = False
    if arr[ind]<=target:
        take = partition(ind-1,arr,target-arr[ind],dp)
    dp[ind][target] = take or nonTake
    return take or nonTake
for i in range(int(input())):
    n=int(input())
    arr=[int(x) for x in input().split()]
    Sum=sum(arr)
    if Sum%2==1:
        print("False")
    else:
        target=Sum//2
        dp=[[-1 for i in range(target+1)]for j in range(n+1)]
    
        print(partition(n-1,arr,target,dp))
        
        
            
        
    
