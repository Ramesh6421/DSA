# problem link(https://leetcode.com/problems/top-k-frequent-elements/)
'''
Given an integer array nums and an integer k, return the k most frequent elements.
You may return the answer in any order.

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Example 2:

Input: nums = [1], k = 1
Output: [1]

'''

from heapq import heapify,heappop
from collections import Counter

def topKFrequent(nums,k):
    d=Counter(nums)
    values=[-1*i for i in d.values()]
    keys=[i for i in d.keys()]
    heap=list(zip(values,keys))
    heapify(heap)
    res=[]
    for i in range(k):
        cur=heappop(heap)
        res.append(cur[1])
    return res   

nums = [1,1,1,1,2,2,3,3,3]
k = 2    
print(topKFrequent(nums,k))    
    
    
    
    
    
    
    
    
    
    
    
