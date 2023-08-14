# printing the longest common subsequence string
'''
Input:
s1="adebc"
s2="dcadb"

output:
"adb"

'''
# Tabulation
'''
TC-> O(N*M)+O(N+M)
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
    

    i,j=n,m
    s=''
    while i>0 and j>0:
        if s1[i-1]==s2[j-1]:
            s=s1[i-1]+s
            i=i-1
            j=j-1
        elif dp[i-1][j]>dp[i][j-1]:
            i=i-1
        else:
            j=j-1
    return s
            

s1="adebc"
s2="dcadb"
n=len(s1)
m=len(s2)
dp=[[-1 for j in range(m+1)] for j in range(n+1)]
print(lcs(n,m,s1,s2,dp))
