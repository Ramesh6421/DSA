# priblem :link(https://www.codingninjas.com/codestudio/problems/count-distinct-substrings_985292?utm_source=youtube&utm_medium=affiliate&utm_campaign=striver_tries_videos&leftPanelTab=0)
# notes link (https://takeuforward.org/data-structure/number-of-distinct-substrings-in-a-string-using-trie/)
'''
Problem Statement:
Given a string of alphabetic characters.
Return the count of distinct substrings of the string(including the empty string) using the Trie data structure.

Example 1:

Input:
 S1= “ababa”

Output: Total number of distinct substrings : 10

Explanation:

All the substrings of the string are a, ab, aba, abab, ababa, b, ba, bab, baba, a, ab, aba, b, ba, a.
Many of the substrings are duplicated.
The distinct substrings are a, ab, aba, abab, ababa, b, ba, bab, baba.
Total Count of the distinct substrings is 9 + 1(for empty string) = 10.

'''

# Complexity
'''
TC-> O(N*N)
SC-> we can't define,It is based on input.
'''

class Trie:
    def __init__(self):
        self.child={}
 
def countDistinctSubstrings(s):
    ob1=Trie()
    count=0
    n=len(s)
    for i in range(len(s)):
        cur=ob1.child
        for j in range(i,n):
            if s[j] not in cur:
                cur[s[j]]={}
                count+=1
            cur=cur[s[j]]          
    return count+1   
s='abab'
ans=countDistinctSubstrings(s)
print(ans)
