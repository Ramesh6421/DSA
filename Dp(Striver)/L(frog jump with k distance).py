# frog jump with k distance
# notes : https://takeuforward.org/data-structure/dynamic-programming-frog-jump-with-k-distances-dp-4/
# problem : (link : https://atcoder.jp/contests/dp/tasks/dp_b)
'''
There are N stones, numbered 1,2,…,N. For each i (1≤i≤N), the height of Stone i is hi
​There is a frog who is initially on Stone 1. He will repeat the following action some number of times to reach Stone N:
If the frog is currently on Stone i, jump to one of the following: Stone i+1,i+2,…,i+K. Here, a cost of ∣hi−hj∣ is incurred,
where j is the stone to land on.
Find the minimum possible total cost incurred before the frog reaches Stone N.

Example1:                    EXample2:                  EXample2:
5 3                          3 1                        10 4
10 30 40 50 20               10 20 10                   40 10 20 70 80 10 20 70 80 60
Output:                      Output:                    Output:
30                           20                         40
∣10−30∣+∣30−20∣=30.       ∣10−20∣+∣20−10∣=20.            ∣40−70∣+∣70−70∣+∣70−60∣=40. '''

# Recursive+Memoization
'''
TC-> O(N)*k
SC-> O(N)+O(N)
'''
def jumps(i,a,k,dp):
    if i==0:
        return 0
    if i in dp:
        return dp[i]
    minsteps=10**9
    for j in range(1,k+1):
        if i-j>=0:
            jps=jumps(i-j,a,k,dp)+abs(a[i]-a[i-j])
            minsteps=min(minsteps,jps)
    dp[i]=minsteps
    return dp[i]
n,k=5,3
a=[10,30,40,50,20]
print(jumps(n-1,a,k,{}))
n,k=10,4
a=[40,10,20,70,80,10,20,70,80,60]
print(jumps(n-1,a,k,{}))
        
# Tabulation
'''
TC-> O(N)
SC-> O(N)
'''
def jumps(n,a,k,dp):
    dp[0]=0
    for i in range(1,n):
        minsteps=10**9
        for j in range(1,k+1):
            if i-j>=0:
                jps=dp[i-j]+abs(a[i]-a[i-j])
                minsteps=min(minsteps,jps)
        dp[i]=minsteps
    return dp[n-1]
n,k=5,3
a=[10,30,40,50,20]
print(jumps(n,a,k,{}))
n,k=10,4
a=[40,10,20,70,80,10,20,70,80,60]
print(jumps(n,a,k,{}))
        
