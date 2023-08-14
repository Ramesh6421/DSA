# Longest commom subsequence length
# problem: link(https://www.codingninjas.com/codestudio/problems/longest-common-subsequence_624879?source=youtube&campaign=striver_dp_videos&utm_source=youtube&utm_medium=affiliate&utm_campaign=striver_dp_videos&leftPanelTab=0)
'''
Given two strings, 'S' and 'T' with lengths 'M' and 'N',
find the length of the 'Longest Common Subsequence'.
For a string 'str'(per se) of length K,
the subsequences are the strings containing characters in the same relative order as they are present in 'str,'
but not necessarily contiguous. Subsequences contain all the strings of length varying from 0 to K.

Example :
Subsequences of string "abc" are:  ""(empty string), a, b, c, ab, bc, ac, abc.

Input:               Output:
s = adebc              3
t = dcadb              i.e, adb

'''
# Bruteforce approach
'''
  # Recursion
  -> finding all subsequences of s usi
  -> finding all subsequences of t
  -> linearly compare all subsequences(s,t), then find the maximum length.

  TC -> exponential

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
print(lcs(n-1,m-1,s1,s2,dp))



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
print(lcs(n,m,s1,s2,dp))



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
print(lcs(n,m,s1,s2,dp))



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
print(lcs(n,m,s1,s2,prev))
    
