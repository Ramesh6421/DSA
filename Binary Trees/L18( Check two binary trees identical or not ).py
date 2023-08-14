class TreeNode:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

def check_identical(p,q):
    if not p and not q:
        return True
    if not p or not q:
        return False
    
    return (p.val==q.val) and (check_identical(p.left,q.left)) and (check_identical(p.right,q.right))



root1=TreeNode(1)
root1.left=TreeNode(2)
root1.right=TreeNode(3)
root1.left.left=TreeNode(4)
root1.left.right=TreeNode(5)
root1.left.right.left=TreeNode(6)
root1.right.left=TreeNode(7)
root1.right.right=TreeNode(8)



root2=TreeNode(1)
root2.left=TreeNode(2)
root2.right=TreeNode(3)
root2.left.left=TreeNode(4)
root2.left.right=TreeNode(5)
root2.left.right.left=TreeNode(6)
root2.right.left=TreeNode(7)
root2.right.right=TreeNode(8)

print(check_identical(root1,root2))
