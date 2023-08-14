# problem link(https://practice.geeksforgeeks.org/problems/alien-dictionary/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=alien-dictionary)
'''
Given a sorted dictionary of an alien language having N words and k starting alphabets of standard dictionary.
Find the order of characters in the alien language.
Note: Many orders may be possible for a particular test case,
thus you may return any valid order and output will be 1 if the order of string returned by the function is correct
else 0 denoting incorrect string returned.

Example 1:

Input: 
N = 5, K = 4
dict = {"baa","abcd","abca","cab","cad"}
Output:
1
Explanation:
Here order of characters is 
'b', 'd', 'a', 'c' Note that words are sorted 
and in the given language "baa" comes before 
"abcd", therefore 'b' is before 'a' in output.
Similarly we can find other orders.
Example 2:

Input: 
N = 3, K = 3
dict = {"caa","aaa","aab"}
Output:
1
Explanation:
Here order of characters is
'c', 'a', 'b' Note that words are sorted
and in the given language "caa" comes before
"aaa", therefore 'c' is before 'a' in output.
Similarly we can find other orders.

'''

# Complexity
'''
TC-> O(K+E) + O(N*len(maxString) + K)
SC-> O(K) + O(K)
'''

def toposort(V,adj):
    indegree=[0]*V
    for i in range(V):
        for j in adj[i]:
            indegree[j]+=1
    q=[]
    for i in range(V):
        if indegree[i]==0:
            q.append(i)
    topo=[]
    while q:
        node=q.pop(0)
        topo.append(node)
        for i in adj[node]:
            indegree[i]-=1
            if indegree[i]==0:
                q.append(i)
            
    return topo

def alien_Dict(dict,N,K):
    adj={i:[] for i in range(K)}
    for i in range(N-1):
        s1=dict[i]
        s2=dict[i+1]
        Len=min(len(s1),len(s2))
        for j in range(Len):
            if s1[j]!=s2[j]:
                x=ord(s1[j])-97 
                y=ord(s2[j])-97 
                adj[x].append(y)
                break
    alien=toposort(K,adj)            
    order=''
    for i in alien:
        order+=chr(i+97)
    return order    

N=5
K=4
dict=["baa","abcd","abca","cab","cad"]
print(alien_Dict(dict,N,K))

N=5
K=5
dict=["baa","abcd","abca","cab","cad"]
print(alien_Dict(dict,N,K))
