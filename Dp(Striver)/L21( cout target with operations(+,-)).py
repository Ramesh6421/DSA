# count target sum with operations using +,-
# notes: (https://takeuforward.org/data-structure/target-sum-dp-21/)
# problem: link(https://www.codingninjas.com/codestudio/problems/target-sum_4127362?source=youtube&campaign=striver_dp_videos&utm_source=youtube&utm_medium=affiliate&utm_campaign=striver_dp_videos&leftPanelTab=0)
'''
You are given an array ‘ARR’ of ‘N’ integers and a target number, ‘TARGET’.
Your task is to build an expression out of an array by adding one of the symbols '+' and '-' before each integer in an array,
and then by concatenating all the integers, you want to achieve a target.
You have to return the number of ways the target can be achieved.

For Example :
You are given the array ‘ARR’ = [1, 1, 1, 1, 1], ‘TARGET’ = 3.
The number of ways this target can be achieved is:
1. -1 + 1 + 1 + 1 + 1 = 3
2. +1 - 1 + 1 + 1 + 1 = 3 
3. +1 + 1 - 1 + 1 + 1 = 3                                       -------( exactly SIMILAR TO L18 )------
4. +1 + 1 + 1 - 1 + 1 = 3
5. +1 + 1 + 1 + 1 - 1 = 3
These are the 5 ways to make. Hence the answer is 5.

Approach:

let, 1+1-1+1-1 ==> 1+1+1-1-1  ==> (1+1+1)-(1+1) ==> s1-s2
i,e,
tar=s1-s2 ------> eq1
totsum=s1+s2 
s1=totsum-s2 ------> eq2
so,
substitute eq2 in eq1
i.e,
tar=totsum-s2-s2
tar=totsum-2s2
2s2=totsum-tar
s2=(totsum-d)//2 ---------> this is the target we searching in the array.


'''
#Recursion+Memoization
'''
TC-> O(N*K)
SC-> O(N*K)+O(N)
'''
def countset(ind,arr,k,dp):
    if ind==0:
        if k==0 and arr[ind]==0:
            return 2
        if k==0 or arr[ind]==k:
            return 1
        return 0
    if dp[ind][k]!=-1:
        return dp[ind][k]
    nonTake=countset(ind-1,arr,k,dp)
    take=0
    if arr[ind]<=k:
        take=countset(ind-1,arr,k-arr[ind],dp)
    dp[ind][k]=take+nonTake
    return take+nonTake
n,d=4,3
arr=[1,2,3,1]
totsum=sum(arr)
if totsum-d<0 or (totsum-d)%2==1:
    print(0)
else:    
    k=(totsum-d)//2
    dp=[[-1 for j in range(k+1)]for i in range(n)]
    print(countset(n-1,arr,k,dp))

#Tabulation
'''
TC-> O(N*K)
SC-> O(N*K)
'''
def countset(n,arr,k,dp):
    if arr[0]==0:
        dp[0][0]=2
    else:
        dp[0][0]=1
    if arr[0]<=k and arr[0]!=0:
        dp[0][arr[0]]=1
    for ind in range(1,n):
        for tar in range(k+1):
            nonTake=dp[ind-1][tar]
            take=0
            if arr[ind]<=tar:
                take=dp[ind-1][tar-arr[ind]]
            dp[ind][tar]=take+nonTake       
    return dp[n-1][k]        
n,d=4,3
arr=[1,2,3,1]
totsum=sum(arr)
if totsum-d<0 or (totsum-d)%2==1:
    print(0)
else:    
    k=(totsum-d)//2
    dp=[[0 for j in range(k+1)]for i in range(n)]
    print(countset(n,arr,k,dp))

#Space Optimization
'''
TC-> O(N*K)
SC-> O(K)
'''

def countset(n,arr,k,prev):
    if arr[0]==0:
        prev[0]=2
    else:
        prev[0]=1
    if arr[0]<=k and arr[0]!=0:
        prev[arr[0]]=1
    for ind in range(1,n):
        cur=[0 for j in range(k+1)]
        for tar in range(k+1):
            nonTake=prev[tar]
            take=0
            if arr[ind]<=tar:
                take=prev[tar-arr[ind]]
            cur[tar]=take+nonTake
        prev=cur    
    return prev[k]        
n,d=4,3
arr=[1,2,3,1]
totsum=sum(arr)
if totsum-d<0 or (totsum-d)%2==1:
    print(0)
else:    
    k=(totsum-d)//2
    prev=[0 for j in range(k+1)]
    print(countset(n,arr,k,prev))

