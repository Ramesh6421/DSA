def dfs(word,seq,dic):
    if word==beginWord:
        cur=seq.copy()
        cur.reverse()
        ans.append(cur) 
    steps=dic[word]
    word=list(word)
    for i in range(len(word)):
        original=word[i]
        for j in range(97,123):
            word[i]=chr(j) 
            dup=''.join(word) 
            if dup in dic and dic[dup]+1==steps:
                seq.append(dup) 
                dfs(dup,seq,dic)
                seq.pop()
        word[i]=original 

def wordLadder_Shortest_Sequences(beginWord, endWord, wordList):
    q=[]
    q.append(beginWord)
    st=set(wordList)
    if beginWord in st:
        st.remove(beginWord)

    dic={}
    dic[beginWord]=0
        
    while q:
        word=q.pop(0)
        steps=dic[word]
        word=list(word)
        for i in range(len(word)):
            original=word[i]
            for j in range(97,123):
                word[i]=chr(j)
                dup=''.join(word)
                if dup in st:
                    q.append(dup)
                    dic[dup]=steps+1
                    st.remove(dup)
            word[i]=original
    if endWord in dic:
        seq=[endWord]
        dfs(endWord,seq,dic)

wordList=["des","der","dfr","dgt","dfs"]
beginWord="der"
endWord="dfs"
ans=[]
wordLadder_Shortest_Sequences(beginWord, endWord, wordList)
print(ans)	    
          

    
            
            
