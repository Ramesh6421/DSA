class TreeNode:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None


def childSum(root):
    if not root:
        return
    child=0
    if root.left:
        child+=root.left.val
    if root.right:
        child+=root.right.val
    if child<root.val:
        if root.left:
            root.left.val=root.val
        elif root.right:
            root.right.val=root.val
    childSum(root.left)
    childSum(root.right)
    tot=0
    if root.left:
        tot+=root.left.val
    if root.right:
        tot+=root.right.val
    if root.left or root.right:
        root.val=tot


root=TreeNode(50)
root.left=TreeNode(7)
root.right=TreeNode(2)
root.left.left=TreeNode(3)
root.left.right=TreeNode(5)
root.right.left=TreeNode(1)
root.right.right=TreeNode(30)
childSum(root)
print(root.val)
        
    
        
