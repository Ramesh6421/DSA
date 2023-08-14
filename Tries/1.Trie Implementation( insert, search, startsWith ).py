# Implement Trie – 1
# problem (https://www.codingninjas.com/codestudio/problems/implement-trie_631356?leftPanelTab=0
# notes (https://takeuforward.org/data-structure/implement-trie-1/)
'''
Problem Statement:
Implementing insertion, search, and startWith operations in a trie or prefix-tree.

Implementation: 

Type 1: To insert a string “word” in Trie.                           

Type 2: To check if the string “word” is present in Trie or not.

Type 3: To check if there is any string in the Trie that starts with the given prefix string “word”.        

Example:
Input: type = {1, 1, 2, 3, 2};
value = {"hello", "help", "help", "hel", "hel"};

Output: 
true
true
false

Explanation: 
Trie object initialized
“hello” inserted in the trie.
“help” insertedin the trie 
“help” searched in the trie //returns true
Checked if any previously inserted word has the prefix “hel” //return true
“hel” searches in the trie //returns true
'''
# Complexity
'''
TC-> O(len(longest string))
SC-> O(1)
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
        
    def search(self,word):
        cur=self.child
        for i in word:
            if i not in cur:
                return False
            cur=cur[i]
        if '#' in cur:
            return True
        return False

    def startsWith(self,word):
        cur=self.child
        for i in word:
            if i not in cur:
                return False
            cur=cur[i]
        return True

ob1 = Trie()
ob1.insert("apple")
print(ob1.search("apple"))
print(ob1.search("app"))
print(ob1.startsWith("app"))
ob1.insert("app")
print(ob1.search("app"))    
