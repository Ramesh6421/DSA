def eval_boolean(i,j,isTrue,dp):
    if i>j:
        return 0
    if i==j:
        if isTrue:
            return exp[i]=='T'
        return exp[i]=='F'
    if dp[i][j][isTrue]!=-1:
        return dp[i][j][isTrue]
    ways=0
    for ind in range(i+1,j,2):
        LT=eval_boolean(i,ind-1,1,dp)
        LF=eval_boolean(i,ind-1,0,dp)
        RT=eval_boolean(ind+1,j,1,dp)
        RF=eval_boolean(ind+1,j,0,dp)

        if exp[ind]=='&':
            if isTrue:
                ways+=(LT*RT)
            else:
                ways+=(LT*RF)+(RT*LF)+(LF*RF)
        elif exp[ind]=='|':
            if isTrue:
                ways+=(LT*RT)+(LT*RF)+(LF*RT)
            else:
                ways+=(LF*RF)
        elif exp[ind]=='^':
            if isTrue:
                ways+=(LT*RF)+(LF*RT)
            else:
                ways+=(LT*RT)+(LF*RF)
    dp[i][j][isTrue]=ways
    return ways

exp='T&T'
n=len(exp)
dp=[[[-1 for k in range(2)]for j in range(n)]for i in range(n)]
print(eval_boolean(0,n-1,1,dp))

                   
                        
        
