# minimum path in triangle | single starting and multiple destinations
# problem : link (https://www.codingninjas.com/codestudio/problems/triangle_1229398?source=youtube&campaign=striver_dp_videos&utm_source=youtube&utm_medium=affiliate&utm_campaign=striver_dp_videos&leftPanelTab=0)
'''
You are given a triangular array/list 'TRIANGLE'.
Your task is to return the minimum path sum to reach from the top to the bottom row.
The triangle array will have N rows and the i-th row, where 0 <= i < N will have i + 1 elements.
You can move only to the adjacent number of row below each step.
For example, if you are at index j in row i, then you can move to i or i + 1 index in row j + 1 in each step.

For Example :
If the array given is 'TRIANGLE' = [[1], [2,3], [3,6,7], [8,9,6,10]] the triangle array will look like:

1
2,3
3,6,7
8,9,6,10

For the given triangle array the minimum sum path would be 1->2->3->8. Hence the answer would be 14.

'''

# Recursion + Memoization
'''
TC-> O(N*N)
SC-> O(N) + O(N*N)
'''
def minpath(triangle,row,col,n,dp):
    if row == n-1:
        return triangle[row][col]
    if dp[row][col]!=-1:
        return dp[row][col]
    down = triangle[row][col] + minpath(triangle,row+1,col,n,dp)
    diagonal = triangle[row][col] + minpath(triangle,row+1,col+1,n,dp)
    minn=min(down,diagonal)
    dp[row][col]=minn
    return minn

triangle = [[1], [2,3], [3,6,7], [8,9,6,10]]
n = 4
dp = [[-1 for j in range(i+1)] for i in range(n)]
print(minpath(triangle,0,0,n,dp))

# Tabulation
'''
TC-> O(N*N)
SC-> O(N*N)
'''
def minpath(triangle,n,dp):
    for i in range(n):
        dp[n-1][i] = triangle[n-1][i]
    for i in range(n-2,-1,-1):
        for j in range(i,-1,-1):
            down = triangle[i][j] + dp[i+1][j]
            diagonal = triangle[i][j] + dp[i+1][j+1]
            minn = min(down,diagonal)
            dp[i][j] = minn
    return dp[0][0]

            
    
triangle = [[1], [2,3], [3,6,7], [8,9,6,10]]
n = 4
dp = [[-1 for j in range(i+1)] for i in range(n)]
print(minpath(triangle,n,dp))


# Space Optimization
'''
TC-> O(N*N)
SC-> O(N)
'''
def minpath(triangle,n,prev):
    for i in range(n):
        prev[i] = triangle[n-1][i]
    for i in range(n-2,-1,-1):
        temp = [-1 for j in range(n)]
        for j in range(i,-1,-1):
            down = triangle[i][j] + prev[j]
            diagonal = triangle[i][j] + prev[j+1]
            minn = min(down,diagonal)
            temp[j] = minn
        prev = temp    
    return prev[0]

            
    
triangle = [[1], [2,3], [3,6,7], [8,9,6,10]]
n = 4
prev = [-1 for j in range(n)]
print(minpath(triangle,n,prev))


