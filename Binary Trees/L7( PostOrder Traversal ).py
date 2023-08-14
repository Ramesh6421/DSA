class TreeNode:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
        
def postorder(root):
    if not root:
        return
    postorder(root.left)
    postorder(root.right)
    print(root.val,"->",end='')
    
root=TreeNode(1)
root.left=TreeNode(2)
root.right=TreeNode(3)
root.left.left=TreeNode(4)
root.left.right=TreeNode(5)
root.left.right.left=TreeNode(6)
root.right.left=TreeNode(7)
root.right.right=TreeNode(8)

postorder(root)
print( )

