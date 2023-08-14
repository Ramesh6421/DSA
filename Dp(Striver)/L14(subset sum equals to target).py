# subset sum equals to target 
# notes: (https://takeuforward.org/data-structure/subset-sum-equal-to-target-dp-14/)
# problem: link(https://www.codingninjas.com/codestudio/problems/subset-sum-equal-to-k_1550954?leftPanelTab=0)
'''
You are given an array/list ‘ARR’ of ‘N’ positive integers and an integer ‘K’.
Your task is to check if there exists a subset in ‘ARR’ with a sum equal to ‘K’.
Note: Return true if there exists a subset with sum equal to ‘K’. Otherwise, return false.

For Example :
If ‘ARR’ is {1,2,3,4} and ‘K’ = 4, then there exists 2 subsets with sum = 4.
These are {1,3} and {4}. Hence, return true.

Input:                  Output:
n,k = 4,4                True
arr = [1,2,3,4]
'''
#Recursion
'''
TC-> O(2**N)
SC-> O(N)
'''
#Recursion +Memoization
'''
TC-> O(N*K)
SC-> O(N) + O(N*K)
'''
def subsetsum(ind,arr,target,dp):
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
    notTake = subsetsum(ind-1,arr,target,dp)
    take = False
    if target>=arr[ind]:
        take = subsetsum(ind-1,arr,target-arr[ind],dp)
    dp[ind][target] = take or notTake
    return dp[ind][target]
n,k = 4,4
arr = [1,2,3,4]
dp=[[-1 for j in range(k+1)] for i in range(n+1)]
print(subsetsum(n-1,arr,k,dp))
        

#Tabulation
'''
TC-> O(N*K)
SC-> O(N*K)
'''
def subsetsum(n,arr,k,dp):
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
    return dp[n-1][k]
n,k = 4,4
arr = [1,2,3,4]
dp=[[-1 for j in range(k+1)] for i in range(n+1)]
print(subsetsum(n,arr,k,dp))
        


#Space Optimization
'''
TC-> O(N*K)
SC-> O(K)
'''
def subsetsum(n,arr,k,prev):
    for i in range(n):
        prev[0]=True
    if arr[0]<=k:    
        prev[arr[0]]=True
    for ind in range(1,n):
        cur =[0 for j in range(k+1)]
        for target in range(1,k+1):
            notTake = prev[target]
            take = False
            if target>=arr[ind]:
                take = prev[target-arr[ind]]
            cur[target] = take or notTake
        prev=cur    
    return prev[k]
n,k = 4,4
arr = [1,2,3,4]
prev=[0 for j in range(k+1)]
print(subsetsum(n,arr,k,prev))


