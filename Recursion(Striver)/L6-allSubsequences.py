'''
printing all the subsequences in an array
Input  = [3,1,2]
output = 3 1 2
         3 1
         3 2
         3
         1 2
         1
         2
'''


def recursion(Index,N,List):
    if Index>=N:
        print(*List)
        return
    List.append(Arr[Index])
    recursion(Index+1,N,List)
    List.pop()
    recursion(Index+1,N,List)
    
Arr=[int(x) for x in input().split()]
recursion(0,len(Arr),[])
