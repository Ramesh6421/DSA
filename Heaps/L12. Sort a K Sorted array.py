# problem link()
'''
Given an array of n elements, where each element is at most k away from its target position.
The task is to print array in sorted form.

Example:
n=6
k=3
nums=[2,6,3,12,56,8]

Output:
[2,3,6,8,12,56]

'''
from heapq import heapify,heappush,heappop 
def SortKsortedArray(n,k,a):
    heap=a[:k]
    heapify(heap)
    res=[0]*n
    i=k
    j=0
    while i<n:
        val=heappop(heap)
        res[j]=val 
        heappush(heap,a[i])
        i+=1 
        j+=1 
    while heap:
        val=heappop(heap) 
        res[j]=val 
        j+=1
    print(*res)
    
n=6
k=3
nums=[2,6,3,12,56,8]
SortKsortedArray(n,k,nums)
    
    
