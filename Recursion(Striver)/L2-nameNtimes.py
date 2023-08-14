'''
printing name N times
'''
def recursion(i,n):
    if i>n:
        return
    print("STRIVER")
    recursion(i+1,n)
n=int(input())
recursion(1,n)
