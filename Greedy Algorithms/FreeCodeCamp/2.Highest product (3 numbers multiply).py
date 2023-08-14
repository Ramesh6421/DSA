# problem: link(https://www.interviewbit.com/problems/highest-product/)
'''
Given an array A, of N integers A.
Return the highest product possible by multiplying 3 numbers from the array.

N>=3
A=[0,0,-5,1,1,5,-2,-1]
output:50

'''

def highest(A):
    A.sort() 
    first = A[-1]*A[-2]*A[-3]
    second = A[0]*A[1]*A[-1]
    return max(first,second)

A=[0,0,-5,1,1,5,-2,-1]
print(highest(A))
