# wildcard Matching
# problem: link(https://www.codingninjas.com/codestudio/problems/wildcard-pattern-matching_701650?source=youtube&campaign=striver_dp_videos&utm_source=youtube&utm_medium=affiliate&utm_campaign=striver_dp_videos)
'''
Given a text and a wildcard pattern of size N and M respectively,
implement a wildcard pattern matching algorithm that finds if the wildcard pattern is matched with the text.
The matching should cover the entire text not partial text.

The wildcard pattern can include the characters ‘?’ and ‘*’
 ‘?’ – matches any single character 
 ‘*’ – Matches any sequence of characters(sequence can be of length 0 or more)

Sample Input 1:                    Sample Output 1:
3
?ay
ray                                      True     
ab*cd
abdefcd                                  True
ab?d
abcc                                     False


Explanation Of The Sample Input1:
Test Case 1:
The pattern is “?ay” and the text is ray.
‘?’ can match a character so it matches with a character ‘r’ of the text and rest of the text matches with the pattern so we print True.

Test Case 2:
“ab” of text matches with “ab” of pattern and then ‘*’ of pattern matches with “def” of the text and “cd” of text matches with “cd” of the pattern. Whole text matches with the pattern so we print True.

Test Case 3:
“ab” of pattern matches with “ab” of text. ‘?’ of pattern matches with ‘c’ of the text but ‘d’ of the pattern do not match with ‘c’ of the text so we print False.

'''
# Recursion + Memoization
'''
TC-> O(N*M)
SC-> O(N*M) + O(N+M)
'''
def wildcard(i,j,s,t,dp):
    if i<0 and j<0:
        return True
    if i<0 and j>=0:
        return False
    if j<0 and i>=0:
        for k in range(i+1):
            if s[k]!='*':
                return False
        return True
    if dp[i][j]!=-1:
        return dp[i][j]
    if s[i]==t[j] or s[i]=='?':
        dp[i][j] = wildcard(i-1,j-1,s,t,dp)
        return dp[i][j]
    if s[i]=='*':
        dp[i][j]=wildcard(i-1,j,s,t,dp) or wildcard(i,j-1,s,t,dp)
        return dp[i][j]
    return False


s='ab*cd'
t='abdefcd'
n=len(s)
m=len(t)
dp=[[-1 for j in range(m)] for i in range(n)]
print(wildcard(n-1,m-1,s,t,dp))



# 1-based Indexing
def wildcard(i,j,s,t,dp):
    if i==0 and j==0:
        return True
    if i==0 and j>0:
        return False
    if j==0 and i>0:
        for k in range(1,i+1):
            if s[k-1]!='*':
                return False
        return True
    if dp[i][j]!=-1:
        return dp[i][j]
    if s[i-1]==t[j-1] or s[i-1]=='?':
        dp[i][j] = wildcard(i-1,j-1,s,t,dp)
        return dp[i][j]
    if s[i-1]=='*':
        dp[i][j]=wildcard(i-1,j,s,t,dp) or wildcard(i,j-1,s,t,dp)
        return dp[i][j]
    return False


s='ab*cd'
t='abdefcd'
n=len(s)
m=len(t)
dp=[[-1 for j in range(m+1)] for i in range(n+1)]
print(wildcard(n,m,s,t,dp))



# Tabulation
'''
TC-> O(N*M)
SC-> O(N*M) 
'''

def wildcard(n,m,s,t,dp):
    dp[0][0]=True
    for j in range(1,m+1):
        dp[0][j]=False
    for i in range(1,n+1):
        flag=True
        for k in range(1,i+1):
            if s[k-1]!='*':
                flag=False
                break
        dp[i][0]=flag
    for i in range(1,n+1):
        for j in range(1,m+1):
            if s[i-1]==t[j-1] or s[i-1]=='?':
                dp[i][j]=dp[i-1][j-1]
            elif s[i-1]=='*':
                dp[i][j]=dp[i-1][j] or dp[i][j-1]
            else:
                dp[i][j]=False    
    return dp[n][m]        


s='ab*cd'
t='abdefcd'
n=len(s)
m=len(t)
dp=[[-1 for j in range(m+1)] for i in range(n+1)]
print(wildcard(n,m,s,t,dp))



# Space Optimization
'''
TC-> O(N*M)
SC-> O(M)
'''

def wildcard(n,m,s,t,prev):
    prev[0]=True
    for j in range(1,m+1):
        prev[j]=False
    for i in range(1,n+1):
        cur=[0 for j in range(m+1)]
        flag=True
        for k in range(1,i+1):
            if s[k-1]!='*':
                flag=False
                break
        cur[0]=flag
        for j in range(1,m+1):
            if s[i-1]==t[j-1] or s[i-1]=='?':
                cur[j]=prev[j-1]
            elif s[i-1]=='*':
                cur[j]=prev[j] or cur[j-1]
            else:
                cur[j]=False
        prev=cur        
    return prev[m]        



s='ab*cd'
t='abdefcd'
n=len(s)
m=len(t)
prev=[0 for j in range(m+1)]
print(wildcard(n,m,s,t,prev))
