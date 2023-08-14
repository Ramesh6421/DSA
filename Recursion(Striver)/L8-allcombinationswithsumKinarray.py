'''
printing all combinations with sum k of given an array.
arr    = [2,3,6,7]
output = [2,2,3]
         [7]
'''

def recursion(Index,N,List,target):
    if Index==N:
        if target==0:
            #print(List)
            Answer.append(List)
        return
    if Arr[Index]<=target:
        #List.append(Arr[Index])
        recursion(Index,N,List+[Arr[Index]],target-Arr[Index])
        #List.pop()
    recursion(Index+1,N,List,target)

Arr=[int(x) for x in input().split()]
K=int(input())
Answer=[]   
recursion(0,len(Arr),[],K)

print(Answer)
