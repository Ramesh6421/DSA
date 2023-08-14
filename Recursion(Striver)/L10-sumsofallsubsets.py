'''
printing sums of all subsets
Arr = [3,1,2]
ouput = [0,1,2,3,3,4,5,6]
'''
def recursion(Index,N,Sum):
    if Index==N:
        Answer.append(Sum)
        return
    recursion(Index+1,N,Sum+Arr[Index])
    recursion(Index+1,N,Sum)

Arr=[int(x) for x in input().split()]
Answer=[]
recursion(0,len(Arr),0)
print(Answer)
