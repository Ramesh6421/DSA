# Longest Palindromic subsequence
'''
Input:
s='bbabcbcab'

output: 'babcbab'

Approach:

It is exactly same to Longest commom subsequence.
but here we have only one string.
another one is reverse of first one
s2=reverse(s1).

'''
# Recursion + Memoization
'''
TC-> O(N*M)
SC-> O(N*M)+O(N+M)
'''
def lonpalseq(ind1,ind2,s1,s2,dp):
    if ind1==0 or ind2==0:
        return 0
    if dp[ind1][ind2]!=-1:
        return dp[ind1][ind2]
    if s1[ind1-1]==s2[ind2-1]:
        dp[ind1][ind2]=1+lonpalseq(ind1-1,ind2-1,s1,s2,dp)
        return dp[ind1][ind2]
    dp[ind1][ind2]=max(lonpalseq(ind1-1,ind2,s1,s2,dp),lonpalseq(ind1,ind2-1,s1,s2,dp))
    return dp[ind1][ind2]

s1='bbabcbcab'
s2=s1[::-1]
n=len(s1)
m=len(s2)
dp=[[-1 for j in range(m+1)] for i in range(n+1)]
print(lonpalseq(n,m,s1,s2,dp))
                       


# Tabulation
'''
TC-> O(N*M)
SC-> O(N*M)
'''
def lonpalseq(ind1,ind2,s1,s2,dp):
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
print(lonpalseq(n,m,s1,s2,dp))


# Space Optimization
'''
TC-> O(N*M)
SC-> O(M)
'''
def lonpalseq(ind1,ind2,s1,s2,prev):
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
print(lonpalseq(n,m,s1,s2,prev))
                       
                       



