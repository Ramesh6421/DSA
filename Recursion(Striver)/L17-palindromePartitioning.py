'''
Palindrome partitioning problem in leetcode.

Given a string s, partition s such that every substring of the partition is a palindrome.
Return all possible palindrome partitioning of s.
A palindrome string is a string that reads the same backward as forward.

Input = 'aabb'
Output = [['a', 'a', 'b', 'b'], ['a', 'a', 'bb'], ['aa', 'b', 'b'], ['aa', 'bb']]

'''
def isPalindrome(s):
    if s==s[::-1]:
        return True
    return False
    
def partition(index,s,path):
    if index==len(s):
        res.append(path.copy())
        return
    for i in range(index,len(s)):
        if isPalindrome(s[index:i+1]):          # checking substring is palindrome or not
            path.append(s[index:i+1])
            partition(i+1,s,path)               # checking from next index to n  
            path.pop()                          # Backtracking 

s=input()
res=[]
partition(0,s,[])
print(res)
