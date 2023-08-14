'''
printing all unique combinations with sum k of given an array.
Each number should use only once in combination.
arr    = [1,1,1,2,2] target=4
output = [1,1,2]
         [2,2]
'''

def recursion(Index,N,List,target):
    if target==0:
        Answer.append(List)
        return
    for i in range(Index,N):
        if i>Index and Arr[i]==Arr[i-1]:
            continue
        if Arr[i]>target:
            break
        recursion(i+1,N,List+[Arr[i]],target-Arr[i])

Arr=[int(x) for x in input().split()]
K=int(input())
Arr.sort()
Answer=[]    
recursion(0,len(Arr),[],K)

print(Answer)
