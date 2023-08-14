# problem ( link: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/ )
'''
Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.

According to the definition of LCA on Wikipedia:
“The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants
(where we allow a node to be a descendant of itself).”

Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
Output: 6
Explanation: The LCA of nodes 2 and 8 is 6.

'''
# Complexity
'''
TC-> O(H)
SC-> None
'''
class TreeNode:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

def LCA(root,p,q):
    while root:
        if p.val<root.val and q.val<root.val:
            root=root.left
        elif p.val>root.val and q.val>root.val:
            root=root.right
        else:
            return root
    return

root=TreeNode(6)
root.left=TreeNode(2)
root.right=TreeNode(8)
root.left.left=TreeNode(0)
root.left.right=TreeNode(4)
root.right.left=TreeNode(7)
root.right.right=TreeNode(9)
root.left.right.left=TreeNode(3)
root.left.right.right=TreeNode(5)

p=root.left #2
q=root.right #8
ans=LCA(root,p,q)
print(ans.val)
