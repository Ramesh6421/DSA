'''
printing subsequences with sum k
arr    = [1,2,1]
output = 2
   i,e,  [1,1]
         [2]
'''

def recursion(Index,N,Sum):
    if Index>=N:
        if Sum==K:
            return 1
        return 0
    Sum=Sum+Arr[Index]
    Take=recursion(Index+1,N,Sum)
    Sum=Sum-Arr[Index]
    NotTake=recursion(Index+1,N,Sum)
    return Take+NotTake
    
Arr=[int(x) for x in input().split()]
K=int(input())
print(recursion(0,len(Arr),0))
