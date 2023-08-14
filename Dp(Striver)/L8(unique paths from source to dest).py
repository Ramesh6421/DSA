# unique paths from source to destniation
# problem: link(https://www.codingninjas.com/codestudio/problems/total-unique-paths_1081470?source=youtube&campaign=striver_dp_videos&utm_source=youtube&utm_medium=affiliate&utm_campaign=striver_dp_videos&leftPanelTab=1)
'''
You are present at point ‘A’ which is the top-left cell of an M X N matrix,
your destination is point ‘B’, which is the bottom-right cell of the same matrix.
Your task is to find the total number of unique paths from point ‘A’ to point ‘B’.
In other words, you will be given the dimensions of the matrix as integers ‘M’ and ‘N’,
your task is to find the total number of unique paths from the cell MATRIX[0][0] to MATRIX['M' - 1]['N' - 1].
To traverse in the matrix, you can either move Right or Down at each step.
For example in a given point MATRIX[i] [j], you can move to either MATRIX[i + 1][j] or MATRIX[i][j + 1].

Input:    output:
2       
2 2         2
1 1         1
3 2         3
1 6         1

'''

# Recursion + Memoization
'''
TC-> O(N*M)
SC-> O((M-1)+(N-1)) + O(M*N)
'''
def paths(row,col,dp):
    if row==0 and col==0:
        return 1
    if row<0 or col<0:
        return 0
    if dp[row][col]!=-1:
        return dp[row][col]
    up=paths(row-1,col,dp)
    left=paths(row,col-1,dp)
    dp[row][col]=up+left
    return up+left

m,n= 2,2 
dp=[[-1 for i in range(n)] for j in range(m)]
print(paths(m-1,n-1,dp))


# Tabulation
'''
TC-> O(M*N)
SC-> O(M*N)
'''
def paths(row,col,dp):
    for i in range(m):
        for j in range(n):
            if i==0 and j==0:
                dp[i][j]=1
            else:
                up=0
                left=0
                if i>0:
                    left=dp[i-1][j]
                if j>0:
                    up=dp[i][j-1]
                dp[i][j]=left+up
    return dp[m-1][n-1]            
    

m,n= 2,2
dp=[[-1 for i in range(n)] for j in range(m)]
print(paths(m,n,dp))


# space optimization
'''
TC-> O(M*N)
SC-> O(M)
'''
def paths( row,col,prev):
    for i in range(m):
        temp=[-1 for i in range(n)]
        for j in range(n):
            if i==0 and j==0:
                temp[j]=1
            else:
                up=0
                left=0
                if i>0:
                    up=prev[j]
                if j>0:
                    left=temp[j-1]
                temp[j]=left+up
        prev=temp        
    return prev[n-1]            
    

m,n= 3,3
prev=[-1 for i in range(n)]
print(paths(m,n,prev))

