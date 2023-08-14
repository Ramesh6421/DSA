# matrix chain multiplication
# problem: link(https://www.codingninjas.com/codestudio/problems/matrix-chain-multiplication_975344?source=youtube&campaign=striver_dp_videos&utm_source=youtube&utm_medium=affiliate&utm_campaign=striver_dp_videos&leftPanelTab=1)
'''
Given a chain of matrices A1, A2, A3,.....An.
Your task is to find out the minimum cost to multiply these matrices.
The cost of matrix multiplication is defined as the number of scalar multiplications.
A Chain of matrices A1, A2, A3,.....An is represented by a sequence of numbers in an array ‘arr’
where the dimension of 1st matrix is equal to arr[0] * arr[1] , 2nd matrix is arr[1] * arr[2], and so on.

For example:
For arr[ ] = { 10, 20, 30, 40}, matrix A1 = [10 * 20], A2 = [20 * 30], A3 = [30 * 40]

Scalar multiplication of matrix with dimension 10 * 20 is equal to 200.

TestCase:

n=4
arr=[4,5,3,2]

In the first test case, there are three matrices of dimensions A = [4 5], B = [5 3] and C = [3 2].
The most efficient order of multiplication is A * ( B * C).
Cost of ( B * C ) = 5 * 3 * 2 = 30  and (B * C) = [5 2] and A * (B * C) = [ 4 5] * [5 2] = 4 * 5 * 2 = 40.
So the overall cost is equal to 30 + 40 =70.


'''
# Recursion + Memoization
'''
TC-> O(N*N)+O(N)
SC->O(N*N)+O(N)+O(N)
'''
def mcm(i,j,dp):
    if i==j:
        return 0
    if dp[i][j]!=-1:
        return dp[i][j]
    minn=10**9
    for k in range(i,j):
        steps=(arr[i-1]*arr[k]*arr[j])+mcm(i,k,dp)+mcm(k+1,j,dp)
        minn=min(minn,steps)
    dp[i][j]=minn
    return minn

arr=[10,20,30,40,50]
n=len(arr)
dp=[[-1 for j in range(n)]for i in range(n)]
print(mcm(1,n-1,dp))
        
# Tabulation
'''
TC-> O(N*N)+O(N)
SC->O(N*N)+O(N)
'''
def mcm(n,arr):
    dp=[[0 for j in range(n)]for i in range(n)]
    for i in range(1,n):
        dp[i][i]=0
    for i in range(n-1,0,-1):
        for j in range(i+1,n):
            minn=10**9
            for k in range(i,j):
                steps=arr[i-1]*arr[k]*arr[j]+dp[i][k]+dp[k+1][j]
                minn=min(minn,steps)
            dp[i][j]=minn          
    return dp[1][n-1]

arr=[10,20,30,40,50]
n=len(arr)
print(mcm(n,arr))
