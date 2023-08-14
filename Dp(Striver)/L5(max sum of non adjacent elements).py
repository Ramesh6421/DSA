# maximum sum of non adjacent elements
# notes : https://takeuforward.org/data-structure/maximum-sum-of-non-adjacent-elements-dp-5/
# problem : (link : https://www.codingninjas.com/codestudio/problems/maximum-sum-of-non-adjacent-elements_843261?source=youtube&campaign=striver_dp_videos&utm_source=youtube&utm_medium=affiliate&utm_campaign=striver_dp_videos)
'''
You are given an array/list of ‘N’ integers.
You are supposed to return the maximum sum of the subsequence with the constraint
that no two elements are adjacent in the given array/list.

Example:                        output:
1-> 3                            
    1 2 4                         5
2-> 4                             
    2 1 4 9                       11
'''
# Recursion + Memoization
'''
TC-> O(N)
SC-> O(N)+O(N)
'''
def maximumNonAdjacentSum(nums,i,dp):    
    if i==0:
        return nums[i]
    if i<0:
        return 0
    if i in dp:
        return dp[i]
    pick=nums[i]+maximumNonAdjacentSum(nums,i-2,dp)
    nonpick=maximumNonAdjacentSum(nums,i-1,dp)
    dp[i]=max(pick,nonpick)
    return dp[i]

n=4
arr=[2,1,4,9]
print(maximumNonAdjacentSum(arr,n-1,{}))

# Tabulation
'''
TC-> O(N)
SC-> O(N)
'''
def maximumNonAdjacentSum(nums,n,dp):    
    dp[0]=nums[0]
    for i in range(1,n):
        #pick=nums[i]+dp[i-2]
        pick=nums[i]
        if i>1:
            pick+=dp[i-2]
        nonpick=dp[i-1]
        dp[i]=max(pick,nonpick)
    return dp[n-1]

n=4
arr=[2,1,4,9]
print(maximumNonAdjacentSum(arr,n,{}))

# Space Optimization
'''
TC-> O(N)
SC-> O(1)
'''
def maximumNonAdjacentSum(nums,n):    
    prev2,prev1=0,nums[0]
    for i in range(1,n):
        #pick=nums[i]+dp[i-2]
        pick=nums[i]
        if i>1:
            pick+=prev2
        nonpick=prev1
        cur=max(pick,nonpick)
        prev2=prev1
        prev1=cur
    return prev1

n=4
arr=[2,1,4,9]
print(maximumNonAdjacentSum(arr,n))

