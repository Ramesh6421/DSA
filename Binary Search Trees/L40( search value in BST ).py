class TreeNode:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

class Solution:
    # Iterative approach
    # Complexity
    '''
    TC-> logN
    '''
    def iterative(self,root,val):
        while root:
            if val==root.val:
                return root
            elif val<=root.val:
                root=root.left
            else:
                root=root.right
        return None

    # Recursive approach
    # Complexity
    '''
    TC-> logN
    SC-> O(H)
    '''
    def recursive(self,root,k):
        if not root:
            return None
        if root.val==k:
            return root
        L=R=None
        if k<root.val:
            L=self.recursive(root.left,k)
        if k>root.val:
            R=self.recursive(root.right,k)
        return L or R
        
root=TreeNode(1)
root.left=TreeNode(2)
root.right=TreeNode(3)

Obj=Solution()

node=Obj.iterative(root,3)
print(node)

node=Obj.recursive(root,3)
print(node)
