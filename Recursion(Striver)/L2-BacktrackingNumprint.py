'''
printing numbers from 1 to N using Backtracking
'''
def recursion(i,n):
    if i<1:
        return
    recursion(i-1,n)
    print(i)
n=int(input())
recursion(n,n)

'''
printing numbers from N to 1 using Backtracking
'''
def recursion(i,n):
    if i>n:
        return
    recursion(i+1,n)
    print(i)
n=int(input())
recursion(1,n)
