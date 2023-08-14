# count of subsets with target k
# notes: link(https://takeuforward.org/data-structure/count-subsets-with-sum-k-dp-17/)
# priblem: link(https://www.codingninjas.com/codestudio/problems/number-of-subsets_3952532?source=youtube&campaign=striver_dp_videos&utm_source=youtube&utm_medium=affiliate&utm_campaign=striver_dp_videos)
'''
You are given an array (0-based indexing) of positive integers and
you have to tell how many different ways of selecting the elements from the array are there
such that the sum of chosen elements is equal to the target number “tar”.

Input:           Output:
n=4 , k=3          3
arr=[1,2,2,3]

'''
#Recursion
'''
TC-> O(2**N)
SC-> O(N)
'''

#Recursion + Memoization
'''
TC-> O(N*K)
SC-> O(N) + O(N*K)
'''
def countset(ind,arr,k,dp):
    if k==0:
        return 1
    if ind==0:
        if arr[ind]==k:
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
n,k=4,3
arr=[1,2,2,3]
dp=[[-1 for j in range(k+1)]for i in range(n+1)]
print(countset(n-1,arr,k,dp))
n,k=2,3
arr=[1,2]
dp=[[-1 for j in range(k+1)]for i in range(n+1)]
print(countset(n-1,arr,k,dp))


#Tabulation
'''
TC-> O(N*K)
SC-> O(N*K)
'''
def countset(n,arr,k,dp):
    for i in range(n):
        dp[i][0]=1  
    if arr[0]<=k:
        dp[0][arr[0]]=1
    for ind in range(1,n):
        for tar in range(1,k+1):
            nonTake=dp[ind-1][tar]
            take=0
            if arr[ind]<=tar:
                take=dp[ind-1][tar-arr[ind]]
            dp[ind][tar]=take+nonTake       
    return dp[n-1][k]        
        
n,k=4,3
arr=[1,2,2,3]
dp=[[0 for j in range(k+1)]for i in range(n)]
print(countset(n,arr,k,dp))
n,k=2,3
arr=[1,2]
dp=[[0 for j in range(k+1)]for i in range(n)]
print(countset(n,arr,k,dp))
    


#Space Optimization
'''
TC-> O(N*K)
SC-> O(K)
'''
def countset(n,arr,k,prev):
    prev[0]=1  
    if arr[0]<=k:
        prev[arr[0]]=1
    for ind in range(1,n):
        cur=[0 for j in range(k+1)]
        cur[0]=1
        for tar in range(1,k+1):
            nonTake=prev[tar]
            take=0
            if arr[ind]<=tar:
                take=prev[tar-arr[ind]]
            cur[tar]=take+nonTake
        prev=cur    
    return prev[k]        
        
n,k=4,3
arr=[1,2,2,3]
prev=[0 for j in range(k+1)]
print(countset(n,arr,k,prev))
n,k=2,3
arr=[1,2]
prev=[0 for j in range(k+1)]
print(countset(n,arr,k,prev))
    

# if arr[i]>=0
'''
above code is work only if arr[i]>=1
for example,
if n=3,k=1
arr=[0,0,1]
it will give 1 as output.
but it's wrong, the actual output is 4.
i.e,[0,1],[0,1],[0,0,1],[1]

'''
def countset(ind,arr,k,dp):
    if ind==0:
        if k==0 and arr[0]==0:
            return 2
        if k==0 or arr[0]==k:
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

n,k=3,1
arr=[0,0,1]
dp=[[-1 for j in range(k+1)]for i in range(n+1)]
print(countset(n-1,arr,k,dp))
