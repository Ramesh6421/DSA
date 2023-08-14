'''
printing subsequences with sum k
arr    = [1,2,1]
output = [1,1]
         [2]
'''
def recursion(Index,N,List,Sum):
    if Index>=N:
        if Sum==K:
            print(List)
        return
    List.append(Arr[Index])
    Sum=Sum+Arr[Index]
    recursion(Index+1,N,List,Sum)
    List.pop()
    Sum=Sum-Arr[Index]
    recursion(Index+1,N,List,Sum)
    
Arr=[int(x) for x in input().split()]
K=int(input())
recursion(0,len(Arr),[],0)
