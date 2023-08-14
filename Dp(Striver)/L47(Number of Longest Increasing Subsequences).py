# number of Longest Increasing Subsequences
# problem link(https://www.codingninjas.com/codestudio/problems/number-of-longest-increasing-subsequence_3751627?source=youtube&campaign=striver_dp_videos&utm_source=youtube&utm_medium=affiliate&utm_campaign=striver_dp_videos&leftPanelTab=0)
'''
Given an integer array ‘ARR’ of length ‘N’, return the number of longest increasing subsequences in it.
The longest increasing subsequence(LIS) is the longest subsequence of the given sequence
such that all elements of the subsequence are in increasing order.

Note :
The subsequence should be a strictly increasing sequence.

For Example :
Let ‘ARR’ = [50, 3, 90, 60, 80].
In this array the longest increasing subsequences are [50, 60, 80] and [3, 60, 80].
There are other increasing subsequences as well but we need the number of longest ones. Hence the answer is 2.

'''
#Tabulation
'''
TC-> O(N*N)+O(N)
SC-> O(N)+O(N)
'''
def LIS(n,arr):
    dp=[1]*n
    cnt=[1]*n
    for i in range(1,n):
        for j in range(i):
            if arr[j]<arr[i]:
                if 1+dp[j]>dp[i]:
                    dp[i]=1+dp[j]
                    cnt[i]=cnt[j]
                elif 1+dp[j]==dp[i]:
                    cnt[i]+=cnt[j]
    ans=0
    maxi=max(dp)
    print(dp)
    print(cnt)
    for i in range(n):
        if dp[i]==maxi:
            ans+=cnt[i]
    return ans

n=10
arr=[1,5,4,3,2,6,7,10,8,9]
print(LIS(n,arr))
        
                    
