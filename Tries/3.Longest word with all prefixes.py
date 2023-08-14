# problem link(https://www.codingninjas.com/codestudio/problems/complete-string_2687860?utm_source=youtube&utm_medium=affiliate&utm_campaign=striver_tries_videos&leftPanelTab=0)
'''
Ninja developed a love for arrays and strings so this time his teacher gave him an array of strings, ‘A’ of size ‘N’.
Each element of this array is a string.
The teacher taught Ninja about prefixes in the past, so he wants to test his knowledge.
A string is called a complete string if every prefix of this string is also present in the array ‘A’.
Ninja is challenged to find the longest complete string in the array ‘A’.If there are multiple strings with the same length,
return the lexicographically smallest one and if no string exists, return "None".

Example:

N = 4
A = [ “ab” , “abc” , “a” , “bp” ] 

Explanation : 

Only prefix of the string “a” is “a” which is present in array ‘A’. So, it is one of the possible strings.
Prefixes of the string “ab” are “a” and “ab” both of which are present in array ‘A’. So, it is one of the possible strings.
Prefixes of the string “bp” are “b” and “bp”. “b” is not present in array ‘A’. So, it cannot be a valid string.
Prefixes of the string “abc” are “a”,“ab” and “abc” all of which are present in array ‘A’. So, it is one of the possible strings.
We need to find the maximum length string, so “abc” is the required string.

'''
# Complexity
'''
TC-> O(N)*O(len)+ O(N)+O(len)
'''
class Trie:
    def __init__(self):
        self.child={}

    def insert(self,word):
        cur=self.child
        for i in word:
            if i not in cur:
                cur[i]={}
            cur=cur[i]
        cur['#']=1
        
    def checkIfPrefixExists(self,word):
        cur=self.child
        for i in word:
            if i in cur:
                cur=cur[i]
                if '#' not in cur:
                    return False
            else:
                return False
        return True
    
def completeString(a):
    ob1=Trie()
    for i in a:
        ob1.insert(i)
    longest=''
    for i in a:
        check=ob1.checkIfPrefixExists(i)
        if check==True:
            if len(i)>len(longest):
                longest=i
            elif len(i)==len(longest):
                longest=min(i,longest)
    if len(longest)==0:
        return None
    return longest

a=["n","ni","nin","ninj","ninja","ninga"]
ans=completeString(a)
print(ans)
