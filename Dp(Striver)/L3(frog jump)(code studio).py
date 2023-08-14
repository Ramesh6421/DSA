#Frog jump (code studio)
#notes :https://takeuforward.org/data-structure/dynamic-programming-frog-jump-dp-3/
#problem
'''
There is a frog on the 1st step of an N stairs long staircase. The frog wants to reach the Nth stair.
HEIGHT[i] is the height of the (i+1)th stair.If Frog jumps from ith to jth stair,
the energy lost in the jump is given by |HEIGHT[i-1] - HEIGHT[j-1] |.In the Frog is on ith staircase,
he can jump either to (i+1)th stair or to (i+2)th stair.
Your task is to find the minimum total energy used by the frog to reach from 1st stair to Nth stair.  '''
#example
'''
Input:
4
10 20 30 10

Output:
20

Explanation:
The frog can jump from 1st stair to 2nd stair (|20-10| = 10 energy lost).
Then a jump from the 2nd stair to the last stair (|10-20| = 10 energy lost).
So, the total energy lost is 20 which is the minimum. 
Hence, the answer is 20.  '''
#------------------------------------------------------------------------------------------------------------
#recursive approach
'''
TC -> O(2**N)
SC -> O(N)
'''
def jumps(ind,heights):
    if ind<=0:
        return 0
    left=jumps(ind-1,heights)+abs(heights[ind]-heights[ind-1])
    right=10**9
    if ind>1:
        right=jumps(ind-2,heights)+abs(heights[ind]-heights[ind-2])
    return min(left,right)
n=int(input())
heights=[int(x) for x in input().split()]
print(jumps(n-1,heights))
#---------------------------------------------------------------------------------------------------------------
#Memoization approach
'''
TC -> O(N)
Sc -> O(N)+O(N)
'''
def jumps(ind,heights,d):
    if ind==0:
        return 0
    if ind in d:
        return d[ind]
    left=jumps(ind-1,heights,d)+abs(heights[ind]-heights[ind-1])
    right=10**9
    if ind>1:
        right=jumps(ind-2,heights,d)+abs(heights[ind]-heights[ind-2])
    d[ind]=min(left,right)
    return d[ind]
d={}
n=int(input())
heights=[int(x) for x in input().split()]
print(jumps(n-1,heights,d))
#----------------------------------------------------------------------------------------------------------------------
#Dynamic programming approach
'''
TC -> O(N)
Sc -> O(N)
'''
def jumps(n,heights,dp):
    dp[0]=0
    for i in range(1,n):
        left=dp[i-1]+abs(heights[i]-heights[i-1])
        right=10**9
        if i>1:
            right=dp[i-2]+abs(heights[i]-heights[i-2])
        dp[i]=min(left,right)
    return dp[n-1]
n=int(input())
heights=[int(x) for x in input().split()]
print(jumps(n,heights,{}))
#------------------------------------------------------------------------------------------------------------------------
#space optimization approach
'''
TC -> O(N)
Sc -> O(1)
'''
def jumps(n,heights):
    prev2,prev1=0,0
    for i in range(1,n):
        left=prev1+abs(heights[i]-heights[i-1])
        right=10**9
        if i>1:
            right=prev2+abs(heights[i]-heights[i-2])
        cur=min(left,right)
        prev2=prev1
        prev1=cur
    return cur
n=int(input())
heights=[int(x) for x in input().split()]
print(jumps(n,heights))

