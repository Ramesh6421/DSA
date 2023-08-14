class TreeNode:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None


def check_balance(root):
    if not root:
        return 0
    lh=check_balance(root.left)
    if lh==-1:
        return -1
    rh=check_balance(root.right)
    if rh==-1:
        return -1
    if abs(lh-rh)>1:
        return -1
    return 1+max(lh,rh)

root=TreeNode(1)
root.left=TreeNode(2)
root.right=TreeNode(3)
root.left.left=TreeNode(4)
root.left.right=TreeNode(5)
root.left.right.left=TreeNode(6)
root.right.left=TreeNode(7)
root.right.right=TreeNode(8)

ans=check_balance(root)
if ans==-1:
    print("False")
else:
    print("True")
    
