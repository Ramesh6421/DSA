'''
printing all permutations of given array/string
Arr = [1,2,3]
output = [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
'''
def recursion(List,Dict):
    #print(List)
    if len(List)==len(Arr):
        Answer.append(List)
    for i in range(len(Arr)):
        if i not in Dict:
            Dict[i]=1
            recursion(List+[Arr[i]],Dict)
            Dict.pop(i)

Arr=[int(x) for x in input().split()]
Answer=[]
recursion([],{})
print(Answer)
    
