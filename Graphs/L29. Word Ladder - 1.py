# problem link(https://practice.geeksforgeeks.org/problems/word-ladder/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=word-ladder)
'''
Given two distinct words startWord and targetWord, and a list denoting wordList of unique words of equal lengths.
Find the length of the shortest transformation sequence from startWord to targetWord.
Keep the following conditions in mind:

A word can only consist of lowercase characters.
Only one letter can be changed in each transformation.
Each transformed word must exist in the wordList including the targetWord.
startWord may or may not be part of the wordList.

Example 1:

Input:
wordList = {"des","der","dfr","dgt","dfs"}
startWord = "der", targetWord= "dfs",
Output:
3
Explanation:
The length of the smallest transformation
sequence from "der" to "dfs" is 3
i,e "der" -> "dfr" -> "dfs".
Example 2:

Input:
wordList = {"geek", "gefk"}
startWord = "gedk", targetWord= "geek", 
Output:
2
Explanation:
gedk -> geek
Example 3:

Input: 
wordList = {"poon", "plee", "same", "poie","plea","plie","poin"}
startWord = "toon", targetWord= "plea",
Output: 7 
Explanation:
toon -> poon -> poin -> poie -> plie -> plee -> plea 

'''

# Complexity
'''
TC-> O( N * wordLength * 26 ) * log(N)
SC-> O(N)+O(N)
'''
def wordLadderLength(startWord, targetWord, wordList):
    q=[]
    q=[(startWord,1)]
    st=set(wordList)
    if startWord in st:
        st.remove(startWord)
    while q:
        word,steps=q.pop(0)
        if word==targetWord:
            return steps
        word=list(word)    
        for i in range(len(word)):
            original=word[i]
            for j in range(97,123):
                word[i]=chr(j)
                cur=''.join(word)
                if cur in st:
                    st.remove(cur)
                    q.append((cur,steps+1))
            word[i]=original
    return 0	            


wordList=["des","der","dfr","dgt","dfs"]
startWord="der"
targetWord="dfs"
print(wordLadderLength(startWord, targetWord, wordList))
	    
