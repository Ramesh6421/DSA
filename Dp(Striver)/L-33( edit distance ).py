# edit distance
# problem: link(https://www.codingninjas.com/codestudio/problems/edit-distance_630420?source=youtube&campaign=striver_dp_videos&utm_source=youtube&utm_medium=affiliate&utm_campaign=striver_dp_videos)
'''
You are given two strings 'S' and 'T' of lengths 'N' and 'M' respectively.
Find the "Edit Distance" between the strings.
Edit Distance of two strings is the minimum number of steps required to make one string equal to the other.

In order to do so, you can perform the following three operations:
1. Delete a character
2. Replace a character with another one
3. Insert a character

Input:        Output:
s='horse'        3 
t='ros'          horse-->rorse-->ros
                 replace h->r
                 delete r,e
'''
# Recursion + Memoization
'''
TC-> O(N*M)
SC-> O(N*M) + O(N+M)
'''
def edit_dis(i,j,s,t,dp):
    if i<0:
        return j+1
    if j<0:
        return i+1
    if dp[i][j]!=-1:
        return dp[i][j]
    if s[i]==t[j]:
        dp[i][j] = edit_dis(i-1,j-1,s,t,dp)
        return dp[i][j]
    insert = 1+edit_dis(i,j-1,s,t,dp)
    delete = 1+edit_dis(i-1,j,s,t,dp)
    replace = 1+edit_dis(i-1,j-1,s,t,dp)
    dp[i][j] = min(insert,delete,replace) 
    return dp[i][j]

s='horse'
t='ros'
n=len(s)
m=len(t)
dp=[[-1 for j in range(m)]for i in range(n)]
print(edit_dis(n-1,m-1,s,t,dp))


# 1-based Indexing
def edit_dis(i,j,s,t,dp):
    if i==0:
        return j
    if j==0:
        return i
    if dp[i][j]!=-1:
        return dp[i][j]
    if s[i-1]==t[j-1]:
        dp[i][j] = edit_dis(i-1,j-1,s,t,dp)
        return dp[i][j]
    insert = 1+edit_dis(i,j-1,s,t,dp)
    delete = 1+edit_dis(i-1,j,s,t,dp)
    replace = 1+edit_dis(i-1,j-1,s,t,dp)
    dp[i][j] = min(insert,delete,replace) 
    return dp[i][j]

s='horse'
t='ros'
n=len(s)
m=len(t)
dp=[[-1 for j in range(m+1)]for i in range(n+1)]
print(edit_dis(n,m,s,t,dp))



# Tabulation
'''
TC-> O(N*M)
SC-> O(N*M) 
'''
def edit_dis(n,m,s,t,dp):
    for j in range(m+1):
        dp[0][j]=j
    for i in range(n+1):
        dp[i][0]=i
    for i in range(1,n+1):
        for j in range(1,m+1):
            if s[i-1]==t[j-1]:
                dp[i][j]=dp[i-1][j-1]
            else:
                insert = 1+dp[i][j-1]
                delete = 1+dp[i-1][j]
                replace = 1+dp[i-1][j-1]
                dp[i][j] = min(insert,delete,replace) 
    return dp[n][m]
                            
s='horse'
t='ros'
n=len(s)
m=len(t)
dp=[[0 for j in range(m+1)]for i in range(n+1)]
print(edit_dis(n,m,s,t,dp))

        

# Space Optimization
'''
TC-> O(N*M)
SC-> O(M)
'''
def edit_dis(n,m,s,t,prev):
    for j in range(m+1):
        prev[j]=j
    for i in range(1,n+1):
        cur=[0 for j in range(m+1)]
        cur[0]=i
        for j in range(1,m+1):
            if s[i-1]==t[j-1]:
                cur[j]=prev[j-1]
            else:
                insert = 1+cur[j-1]
                delete = 1+prev[j]
                replace = 1+prev[j-1]
                cur[j] = min(insert,delete,replace)
        prev=cur        
    return prev[m]
                            
s='horse'
t='ros'
n=len(s)
m=len(t)
prev=[0 for j in range(m+1)]
print(edit_dis(n,m,s,t,prev))

        

