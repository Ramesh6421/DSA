# House Robber (similar to lecture 5, here we taking the circular array, last and first elements are adjacent.)
# problem : link(https://www.codingninjas.com/codestudio/problems/house-robber_839733?source=youtube&campaign=striver_dp_videos&utm_source=youtube&utm_medium=affiliate&utm_campaign=striver_dp_videos&leftPanelTab=0)
'''
Mr. X is a professional robber planning to rob houses along a street.
Each house has a certain amount of money hidden.
All houses along this street are arranged in a circle.
That means the first house is the neighbor of the last one.
Meanwhile, adjacent houses have a security system connected,
and it will automatically contact the police if two adjacent houses were broken into on the same night.
You are given an array/list of non-negative integers 'ARR' representing the amount of money of each house.
Your task is to return the maximum amount of money Mr. X can rob tonight without alerting the police.

Input:              output:
3                     0
1                     3
0                     4
3
2 3 2
4
1 3 2 1                
'''

def maxx(n,arr):
    prev2,prev1=0,arr[0]
    for i in range(1,n):
        pick=arr[i]
        if i>1:
            pick+=prev2
        nonpick=prev1
        cur=max(pick,nonpick)
        prev2=prev1
        prev1=cur
    return prev1

for i in range(int(input())):
    n=int(input())
    arr=[int(x) for x in input().split()]
    if n==1:
        print(arr[0])
    else:
        first=maxx(n-1,arr[:n-1])
        last=maxx(n-1,arr[1:n])
        print(max(first,last))
