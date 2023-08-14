# Largest divisible subset
# problem: link(https://www.codingninjas.com/codestudio/problems/divisible-set_3754960?source=youtube&campaign=striver_dp_videos&utm_source=youtube&utm_medium=affiliate&utm_campaign=striver_dp_videos&leftPanelTab=0)
'''
You are given an array of distinct numbers ‘arr’.
Your task is to return the largest subset of numbers from ‘arr’,
such that any pair of numbers ‘a’ and ‘b’ from the subset satisfies
the following: a % b == 0 or b % a == 0.

'''
# Tabulation
'''
TC-> O(N*N)+O(N)
SC-> O(N)+O(N)
'''
def LIS(n,arr):
    dp=[1]*n
    dic={}
    for i in range(n):
        dic[i]=i
        for j in range(i):
            if arr[i]%arr[j]==0:
                if 1+dp[j]>dp[i]:
                    dp[i]=1+dp[j]
                    dic[i]=j
   
    maxi=max(dp)
    lastIndex=dp.index(maxi)
    li=[-1]*maxi
    li[0]=arr[lastIndex]
    ind=1
    while dic[lastIndex]!=lastIndex:
        lastIndex=dic[lastIndex]
        li[ind]=arr[lastIndex]
        ind+=1

    li.reverse()
    print(*li)        # sequence
    return max(dp)    # length

#n = 8
#arr = [10,9,2,5,3,7,101,18]
n=6
arr=[5,4,11,1,16,8]
arr.sort()
print(LIS(n,arr))    
