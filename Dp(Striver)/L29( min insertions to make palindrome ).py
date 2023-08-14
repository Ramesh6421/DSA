# minimum insertions to make given string to palindrome
# problem: link(https://www.codingninjas.com/codestudio/problems/minimum-insertions-to-make-palindrome_985293?source=youtube&campaign=striver_dp_videos&utm_source=youtube&utm_medium=affiliate&utm_campaign=striver_dp_videos)
'''
A palindrome string is one that reads the same backward as well as forward.
Given a string 'STR', you need to tell the minimum number of characters needed to insert into it to make it a palindromic string.

For example:
String 'STR' = “abcaa” can be converted into a palindrome by inserting 2 characters. So the final string becomes “aabcbaa”.

'''
# Recursion+Memoization
'''
TC-> O(N*M)
SC-> O(N*M)+O(N+M)
'''
def lps(ind1,ind2,s1,s2,dp):
    if ind1==0 or ind2==0:
        return 0
    if dp[ind1][ind2]!=-1:
        return dp[ind1][ind2]
    if s1[ind1-1]==s2[ind2-1]:
        dp[ind1][ind2]=1+lps(ind1-1,ind2-1,s1,s2,dp)
        return dp[ind1][ind2]
    dp[ind1][ind2]=max(lps(ind1-1,ind2,s1,s2,dp),lps(ind1,ind2-1,s1,s2,dp))
    return dp[ind1][ind2]

s1='codingninjas'
s2=s1[::-1]
n=len(s1)
m=len(s2)
dp=[[-1 for j in range(m+1)] for i in range(n+1)]
length = lps(n,m,s1,s2,dp)
print(n-length)


# Tabulation
'''
TC-> O(N*M)
SC-> O(N*M)
'''
def lps(ind1,ind2,s1,s2,dp):
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
                             
                
s1='bbabcbcab'
s2=s1[::-1]
n=len(s1)
m=len(s2)
dp=[[0 for j in range(m+1)] for i in range(n+1)]
length=lps(n,m,s1,s2,dp)
print(n-length)


# Space Optimization
'''
TC-> O(N*M)
SC-> O(M)
'''
def lps(ind1,ind2,s1,s2,prev):
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
                             
                
s1='bbabcbcab'
s2=s1[::-1]
n=len(s1)
m=len(s2)
prev=[0 for j in range(m+1)]
length=lps(n,m,s1,s2,prev)
print(n-length)
                       
                       



