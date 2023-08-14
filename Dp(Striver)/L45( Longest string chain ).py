# problem: link(https://www.codingninjas.com/codestudio/problems/longest-string-chain_3752111?source=youtube&campaign=striver_dp_videos&utm_source=youtube&utm_medium=affiliate&utm_campaign=striver_dp_videos&leftPanelTab=0)
'''
You are given an array ‘ARR’ of strings, where each string consists of English lowercase letters.
Let’s say a string ‘A’ is a predecessor of string ‘B’ if and only if we can add exactly one letter anywhere in ‘A’ to make it equal to ‘B’.

For example “abd” is a predecessor of “abcd”, we can add “c” in “abd” to make a string “abcd”
A string chain is a sequence of strings where for every ‘i’ in [1 . . . (K - 1)], ‘Si’ is the predecessor of ‘Si+1’.
And the length of such a string chain is ‘K’.
Now your task is to find the length of the longest possible string chain.

For Example :
Let ‘ARR’ = ["x", “xx”, “y”, “xyx”] 
The longest possible string chain is “x” -> “xx” -> “xyx”
The length of the given chain is 3, hence the answer is 3.

'''

# Tabulation
'''
TC-> O(N*N)*len(LIS) + O(nlogn)
SC-> O(N)
'''
def compare(s,t):             # comapring two strings are differ by one charecter or not
    if len(s)!=len(t)+1:
        return False
    i,j=0,0
    while i<len(s):
        if j<len(t) and s[i]==t[j]:
            i+=1
            j+=1
        else:
            i+=1
    if i==len(s) and j==len(t):
        return True
    return False
    
def LIS(n,arr):
    dp=[1]*n
    for i in range(1,n):
        for j in range(i):
            if compare(arr[i],arr[j]):
                if 1+dp[j]>dp[i]:
                    dp[i]=1+dp[j]
    return max(dp)    
    

n=4
arr=['x','xx','y','xyx']
cur=sorted(arr,key=len)  # sorting based on the string length
print(LIS(n,cur))
    
