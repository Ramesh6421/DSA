# Problem link(https://www.spoj.com/problems/RMQSQ/) 
'''
You are given a list of N numbers and Q queries. Each query is specified by two numbers i and j;
the answer to each query is the minimum number between the range [i, j] (inclusive).
Note: the query ranges are specified using 0-based indexing.

Note:
Update query is added, query is like
[ Type, index, value ] # if type is 1 then update otherwise minimum in Range

[ Type, L, R ] # if type is 2 then find minimum in Range L...R.

Input
The first line contains N, the number of integers in our list (N <= 100,000). The next line holds N numbers that are guaranteed to fit inside an integer. Following the list is a number Q (Q <= 10,000). The next Q lines each contain two numbers i and j which specify a query you must answer (0 <= i, j <= N-1).

Output
For each query, output the answer to that query on its own line in the order the queries were made.

Example
Input:
3
1 4 1
2
1 1
1 2
Output:
4
1

'''

# Complexity

'''
TC-> O(NlogN) + O(Q*logN)
SC-> O(4N)
'''

def Build( SegTree_ind, SegStart, SegEnd ):
    
    if SegStart == SegEnd:
        SegTree[ SegTree_ind ] = a[ SegStart-1]
        return
    
    mid = ( SegStart + SegEnd ) // 2
    
    Build( 2*SegTree_ind, SegStart, mid )
    Build( 2*SegTree_ind+1, mid+1, SegEnd )

    LeftVal = SegTree[ 2 * SegTree_ind ]
    RightVal = SegTree[ 2 * SegTree_ind+1 ]
    
    SegTree[ SegTree_ind ] = min( LeftVal, RightVal )


def Query( SegTree_ind, SegStart, SegEnd, L, R ):
    
    if SegStart > R or SegEnd < L:
        return float("inf")
    
    if SegStart >= L and SegEnd <= R:
        return SegTree[SegTree_ind]

    mid = ( SegStart + SegEnd ) // 2

    Left = Query ( 2 * SegTree_ind, SegStart, mid, L, R )
    Right = Query ( 2 * SegTree_ind+1, mid+1, SegEnd, L, R )
    return min( Left, Right )
    

def Update( SegTree_ind, SegStart, SegEnd, Query_ind ):

    if SegStart == SegEnd:
        SegTree[ SegTree_ind ] = a[ SegStart]
        return

    mid = ( SegStart + SegEnd ) // 2

    if Query_ind <= mid:
        Update( 2*SegTree_ind, SegStart, mid, Query_ind )
    else:
        Update( 2*SegTree_ind+1, SegStart, mid, Query_ind )

    LeftVal = SegTree[ 2*SegTree_ind ]
    RightVal = SegTree[ 2*SegTree_ind+1 ]
    
    SegTree[ SegTree_ind ] = min( LeftVal, RightVal )    


    
n = int( input () )
a = [ int(x) for x in input().split() ]
q = int( input () )

SegTree = [0]*(4*n+1)

Build( 1, 1, n )

print( SegTree )
for i in range( q ):
    Type, L, R = [ int(x) for x in input().split() ]
    if Type == 1:
        val = R
        a[ L ] = val
        Update( 1, 1, n, L+1 )

    else:    
        ans = Query(1,1,n,L+1,R+1)
        print(ans)
    

'''    
n = 6
a = [1, 5, 2, -3, 4, -1]
q = 3
queries = [ [2, 0, 2],      # 1 is minimum at index 0 to 2
            [1, 1, -2],     # a[ 1 ] = -2
            [2, 0, 2]       # -2 is minimum at index 0 to 2 
            ]
'''
