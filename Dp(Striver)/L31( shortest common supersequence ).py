# Shortest Common Supersequence
# problem: link(https://www.codingninjas.com/codestudio/problems/shortest-supersequence_4244493?source=youtube&campaign=striver_dp_videos&utm_source=youtube&utm_medium=affiliate&utm_campaign=striver_dp_videos)
'''
Given two strings, ‘A’ and ‘B’. Return the shortest supersequence string ‘S’, containing both ‘A’ and ‘B’ as its subsequences.
If there are multiple answers, return any of them.
Note: A string 's' is a subsequence of string 't' if deleting some number of characters from 't' (possibly 0) results in the string 's'.

For Example:
Suppose ‘A’ = “brute”, and ‘B’ = “groot”

The shortest supersequence will be “bgruoote”. As shown below, it contains both ‘A’ and ‘B’ as subsequences.

A   A A     A A
b g r u o o t e
  B B   B B B  

It can be proved that the length of supersequence for this input cannot be less than 8. So the output will be bgruoote.

'''


# Tabulation
'''
TC-> O(N*M)+O(N+M)
Sc-> O(N*M)
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
    length =(n+m)-(dp[n][m])
    print(length)

    i,j=n,m
    s=''
    while i>0 and j>0:
        if s1[i-1]==s2[j-1]:
            s=s1[i-1]+s
            i=i-1
            j=j-1
        elif dp[i-1][j]>dp[i][j-1]:
            s=s1[i-1]+s
            i=i-1
        else:
            s=s2[j-1]+s
            j=j-1
    while i>0:
        s=s1[i-1]+s
        i=i-1
    while j>0:
        s=s2[j-1]+s
        j=j-1
    return s

s1='brute'
s2='groot'
n=len(s1)
m=len(s2)
dp=[[0 for j in range(m+1)] for i in range(n+1)]
print(lcs(n,m,s1,s2,dp))
s1='bleed'
s2='blue'
n=len(s1)
m=len(s2)
dp=[[0 for j in range(m+1)] for i in range(n+1)]
print(lcs(n,m,s1,s2,dp))
