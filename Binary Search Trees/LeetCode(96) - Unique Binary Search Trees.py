# problem
'''
Given an integer n, return the number of structurally unique BST's (binary search trees)
which has exactly n nodes of unique values from 1 to n.

Input: n = 3
Output: 5 
'''
# Complexity
'''
TC-> O(N*N)
SC-> O(N)
'''
def numTrees(n):
    dp=[1]*(n+1)
    for num in range(2,n+1):
        cur=0
        for ways in range(1,num+1):
            Left=ways-1
            Right=num-ways
            cur+=dp[Left]*dp[Right]
        dp[num]=cur
    return dp[n]    

n=3
ans=numTrees(n)
print(ans)
