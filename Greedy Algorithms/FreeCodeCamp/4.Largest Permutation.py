#Problem Description
'''
Given an integer array A of size N consisting of unique integers from 1 to N. You can swap any two integers atmost B times.
Return the largest lexicographical value array that can be created by executing atmost B swaps.

Problem Constraints
1 <= N <= 106
1 <= B <= 109

Input Format
First argument is an integer array A of size N.
Second argument is an integer B.

Output Format
Return an integer array denoting the largest lexicographical value array that can be created by executing atmost B swaps.

Example Input
Input 1:

 A = [1, 2, 3, 4]
 B = 1
Input 2:

 A = [3, 2, 1]
 B = 2

Example Output
Output 1:
 [4, 2, 3, 1]

Output 2:
 [3, 2, 1]
'''

#Complexity
'''
TC-> O(N)+O(N)
SC-> O(N)
'''

def solve(A,B):
    d={}
    for i in range(len(A)):
        d[A[i]]=i               # storing the index values of array A
    maxx=len(A)
    for i in range(len(A)):
        if B==0:
            break
        if A[i]!=maxx:
            j = d[maxx] 
            A[i],A[j]=A[j],A[i]     # swapping the array values
            d[A[i]],d[A[j]]=d[A[j]],d[A[i]]    # swapping the indexes in dictionary
            B=B-1          # reducing the number of swaps
        maxx-=1          # reducing the highest number
    return A        

A = [1, 2, 3, 4]
B = 1
print(solve(A,B))
