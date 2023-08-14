'''
printing all unique possible subsets in given array
Arr = [1,2,2]
output = [[],[1],[1,2],[1,2,2],[2],[2,2]]
'''
def recursion(Index,N,List):
    Answer.append(List)
    for i in range(Index,N):
        if i!=Index and Arr[i]==Arr[i-1]:
            continue
        recursion(i+1,N,List+[Arr[i]])
    
Arr=[int(x) for x in input().split()]
Answer=[]
recursion(0,len(Arr),[])
print(Answer)
