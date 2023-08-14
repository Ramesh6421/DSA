# climbibg stairs
# notes : https://takeuforward.org/data-structure/dynamic-programming-climbing-stairs/
# problem:
'''
You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
'''
# example:
'''
Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
---------------------
Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
'''
#----------------------------------

'''
TC=O(N)
SC=O(N)+O(N)
'''
def ways(n):
    if n==0:
        return 0
    if n==1:
        return 1
    if dp[n]!=-1:
        return dp[n]
    dp[n]=ways(n-1)+ways(n-2)
    return dp[n]
n=int(input())
dp=[-1]*((n+1)+1)
print(ways(n+1))
#---------------------------------------------------------


'''
TC=O(N)
SC=O(N)
'''
def ways(n):
    dp[0]=0
    dp[1]=1
    for i in range(2,n+1):
        dp[i]=dp[i-1]+dp[i-2]
    return dp[n]
n=int(input())
dp=[-1]*((n+1)+2)
print(ways(n+1))
#------------------------------------------------------------


'''
TC=O(N)
SC=O(1)
'''
def ways(n):
    if n==0:
        return 0
    if n==1:
        return 1
    prev2=0
    prev1=1
    for i in range(2,n+1):
        cur=prev1+prev2
        prev2=prev1
        prev1=cur
    return cur
n=int(input())
print(ways(n+1))


