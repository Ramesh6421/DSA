# rod cutting problem
# notes: link()
# problem: link(https://www.codingninjas.com/codestudio/problems/rod-cutting-problem_800284?source=youtube&campaign=striver_dp_videos&utm_source=youtube&utm_medium=affiliate&utm_campaign=striver_dp_videos&leftPanelTab=0)
'''
Given a rod of length ‘N’ units.
The rod can be cut into different sizes and each size has a cost associated with it.
Determine the maximum cost obtained by cutting the rod and selling its pieces.
Note:
1. The sizes will range from 1 to ‘N’ and will be integers.
2. The sum of the pieces cut should be equal to ‘N’.
3. Consider 1-based indexing.

Input:                       Output:
N=5                            12
costs=[2,5,7,8,10]

Explanation:
All possible partitions are:
1,1,1,1,1           max_cost=(2+2+2+2+2)=10
1,1,1,2             max_cost=(2+2+2+5)=11
1,1,3               max_cost=(2+2+7)=11
1,4                 max_cost=(2+8)=10
5                   max_cost=(10)=10
2,3                 max_cost=(5+7)=12
1,2,2               max _cost=(2+5+5)=12    

Clearly, if we cut the rod into lengths 1,2,2, or 2,3, we get the maximum cost which is 12.


'''

# Recursion
'''
TC-> >O(2**N)
SC-> O(N)
'''

# Recursion Memoization
'''
TC-> O(N*N)
SC-> O(N*N)+O(N)
'''
def rodcut(ind,n,arr,dp):
    if ind==0:
        return n*arr[0]
    if dp[ind][n]!=-1:
        return dp[ind][n]
    nonPick=rodcut(ind-1,n,arr,dp)
    pick=0
    rodlen=ind+1
    if rodlen<=n:
        pick=arr[ind]+rodcut(ind,n-rodlen,arr,dp)
    dp[ind][n]=max(pick,nonPick)    
    return max(pick,nonPick)

n=5
arr=[2,5,7,8,10]
dp=[[-1 for j in range(n+1)] for i in range(n)]
print(rodcut(n-1,n,arr,dp))



# Tabulation
'''
TC-> O(N*N)
SC-> O(N*N)
'''
def rodcut(n,arr,dp):
    for i in range(n+1):
        dp[0][i]=i*arr[0]
    for i in range(1,n):
        for j in range(n+1):
            nonPick=dp[i-1][j]
            pick=0
            rodlen=i+1
            if rodlen<=j:
                pick=arr[i]+dp[i][j-rodlen]
            dp[i][j]=max(pick,nonPick)
    return dp[n-1][n]

            
n=5
arr=[2,5,7,8,10]
dp=[[0 for j in range(n+1)] for i in range(n)]
print(rodcut(n,arr,dp))



# Space Optimization using two rows
'''
TC-> O(N*N)
SC-> O(N)
'''
def rodcut(n,arr,prev):
    for i in range(n+1):
        prev[i]=i*arr[0]
    for i in range(1,n):
        cur=[0 for j in range(n+1)]
        for j in range(n+1):
            nonPick=prev[j]
            pick=0
            rodlen=i+1
            if rodlen<=j:
                pick=arr[i]+cur[j-rodlen]
            cur[j]=max(pick,nonPick)
        prev=cur    
    return prev[n]

            
n=5
arr=[2,5,7,8,10]
prev=[0 for j in range(n+1)]
print(rodcut(n,arr,prev))
    
    

# Space Optimization using one row
'''
TC-> O(N*N)
SC-> O(N)
'''
def rodcut(n,arr,prev):
    for i in range(n+1):
        prev[i]=i*arr[0]
    for i in range(1,n):
        for j in range(n+1):
            nonPick=prev[j]
            pick=0
            rodlen=i+1
            if rodlen<=j:
                pick=arr[i]+prev[j-rodlen]
            prev[j]=max(pick,nonPick) 
    return prev[n]

            
n=5
arr=[2,5,7,8,10]
prev=[0 for j in range(n+1)]
print(rodcut(n,arr,prev))
    
