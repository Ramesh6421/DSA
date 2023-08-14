# problem link(https://leetcode.com/problems/unique-binary-search-trees-ii/)
'''
Given an integer n, return all the structurally unique BST's (binary search trees),
which has exactly n nodes of unique values from 1 to n. Return the answer in any order.

Input: n = 3
Output: [[1,null,2,null,3],[1,null,3,2],[2,1,3],[3,1,null,null,2],[3,2,null,1]] 

'''
# Complexity
'''
TC-> O(N*N*N)
SC-> O(N*N)+O(2**N)
'''
class TreeNode:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

def uniqueBST(st,end):
    if st>end:
        return [None]
    ans=[]
    for root in range(st,end+1):
        L=uniqueBST(st,root-1)
        R=uniqueBST(root+1,end)
        for left in L:
            for right in R:
                node=TreeNode(root)
                node.left=left
                node.right=right
                ans.append(node)
    return ans

n=3
ans=uniqueBST(1,n)
print(ans)
