'''
Reversing an array using two pointers (Modifying the Array itself)
Approach:
swapping the elements

Input  = [1,2,3,4,5]
output = [5,4,3,2,1]
'''
def recursion(Left,Right,Array):
    if Left<Right:
        Array[Left],Array[Right]=Array[Right],Array[Left]
        recursion(Left+1,Right-1,Array)
    return
Array=[int(x) for x in input().split()]
recursion(0,len(Array)-1,Array)
print(Array)


'''
Reversing an array using One pointer (Modifying the array itself)
'''

def recursion(Left,n,Array):
    if Left<n//2:
        Array[Left],Array[n-Left-1]=Array[n-Left-1],Array[Left]
        recursion(Left+1,n,Array)
    return
Array=[int(x) for x in input().split()]
recursion(0,len(Array),Array)
print(Array)

