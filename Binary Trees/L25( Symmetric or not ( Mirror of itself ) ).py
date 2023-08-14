# problem: link:(https://leetcode.com/problems/symmetric-tree/)
'''
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

'''

#Complexity:
'''
TC-> O(N)
SC-> O(N)
'''

class TreeNode:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

def sym(p,q):
    if not p and not q:
        return True
    if not p or not q:
        return False
    if p.val!=q.val:
        return False
    return sym(p.left,q.right) and sym(p.right,q.left)


root=TreeNode(1)
root.left=TreeNode(2)
root.right=TreeNode(2)
root.left.left=TreeNode(3)
root.left.right=TreeNode(4)
root.right.left=TreeNode(4)
root.right.right=TreeNode(3)

print(sym(root.left,root.right))
        
