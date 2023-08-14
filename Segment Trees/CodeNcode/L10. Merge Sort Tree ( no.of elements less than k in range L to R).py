# problem
'''
Given an array of size N and Q queries of form L,R,K.
Find number of elements in the Range L to R which are strictly smaller than k.
'''

#Complexity
'''
TC->O(NlogN)+O(QlogN)
SC->O(NlogN)
'''
from bisect import bisect_left
def Build(SegInd,SegStart,SegEnd):

    if SegStart == SegEnd:
        SegTree[SegInd].append(a[SegStart-1])
        return
    
    mid=(SegStart+SegEnd)//2
    Build(2*SegInd,SegStart,mid)
    Build(2*SegInd+1,mid+1,SegEnd)

    i=0
    j=0

    while i<len(SegTree[2*SegInd]) and j<len(SegTree[2*SegInd+1]):

        if SegTree[2*SegInd][i]<=SegTree[2*SegInd+1][j]:
            SegTree[SegInd].append(SegTree[2*SegInd][i])
            i+=1

        else:
            SegTree[SegInd].append(SegTree[2*SegInd+1][j])
            j+=1

    while i<len(SegTree[2*SegInd]):
        SegTree[SegInd].append(SegTree[2*SegInd][i])
        i+=1

    while j<len(SegTree[2*SegInd+1]):
        SegTree[SegInd].append(SegTree[2*SegInd+1][j])
        j+=1

def Query(SegInd,SegStart,SegEnd,L,R,k):

    if SegStart>R or SegEnd<L:
        return 0

    if SegStart>=L and SegEnd<=R:
        res=bisect_left(SegTree[SegInd],k)
        return res

    mid=(SegStart+SegEnd)//2
    left=Query(2*SegInd,SegStart,mid,L,R,k)
    right=Query(2*SegInd+1,mid+1,SegEnd,L,R,k)

    return left+right

n=8
a=[1,4,3,5,6,4,3,2]
SegTree=[[] for i in range(4*n+1)]
Build(1,1,n)
#print(SegTree)
q=3
queries=[[4,8,4],[1,5,4],[2,6,5]]
for L,R,K in queries:
    ans=Query(1,1,n,L,R,K)
    print(ans)

        
