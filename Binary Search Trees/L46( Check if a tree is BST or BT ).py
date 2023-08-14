# problem ( link: https://leetcode.com/problems/validate-binary-search-tree/ )
'''
Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.

Input: root = [2,1,3]
Output: true

Input: root = [5,1,4,null,null,3,6]
Output: false

'''
# Complexity
'''
TC-> O(N)
SC-> O(H)
'''
class TreeNode:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

from sys import maxsize

def validBST(root,mn,mx):
    if not root:
        return True
    if root.val>=mx or root.val<=mn:
        return False
    L=validBST(root.left,mn,root.val)
    R=validBST(root.right,root.val,mx)
    return L and R

root=TreeNode(5)
root.left=TreeNode(1)
root.right=TreeNode(4)
root.right.left=TreeNode(3)
root.right.right=TreeNode(6)

mn=-(maxsize-1)
mx=maxsize
ans=validBST(root,mn,mx)    
print(ans)        
