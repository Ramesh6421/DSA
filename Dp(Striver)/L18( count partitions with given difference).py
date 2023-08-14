# count partitions with given difference
# notes: link(https://takeuforward.org/data-structure/count-partitions-with-given-difference-dp-18/)
# problem: link(https://www.codingninjas.com/codestudio/problems/partitions-with-given-difference_3751628?source=youtube&campaign=striver_dp_videos&utm_source=youtube&utm_medium=affiliate&utm_campaign=striver_dp_videos&leftPanelTab=0)
'''
Given an array ‘ARR’, partition it into two subsets (possibly empty) such that their union is the original array.
Let the sum of the elements of these two subsets be ‘S1’ and ‘S2’.
Given a difference ‘D’, count the number of partitions in which ‘S1’ is greater than or equal to ‘S2’ and
the difference between ‘S1’ and ‘S2’ is equal to ‘D’. Since the answer may be too large, return it modulo ‘10^9 + 7’.

If ‘Pi_Sj’ denotes the Subset ‘j’ for Partition ‘i’. Then, two partitions P1 and P2 are considered different if:
1) P1_S1 != P2_S1 i.e, at least one of the elements of P1_S1 is different from P2_S2.
2) P1_S1 == P2_S2, but the indices set represented by P1_S1 is not equal to the indices set of P2_S2. Here, the indices set of P1_S1 is formed by taking the indices of the elements from which the subset is formed.
Refer to the example below for clarification.
Note that the sum of the elements of an empty subset is 0.

For Example :
If N = 4, D = 3, ARR = {5, 2, 5, 1}
There are only two possible partitions of this array.
Partition 1: {5, 2, 1}, {5}. The subset difference between subset sum is: (5 + 2 + 1) - (5) = 3
Partition 2: {5, 2, 1}, {5}. The subset difference between subset sum is: (5 + 2 + 1) - (5) = 3
These two partitions are different because, in the 1st partition, S1 contains 5 from index 0, and in the 2nd partition, S1 contains 5 from index 2.

Approach:

given that , d=s1-s2 ------> eq1
totsum=s1+s2 
s1=totsum-s2 ------> eq2
so,
substitute eq2 in eq1
i.e,
d=totsum-s2-s2
d=totsum-2s2
2s2=totsum-d
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
arr=[5,2,4,6]
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
arr=[5,2,4,6]
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
arr=[5,2,4,6]
totsum=sum(arr)
if totsum-d<0 or (totsum-d)%2==1:
    print(0)
else:    
    k=(totsum-d)//2
    prev=[0 for j in range(k+1)]
    print(countset(n,arr,k,prev))

