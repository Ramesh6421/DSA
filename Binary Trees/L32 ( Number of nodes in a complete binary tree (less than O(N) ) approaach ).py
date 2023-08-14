# Problem: (https://leetcode.com/problems/count-complete-tree-nodes/)
'''
Given the root of a complete binary tree, return the number of the nodes in the tree.
According to Wikipedia, every level, except possibly the last, is completely filled in a complete binary tree,
and all nodes in the last level are as far left as possible.
It can have between 1 and 2h nodes inclusive at the last level h.

Design an algorithm that runs in less than O(n) time complexity.
Input: root = [1,2,3,4,5,6]
Output: 6

'''
# Complexity
'''
TC->O(lon^2N)
Sc->O(H)
'''
class TreNode:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

def leftheight(root):
    ht=0
    while root:
        ht+=1
        root=root.left
    return ht
def rightheight(root):
    ht=0
    while root:
        ht+=1
        root=root.right
    return ht
def height(root):
    if not root:
        return 0
    lh=leftheight(root)
    rh=rightheight(root)
    if lh==rh:
        return (2**lh)-1
    return 1+height(root.left)+height(root.right)

ans=height(root)
print(ans)
