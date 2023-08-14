'''
APPROACH - 2

printing all permutations of a given string or array.
Arr = [1,2,3]
output = [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,2,1],[3,1,2]]
'''

def recursion(Index,N,Arr):
    if Index==N:
        #print(Arr)
        #List=Arr.copy()
        Answer.append(Arr.copy())
        return
    for i in range(Index,N):
        Arr[Index],Arr[i] = Arr[i],Arr[Index]
        recursion(Index+1,N,Arr)
        Arr[Index],Arr[i] = Arr[i],Arr[Index]
            
Arr=[int(x) for x in input().split()]
Answer=[]
recursion(0,len(Arr),Arr)
print(Answer)
