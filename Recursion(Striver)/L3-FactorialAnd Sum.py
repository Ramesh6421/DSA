'''
sum of N numbers
'''
def recursion(n):
    if n==0:
        return 0
    return n+recursion(n-1)
n=int(input())
print(recursion(n))


'''
Factorial of a number
'''
def recursion(n):
    if n==0:
        return 1
    return n*recursion(n-1)
n=int(input())
print(recursion(n))

