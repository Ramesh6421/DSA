#Problem Description: link(https://www.interviewbit.com/problems/assign-mice-to-holes/)
'''
There are N Mice and N holes that are placed in a straight line. Each hole can accomodate only 1 mouse.
The positions of Mice are denoted by array A and the position of holes are denoted by array B.
A mouse can stay at his position, move one step right from x to x + 1, or move one step left from x to x − 1.
Any of these moves consumes 1 minute.
Assign mice to holes so that the time when the last mouse gets inside a hole is minimized.

Problem Constraints
1 <= N <= 105
-109 <= A[i], B[i] <= 109

Input Format
First argument is an integer array A.
Second argument is an integer array B.

Output Format
Return an integer denoting the minimum time when the last nouse gets inside the holes.

Example Input
Input 1:

 A = [-4, 2, 3]
 B = [0, -2, 4]
Input 2:

 A = [-2]
 B = [-6]

Example Output
Output 1:

 2
Output 2:

 4
 
'''
# Complexity
'''
TC-> O(NlogN)*2+O(N)
SC-> O(1)
'''
def solve(A,B):
    A.sort()
    B.sort()
    ans=0
    for i in range(len(A)):
        cur=abs(A[i]-B[i])
        ans=max(cur,ans)
    return ans

A = [-4, 2, 3]
B = [0, -2, 4]
print(solve(A,B))
