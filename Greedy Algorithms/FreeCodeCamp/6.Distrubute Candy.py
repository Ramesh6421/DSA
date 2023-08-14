# problem description: link(https://www.interviewbit.com/problems/distribute-candy/)
'''
There are N children standing in a line. Each child is assigned a rating value.
You are giving candies to these children subjected to the following requirements:
1. Each child must have at least one candy.
2. Children with a higher rating get more candies than their neighbors.
What is the minimum candies you must give?

Input Format:

The first and the only argument contains N integers in an array A.
Output Format:

Return an integer, representing the minimum candies to be given.
Example:

Input 1:
    A = [1, 2]

Output 1:
    3

Explanation 1:
    The candidate with 1 rating gets 1 candy and candidate with rating cannot get 1 candy as 1 is its neighbor. 
    So rating 2 candidate gets 2 candies. In total, 2 + 1 = 3 candies need to be given out.

Input 2:
    A = [1, 5, 2, 1]

Output 2:
    7

Explanation 2:
    Candies given = [1, 3, 2, 1]
'''
# Complexity
'''
TC-> O(N)+O(N)
SC-> O(N)+O(N)
'''
def solve(A):
    n=len(A)
    data=[]
    for i in range(n):
        data.append((A[i],i))
    data.sort() 
    candies = [1]*n
    for x,i in data:
        if i>0 and A[i]>A[i-1]:
            candies[i]=max(candies[i],candies[i-1]+1)
        if i<n-1 and A[i]>A[i+1]:
            candies[i]=max(candies[i],candies[i+1]+1)
          
    return sum(candies)
n=int(input())
A = [int(x) for x in input().split()]
print(solve(A))
