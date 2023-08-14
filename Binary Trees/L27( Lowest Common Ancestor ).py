# Problem:
'''
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia:
“The lowest common ancestor is defined between two nodes p and q
as the lowest node in T that has both p and q as descendants
(where we allow a node to be a descendant of itself).”

'''
#Complexity
'''
Tc-> O(N)
Sc-> O(N)
'''

class TreeNode:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
        
def LCA(root,p,q):
    if not root or root.val==p or root.val==q:
        return root
    Left=LCA(root.left,p,q)
    Right=LCA(root.right,p,q)
    if not Left:
        return Right
    elif not Right:
        return Left
    else:
        return root

root=TreeNode(1)
root.left=TreeNode(2)
root.right=TreeNode(3)
root.left.left=TreeNode(4)
root.left.right=TreeNode(5)
root.left.right.left=TreeNode(6)
root.left.right.right=TreeNode(7)
root.right.left=TreeNode(8)
root.right.right=TreeNode(9)

node=LCA(root,5,8)

print(node.val)
