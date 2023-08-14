from heapq import heapify,heappush,heappop 
for i in range(int(input())):
    n,k=[int(x) for x in input().split()]
    a=[int(x) for x in input().split()]
    heap=a[:k]
    heapify(heap)
    res=[0]*n
    i=k
    j=0
    print(heap)
    while i<n:
        val=heappop(heap)
        res[j]=val 
        heappush(heap,a[i])
        print(heap)
        i+=1 
        j+=1 
    while heap:
        val=heappop(heap) 
        res[j]=val 
        j+=1
    print(*res)      
    
