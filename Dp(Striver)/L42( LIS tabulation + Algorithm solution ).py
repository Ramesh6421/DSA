# Longest Increasing Subsequence
# Tabulation
'''
TC-> O(N*N)
SC-> O(N*N)
'''
# after 1-based indexing of memoization code
def LIS(arr,n,after):
    for ind in range(n-1,-1,-1):
        cur=[0 for j in range(n+1)]
        for prev_ind in range(ind-1,-2,-1):
            pick,nonpick = 0,0
            if prev_ind==-1 or arr[ind]>arr[prev_ind]:
                pick = 1 + after[ind+1]
            nonpick = 0 + after[prev_ind+1]
            cur[prev_ind+1] = max(pick,nonpick)
        after=cur    
            
    return after[0]

n = 8
arr = [10,9,2,5,3,7,101,18]
after=[0 for j in range(n+1)]
print(LIS(arr,n,after))    




# Algorithm
# printing length of LIS
'''
TC-> O(N*N)
SC-> O(N)
'''

def LIS(n,arr):
    dp=[1]*n
    for i in range(n):
        for j in range(i):
            if arr[j]<arr[i]:
                dp[i]=max(dp[i],dp[j]+1)
              
    return max(dp)

n = 8
arr = [10,9,2,5,3,7,101,18]
#n=5
#arr=[1,3,5,4,7]
print(LIS(n,arr))    



# printing sequence of LIS
'''
TC-> O(N*N) + O(K)    k is len(LIS)
SC-> O(N) + O(K)      k is len(LIS)
'''

def LIS(n,arr):
    dp=[1]*n
    dic={}
    for i in range(n):
        dic[i]=i
        for j in range(i):
            if arr[j]<arr[i]:
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
print(LIS(n,arr))    
