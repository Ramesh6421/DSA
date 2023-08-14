# problem link(https://leetcode.com/problems/sliding-window-maximum/)

'''
You are given an array of integers nums,
there is a sliding window of size k which is moving from the very left of the array to the very right.
You can only see the k numbers in the window. Each time the sliding window moves right by one position.
Return the max sliding window.

Example 1:

Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
Explanation: 
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7

'''

# Approach - 1 ( using double ended queue )

from heapq import heapify,heappush,heappop
def maxSlidingWindow(nums,k): 
    res=[]
    n=len(nums)
    deque=[]
    for i in range(n):
        if len(deque)>0 and deque[0][1]<=(i-k):
            deque.pop(0)
        while deque and deque[-1][0]<nums[i]:
            deque.pop()
        deque.append((nums[i],i))
        if i>=(k-1):
            res.append(deque[0][0])
    return res        

nums = [1,3,-1,-3,5,3,6,7]
k = 3
print(maxSlidingWindow(nums,k))


# Approach - 2 ( using heaps )
from heapq import heapify,heappush,heappop
def maxSlidingWindow(nums,k):
    res=[]
    n=len(nums)
    nums=[-1*i for i in nums]
    heap=[]
    heapify(heap)
    for i in range(n):
        while heap and heap[0][1]<=i-k:
            heappop(heap)
        heappush(heap,(nums[i],i))
        if i>=k-1:
            res.append(heap[0][0]*-1)
    return res        

nums = [1,3,-1,-3,5,3,6,7]
k = 3
print(maxSlidingWindow(nums,k))
        
