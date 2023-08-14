def wordLadder_Shortest_Sequences(startWord, targetWord, wordList):
    q=[]
    q.append([startWord])
    st=set(wordList)
    if startWord in st:
        st.remove(startWord)
    usedonlevel=[startWord]
    ans=[]
    level=0
    while q:
        cur=q.pop(0)
        if len(cur)>level:
            level+=1
            for it in usedonlevel:
                if it in st:
                    st.remove(it)
            usedonlevel=[]
            
        word=cur[-1]
        if word==targetWord:
            if len(ans)==0:
                ans.append(cur) 
            elif len(ans[0])==len(cur):
                ans.append(cur)
            
        word=list(word)
        for i in range(len(word)):
            original=word[i]
            for j in range(97,123):
                word[i]=chr(j)
                dup=''.join(word)
                if dup in st:
                    usedonlevel.append(dup)
                    cur.append(dup)
                   
                    x=cur.copy()
                    q.append(x)
                    cur.pop()
            word[i]=original
        
    return ans        

wordList=["des","der","dfr","dgt","dfs"]
startWord="der"
targetWord="dfs"
print(wordLadder_Shortest_Sequences(startWord, targetWord, wordList))
	    
          

