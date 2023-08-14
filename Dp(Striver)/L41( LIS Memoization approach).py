# Longest Increasing Subsequence
# Recursion + Memoization
'''
TC-> O(N*N)
SC-> O(N*N)+O(N)
'''
def LIS(ind,prev_ind,arr,n,dp):
    if ind==n:
        return 0
    if dp[ind][prev_ind]!=-1:
        return dp[ind][prev_ind]
    pick,nonpick = 0,0
    if prev_ind==-1 or arr[ind]>arr[prev_ind]:
        pick = 1 + LIS(ind+1,ind,arr,n,dp)
    nonpick = 0 + LIS(ind+1,prev_ind,arr,n,dp)
    dp[ind][prev_ind] = max(pick,nonpick)
    return dp[ind][prev_ind]

n = 8
arr = [10,9,2,5,3,7,101,18]
dp=[[-1 for j in range(n)] for i in range(n)]
print(LIS(0,-1,arr,n,dp))




