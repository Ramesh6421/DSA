# unbound knapsack i.e, you can take one time multiple times.
# notes: link(https://takeuforward.org/data-structure/unbounded-knapsack-dp-23/)
# problem: link(https://www.codingninjas.com/codestudio/problems/unbounded-knapsack_1215029?source=youtube&campaign=striver_dp_videos&utm_source=youtube&utm_medium=affiliate&utm_campaign=striver_dp_videos&leftPanelTab=0)
'''
You are given ‘N’ items with certain ‘PROFIT’ and ‘WEIGHT’ and a knapsack with weight capacity ‘W’.
You need to fill the knapsack with the items in such a way that you get the maximum profit.
You are allowed to take one item multiple times.

For Example,

Let us say we have 'N' = 3 items and a knapsack of capacity 'W' =  10
'PROFIT' = { 5, 11, 13 }
'WEIGHT' = { 2, 4, 6 }

We can fill the knapsack as:

1 item of weight 6 and 1 item of weight 4.
1 item of weight 6 and 2 items of weight 2.
2 items of weight 4 and 1 item of weight 2.
5 items of weight 2.

The maximum profit will be from case 3 i.e ‘27’. Therefore maximum profit = 27.
'''
# Recursion
'''
TC-> >O(2**N)
SC-> O(K)             where k is weight of bag
'''

# Recursion + Memoization
'''
TC-> O(N*K)
SC-> O(N*K)+O(N)             
'''
def unboundknap(ind,pi,wi,bw,dp):
    if ind==0:
        cur=(bw//wi[ind])*pi[ind]
        return cur
    if dp[ind][bw]!=-1:
        return dp[ind][bw]
    nonPick=unboundknap(ind-1,pi,wi,bw,dp)
    pick=0
    if wi[ind]<=bw:
        pick=pi[ind]+unboundknap(ind,pi,wi,bw-wi[ind],dp)
    dp[ind][bw]=max(pick,nonPick)    
    return max(pick,nonPick)


n,bagweight=3,10
profits=[5,11,13]
weights=[2,4,6]
dp=[[-1 for j in range(bagweight+1)] for i in range(n)]
print(unboundknap(n-1,profits,weights,bagweight,dp))


# Tabulation
'''
TC-> O(N*K)
SC-> O(N*K)         
'''
def unboundknap(n,pi,wi,bw,dp):
    for i in range(bw+1):
        dp[0][i]=(i//wi[0])*pi[0]
    for i in range(1,n):
        for j in range(bw+1):
            nonPick=dp[i-1][j]
            pick=0
            if wi[i]<=j:
                pick=pi[i]+dp[i][j-wi[i]]
            dp[i][j]=max(pick,nonPick)
    return dp[n-1][bw]
n,bagweight=3,10
profits=[5,11,13]
weights=[2,4,6]
dp=[[0 for j in range(bagweight+1)] for i in range(n)]
print(unboundknap(n,profits,weights,bagweight,dp))

            

# Space Optimization using two rows
'''
TC-> O(N*K)
SC-> O(K)         
'''
def unboundknap(n,pi,wi,bw,prev):
    for i in range(bw+1):
        prev[i]=(i//wi[0])*pi[0]
    for i in range(1,n):
        cur=[-1 for j in range(bw+1)]
        for j in range(bw+1):
            nonPick=prev[j]
            pick=0
            if wi[i]<=j:
                pick=pi[i]+cur[j-wi[i]]
            cur[j]=max(pick,nonPick)
        prev=cur    
    return prev[bw]
n,bagweight=3,10
profits=[5,11,13]
weights=[2,4,6]
prev=[0 for j in range(bagweight+1)]
print(unboundknap(n,profits,weights,bagweight,prev))


# Space Optimization using one row
'''
TC-> O(N*K)
SC-> O(K)         
'''
def unboundknap(n,pi,wi,bw,prev):
    for i in range(wi[0],bw+1):
        prev[i]=(i//wi[0])*pi[0]
    for i in range(1,n):
        for j in range(bw+1):
            nonPick=prev[j]
            pick=0
            if wi[i]<=j:
                pick=pi[i]+prev[j-wi[i]]
            prev[j]=max(pick,nonPick)  
    return prev[bw]
n,bagweight=3,10
profits=[5,11,13]
weights=[2,4,6]
prev=[0 for j in range(bagweight+1)]
print(unboundknap(n,profits,weights,bagweight,prev))

            

