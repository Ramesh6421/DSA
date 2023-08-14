# 0/1 knapsack
# notes: link(https://takeuforward.org/data-structure/0-1-knapsack-dp-19/)
# problem: link(https://www.codingninjas.com/codestudio/problems/0-1-knapsack_920542?source=youtube&campaign=striver_dp_videos&utm_source=youtube&utm_medium=affiliate&utm_campaign=striver_dp_videos&leftPanelTab=0)
'''
A thief is robbing a store and can carry a maximal weight of W into his knapsack.
There are N items and the ith item weighs wi and is of value vi.
Considering the constraints of the maximum weight that a knapsack can carry,
you have to find and return the maximum value that a thief can generate by stealing items.

Example,
Input:

n = 4                                 output:
weights = [1,2,4,5]                     13
values = [5,4,8,6]
bagweight = 5

'''
#Recursion
'''
TC-> O()2**N)
SC-> O(N)
'''

#Recursion + Memoization
'''
TC-> O(N*W)
SC-> O(N*W)+O(N)
'''
def knapsack(ind,bw,wi,vi,dp):
    if ind==0:
        if wi[ind]<=bw:
            return vi[ind]
        return 0
    if dp[ind][bw]!=-1:
        return dp[ind][bw]
    nonTake=knapsack(ind-1,bw,wi,vi,dp)
    take=-10**9+7
    if wi[ind]<=bw:
        take=vi[ind]+knapsack(ind-1,bw-wi[ind],wi,vi,dp)
    dp[ind][bw]=max(take,nonTake)    
    return max(take,nonTake)

n=4
weights=[1,2,4,5]
values=[5,4,8,6]
bagweight=5
dp=[[-1 for j in range(bagweight+1)]for i in range(n)]
print(knapsack(n-1,bagweight,weights,values,dp))


#Tabulation
'''
TC-> O(N*W)
SC-> O(N*W)
'''
def knapsack(n,bw,wi,vi,dp):
    for i in range(wi[0],bw+1):
        dp[0][i]=vi[0]
    for i in range(1,n):
        for j in range(bw+1):
            nonTake=dp[i-1][j]
            take=-10**9+7
            if wi[i]<=j:
                take=vi[i]+dp[i-1][j-wi[i]]
            dp[i][j]=max(take,nonTake)
    return dp[n-1][bw]

n=4
weights=[1,2,4,5]
values=[5,4,8,6]
bagweight=5
dp=[[0 for j in range(bagweight+1)]for i in range(n)]
print(knapsack(n,bagweight,weights,values,dp))
                    

#Space Optimization with two rows
'''
TC-> O(N*W)
SC-> O(W)
'''
def knapsack(n,bw,wi,vi,prev):
    for i in range(wi[0],bw+1):
        prev[i]=vi[0]
    for i in range(1,n):
        cur=[0 for j in range(bw+1)]
        for j in range(bw+1):
            nonTake=prev[j]
            take=-10**9+7
            if wi[i]<=j:
                take=vi[i]+prev[j-wi[i]]
            cur[j]=max(take,nonTake)
        prev=cur    
    return prev[bw]

n=4
weights=[1,2,4,5]
values=[5,4,8,6]
bagweight=5
prev=[0 for j in range(bagweight+1)]
print(knapsack(n,bagweight,weights,values,prev))



#Space Optimization with one row
'''
TC-> O(N*W)
SC-> O(W)
'''
def knapsack(n,bw,wi,vi,prev):
    for i in range(wi[0],bw+1):
        prev[i]=vi[0]
    for i in range(1,n):
        for j in range(bw,-1,-1):
            nonTake=prev[j]
            take=-10**9+7
            if wi[i]<=j:
                take=vi[i]+prev[j-wi[i]]
            prev[j]=max(take,nonTake)
    return prev[bw]

n=4
weights=[1,2,4,5]
values=[5,4,8,6]
bagweight=5
prev=[0 for j in range(bagweight+1)]
print(knapsack(n,bagweight,weights,values,prev))
                    
