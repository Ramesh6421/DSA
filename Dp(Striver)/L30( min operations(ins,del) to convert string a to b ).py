# minimum operations to convert string a to b
# problem: link(https://www.codingninjas.com/codestudio/problems/can-you-make_4244510?source=youtube&campaign=striver_dp_videos&utm_source=youtube&utm_medium=affiliate&utm_campaign=striver_dp_videos)

'''
You are given 2 non-empty strings “str” and “ptr” consisting of lowercase English alphabets only.
Your task is to convert string “str” into string “ptr”. In one operation you can do either of the following on “str”:
Remove a character from any position in “str”.
Add a character to any position in “str”.
You have to find the minimum number of operations required to convert string “str” into “ptr”.

For Example:
If str = “abcd”, ptr = “anc”
In one operation remove str[3], after this operation str becomes “abc”.    
In the second operation remove str[1], after this operation str becomes “ac”.
In the third operation add ‘n’ in str[1], after this operation str becomes “anc”.

Hence, the output will be 3.

'''
# Recursion+Memoization
'''
TC-> O(N*M)
SC-> O(N*M)+O(N+M)
'''
def lcs(ind1,ind2,s1,s2,dp):
    if ind1<0 or ind2<0:
        return 0
    if dp[ind1][ind2]!=-1:
        return dp[ind1][ind2]
    if s1[ind1]==s2[ind2]:
        dp[ind1][ind2]=1+lcs(ind1-1,ind2-1,s1,s2,dp)
        return dp[ind1][ind2]
    dp[ind1][ind2]=max(lcs(ind1-1,ind2,s1,s2,dp),lcs(ind1,ind2-1,s1,s2,dp))
    return dp[ind1][ind2]

s1="adebc"
s2="dcadb"
n=len(s1)
m=len(s2)
dp=[[-1 for j in range(m)] for j in range(n)]
length = lcs(n-1,m-1,s1,s2,dp)
print(n+m-(2*length))



# Shifting index -1 to 0
def lcs(ind1,ind2,s1,s2,dp):
    if ind1==0 or ind2==0:
        return 0
    if dp[ind1][ind2]!=-1:
        return dp[ind1][ind2]
    if s1[ind1-1]==s2[ind2-1]:
        dp[ind1][ind2]=1+lcs(ind1-1,ind2-1,s1,s2,dp)
        return dp[ind1][ind2]
    dp[ind1][ind2]=max(lcs(ind1-1,ind2,s1,s2,dp),lcs(ind1,ind2-1,s1,s2,dp))
    return dp[ind1][ind2]

s1="adebc"
s2="dcadb"
n=len(s1)
m=len(s2)
dp=[[-1 for j in range(m+1)] for j in range(n+1)]
length = lcs(n,m,s1,s2,dp)
print(n+m-(2*length))


# Tabulation
'''
TC-> O(N*M)
SC-> O(N*M)
'''
def lcs(n,m,s1,s2,dp):
    for i in range(n):
        dp[i][0]=0
    for j in range(m):
        dp[0][j]=0
    for i in range(1,n+1):
        for j in range(1,m+1):
            if s1[i-1]==s2[j-1]:
                dp[i][j]=1+dp[i-1][j-1]
            else:    
                dp[i][j]=max(dp[i-1][j],dp[i][j-1])
    return dp[n][m]

s1="adebc"
s2="dcadb"
n=len(s1)
m=len(s2)
dp=[[-1 for j in range(m+1)] for j in range(n+1)]
length = lcs(n,m,s1,s2,dp)
print(n+m-(2*length))


# Space Optimization
'''
TC-> O(N*M)
SC-> O(M)
'''
def lcs(n,m,s1,s2,prev):
    #for i in range(n):
    #   prev[0]=0
    for j in range(m):
        prev[j]=0
    for i in range(1,n+1):
        cur=[0 for j in range(m+1)]
        for j in range(1,m+1):
            if s1[i-1]==s2[j-1]:
                cur[j]=1+prev[j-1]
            else:    
                cur[j]=max(prev[j],cur[j-1])
        prev=cur        
    return prev[m]

s1="adebc"
s2="dcadb"
n=len(s1)
m=len(s2)
prev=[0 for j in range(m+1)]
length = lcs(n,m,s1,s2,prev)
print(n+m-(2*length))    
