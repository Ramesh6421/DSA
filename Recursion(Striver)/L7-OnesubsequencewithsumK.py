'''
printing subsequences with sum k
arr    = [1,2,1] ,k = 2
output = [1,1] or [2]
         
'''

def recursion(Index,N,List,Sum):
    if Index>=N:
        if Sum==K:
            print(*List)
            return True
        return False
    List.append(Arr[Index])
    Sum=Sum+Arr[Index]
    if recursion(Index+1,N,List,Sum)==True:
        return True
    List.pop()
    Sum=Sum-Arr[Index]
    if recursion(Index+1,N,List,Sum)==True:
        return True
    return False
    
Arr=[int(x) for x in input().split()]
K=int(input())
recursion(0,len(Arr),[],0)
