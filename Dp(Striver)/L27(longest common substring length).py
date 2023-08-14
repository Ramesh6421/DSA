# Longest common substring length
'''
s1 = 'abcd'
s2 = 'abxd'

output:
length=2
string='ab'

'''
# Tabulation
'''
TC-> O(N*M)
SC-> O(N*M)
'''
def lcsub(n,m,s1,s2,dp):
    for i in range(n):
        dp[i][0]=0
    for j in range(m):
        dp[0][j]=0
    ans=0
    for i in range(1,n+1):
        for j in range(1,m+1):
            if s1[i-1]==s2[j-1]:
                dp[i][j]=1+dp[i-1][j-1]
            else:
                dp[i][j]=0
            ans=max(ans,dp[i][j])
    return ans

s1='abcd'
s2='abxd'
n=len(s1)
m=len(s2)
dp=[[0 for j in range(m+1)] for i in range(n+1)]
print(lcsub(n,m,s1,s2,dp))
        

# Space Optimization
'''
TC-> O(N*M)
SC-> O(M)
'''
def lcsub(n,m,s1,s2,prev):
    ans=0
    for i in range(1,n+1):
        cur=[0 for j in range(m+1)] 
        for j in range(1,m+1):
            if s1[i-1]==s2[j-1]:
                cur[j]=1+prev[j-1]
            else:
                cur[j]=0
            ans=max(ans,cur[j])
        prev=cur    
    return ans

s1='abcd'
s2='abcd'
n=len(s1)
m=len(s2)
prev=[0 for j in range(m+1)] 
print(lcsub(n,m,s1,s2,prev))
        
        
    
