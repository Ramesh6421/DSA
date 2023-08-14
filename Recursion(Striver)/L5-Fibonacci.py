'''
printing the nth Fibonacci number
0 1 1 2 3 5 8 ......

Input = 0
Output= 0

Input = 3
Output= 2

'''
def recursion(n):
    if n==0:
        return 0
    if n==1:
        return 1
    First=recursion(n-1)
    Second=recursion(n-2)
    return First+Second
n=int(input())
print(recursion(n))


'''
//similar Code
'''
def recursion(n):
    if n==0:
        return 0
    if n==1:
        return 1
    return recursion(n-1)+recursion(n-2)
n=int(input())
print(recursion(n))


