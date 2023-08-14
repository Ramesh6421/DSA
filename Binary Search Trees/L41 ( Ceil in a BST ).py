class TreeNode:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

class Solution:
    # Complexity
    '''
    TC-> logN
    '''
    def findCeil(self,root,x):
        ceil=-1
        while root:
            if root.val==x:
                ceil=root.val
                return ceil
            if x>root.val:
                root=root.right
            else:
                ceil=root.val
                root=root.left
        return ceil      

root=TreeNode(2)
root.left=TreeNode(1)
root.right=TreeNode(3)

Obj=Solution()

ans=Obj.findCeil(root,0)
print(ans)

