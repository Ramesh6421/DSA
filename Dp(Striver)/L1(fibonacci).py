# Nth Fibonacci number
# BLOG : https://takeuforward.org/data-structure/dynamic-programming-introduction/

'''
TC=O(N)
SC=O(N)+O(N)
'''
def fibo(n):
    if n==0:
        return 0
    if n==1:
        return 1
    if dp[n]!=-1:
        return dp[n]
    dp[n]=fibo(n-1)+fibo(n-2)
    return dp[n]
n=int(input())
dp=[-1]*(n+1)
print(fibo(n))
#---------------------------------------------------------


'''
TC=O(N)
SC=O(N)
'''
def fibo(n):
    dp[0]=0
    dp[1]=1
    for i in range(2,n+1):
        dp[i]=dp[i-1]+dp[i-2]
    return dp[n]
n=int(input())
dp=[-1]*(n+2)
print(fibo(n))
#------------------------------------------------------------


'''
TC=O(N)
SC=O(1)
'''
def fibo(n):
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
print(fibo(n))


