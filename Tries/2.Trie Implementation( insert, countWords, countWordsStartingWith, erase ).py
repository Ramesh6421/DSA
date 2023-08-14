# Implement Trie – II
# problem (https://www.codingninjas.com/codestudio/problems/implement-trie_1387095?leftPanelTab=0)
# notes (https://takeuforward.org/data-structure/implement-trie-ii/)
'''
Problem Statement:
Implement a data structure ”TRIE” from scratch. Complete some functions.

1) Trie(): Initialize the object of this “TRIE” data structure.

2) insert(“WORD”): Insert the string “WORD”  into this “TRIE” data structure.

3) countWordsEqualTo(“WORD”): Return how many times this “WORD” is present in this “TRIE”.

4) countWordsStartingWith(“PREFIX”): Return how many words are there in this “TRIE” that have the string “PREFIX” as a prefix.

5) erase(“WORD”): Delete this string “WORD” from the “TRIE”.

Note:

1. If erase(“WORD”) function is called then it is guaranteed that the “WORD” is present in the “TRIE”.

2. If you are going to use variables with dynamic memory allocation then you need to release the memory associated with them at the end of your solution.

Example:
Input: 
1
6
insert samsung
insert samsung
insert  vivo
erase vivo
countWordsEqualTo samsung
countWordsStartingWith vi

Output: 
2
0

Explanation: 

Insert “samsung”: we are going to insert the word “samsung” into the “TRIE”.
Insert “samsung”: we are going to insert the word “samsung” again into the “TRIE”.
Insert “vivo”: we are going to insert the word “vivo” into the “TRIE”.
Erase “vivo”: we are going to delete the word “vivo” from the “TRIE”.
countWordsEqualTo “samsung”: There are two instances of “samsung” is present in “TRIE”.
countWordsStartWith “vi”:There is not a single word in the “TRIE” that starts from the prefix “vi”.
'''

# Complexity
'''
TC-> O(len(longest string))
Sc-> O(1)
'''

class Trie:
    def __init__(self):
        self.child={'ew':0,'cp':0}

    def insert(self,word):
        cur=self.child
        for i in word:
            if i not in cur:
                cur[i]={'ew':0,'cp':0}
            cur=cur[i]
            cur['cp']+=1
        cur['ew']+=1    
        cur['#']=1

    def countWordsEqualTo(self,word):
        cur=self.child
        for i in word:
            if i not in cur:
                return 0
            cur=cur[i]
        return cur['ew']

    def countWordsStartingWith(self,word):
        cur=self.child
        for i in word:
            if i not in cur:
                return 0
            cur=cur[i]
        return cur['cp']

    def erase(self,word):
        cur=self.child
        for i in word:
            if i in cur:
                cur[i]['cp']-=1
                cur=cur[i]
            else:
                return
        cur['ew']-=1    
            
ob1=Trie()
ob1.insert("apple");
ob1.insert("apple");
ob1.insert("apps");
ob1.insert("apps");
word1 = "apps";
print("Count Words Equal to ",word1,ob1.countWordsEqualTo(word1))
word2 = "abc";
print("Count Words Equal to ",word2,ob1.countWordsEqualTo(word2))
word3 = "ap";
print("Count Words Starting With ",word3,ob1.countWordsStartingWith(word3))
word4 = "appl";
print("Count Words Starting With ",word4,ob1.countWordsStartingWith(word4))
ob1.erase(word1);
print("Count Words equal to ",word1,ob1.countWordsEqualTo(word1))
