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
    def findFloor(self,root,x):
        floor=-1
        while root:
            if root.val==x:
                return x
            if x<root.val:
                root=root.left
            else:
                floor=root.val
                root=root.right
        return floor

root=TreeNode(2)
root.left=TreeNode(1)
root.right=TreeNode(3)

Obj=Solution()

ans=Obj.findFloor(root,7)
print(ans)

