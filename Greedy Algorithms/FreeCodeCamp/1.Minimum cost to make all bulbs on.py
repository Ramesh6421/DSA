#Problem Description link(https://www.interviewbit.com/problems/interview-questions/)
''' 
N light bulbs are connected by a wire.
Each bulb has a switch associated with it, however due to faulty wiring,
a switch also changes the state of all the bulbs to the right of current bulb.
Given an initial state of all bulbs, find the minimum number of switches you have to press to turn on all the bulbs.
You can press the same switch multiple times.

Note : 0 represents the bulb is off and 1 represents the bulb is on.

Problem Constraints
0 <= N <= 5e5
0 <= A[i] <= 1

Input Format
The first and the only argument contains an integer array A, of size N.

Output Format
Return an integer representing the minimum number of switches required.

Example Input
A = [0 1 0 1]

Example Output
4

Example Explanation
press switch 0 : [1 0 1 0]
press switch 1 : [1 1 0 1]
press switch 2 : [1 1 1 0]
press switch 3 : [1 1 1 1]
'''
# Bruteforce Approach
# Complexity
'''
TC-> O(N*N)
SC->O(1)
'''
def minCost(A):
    cost=0 
    for i in range(len(A)):
        if A[i]==0:
            cost+=1
            for j in range(i,len(A)):
                if A[j]==0:
                    A[j]=1
                else:
                    A[j]=0 
    return cost

A=[0,1,0,1]
ans=minCost(A)
print(ans)

# Optimized Approach
# Complexity
'''
TC-> O(N)
SC-> O(1)
'''
def minCost(A):
    cost=0 
    for i in range(len(A)):
        if cost%2==0:
            if A[i]==0:
                cost+=1
        else:
            if A[i]==1:
                cost+=1
    return cost

A=[0,1,0,1]
ans=minCost(A)
print(ans)
