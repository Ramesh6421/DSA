# problem link(https://leetcode.com/problems/merge-k-sorted-lists/)
'''
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.
Merge all the linked-lists into one sorted linked-list and return it.

Example 1:

Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6
'''
# Leetcode linked list solution
'''
from heapq import heapify,heappush,heappop
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:            
        # using heap
        heap=[]
        heapify(heap)
        for L in lists:
            while L:
                heappush(heap,L.val)
                L=L.next
        if not heap:
            return None
        LL=dup=ListNode(heappop(heap))
        while heap:
            dup.next=ListNode(heappop(heap))
            dup=dup.next
        return LL    

lists = [[1,4,5],[1,3,4],[2,6]]
print(mergeKLists(lists))
'''

# solution normal list values (not linked list)

from heapq import heapify,heappush,heappop
def mergeKLists(lists):            
    heap=[]
    heapify(heap)
    for L in lists:
        for i in L:
            heappush(heap,i)

    if not heap:
        return None
    res=[]
    while heap:
        val=heappop(heap)
        res.append(val)
    return res    

lists = [[1,4,5],[1,3,4],[2,6]]
print(mergeKLists(lists))

