# problem link(https://leetcode.com/problems/kth-largest-element-in-an-array/submissions/)
'''
Given an integer array nums and an integer k, return the kth largest element in the array.
Note that it is the kth largest element in the sorted order, not the kth distinct element.
You must solve it in O(n) time complexity.

Example 1:

Input: nums = [3,2,1,5,6,4], k = 2
Output: 5

'''

from heapq import heapify,heappush,heappop
def findKthLargest(nums,k):
    nums=[i*-1 for i in nums]
    heapify(nums)
    for i in range(k):
        val=heappop(nums)
        if i==k-1:
            return val*-1

nums = [3,2,1,5,6,4]
k = 2

print(findKthLargest(nums,k))
