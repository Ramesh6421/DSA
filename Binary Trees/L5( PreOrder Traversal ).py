class TreeNode:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
        
def preorder(root):
    if not root:
        return
    print(root.val,"->",end='')
    preorder(root.left)
    preorder(root.right)

root=TreeNode(1)
root.left=TreeNode(2)
root.right=TreeNode(3)
root.left.left=TreeNode(4)
root.left.right=TreeNode(5)
root.left.right.left=TreeNode(6)
root.right.left=TreeNode(7)
root.right.right=TreeNode(8)

preorder(root)
print( )

