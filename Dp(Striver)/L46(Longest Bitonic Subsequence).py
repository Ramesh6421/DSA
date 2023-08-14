# problem: link(https://www.codingninjas.com/codestudio/problems/longest-bitonic-sequence_1062688?source=youtube&campaign=striver_dp_videos&utm_source=youtube&utm_medium=affiliate&utm_campaign=striver_dp_videos&leftPanelTab=0)
'''
You are given an array/list 'ARR' consisting of 'N' positive integers.
A subsequence of 'ARR' is called bitonic if it is first increasing and then decreasing.

For Example:
An example of a bitonic sequence will be 1 < 2 < 3 < 4 > 2 > 1.
Your task is to return the length of the longest bitonic sequence of 'ARR'.
A subsequence of an array is an ordered subset of the array's elements having the same sequential ordering as the original array.

For Example:
Let ARR = [1, 2, 1, 2, 1]

One of the bitonic subsequences for this array will be [1, 2, 2, 1].

'''
# Tabulation
'''
Tc-> O(N*N)*2+O(N)
SC-> O(N)+O(N)
'''
def LIS(n,arr):
    dp1=[1]*n
    dp2=[1]*n
    # Longest Increasing subsequence
    for i in range(1,n):
        for j in range(i):
            if arr[j]<arr[i]:
                if 1+dp1[j]>dp1[i]:
                    dp1[i]=1+dp1[j]

    # Longest decreasing subsequence                
    for i in range(n-1,-1,-1):
        for j in range(n-1,i,-1):
            if arr[j]<arr[i]:
                if 1+dp2[j]>dp2[i]:
                    dp2[i]=1+dp2[j]
    maxi=0
    print(dp1)
    print(dp2)
    for i in range(n):
        cur=(dp1[i]+dp2[i])-1
        maxi=max(maxi,cur)
    return maxi

n=8
arr=[1,11,2,10,4,5,2,1]            # output: [1,2,10,5,2,1] ,len=6
print(LIS(n,arr))
