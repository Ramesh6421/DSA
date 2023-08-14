#Problem Description
'''
Given an array of size n, find the majority element. The majority element is the element that appears more than floor(n/2) times.
You may assume that the array is non-empty and the majority element always exist in the array.

Example :
Input : [2, 1, 2]
Return  : 2 which occurs 2 times which is greater than 3/2.
'''
# Complexity
'''
TC-> O(N)
SC-> O(N)
'''
from collections import Counter
def solve(A):
    return Counter(A).most_common(1)[0][0]

A=[3,2,2,4,2,2]
print(solve(A))
