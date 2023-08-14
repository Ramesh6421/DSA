class TreeNode:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

def max_path(root):
    if not root:
        return 0
    left=max(0,max_path(root.left))
    right=max(0,max_path(root.right))
    cur=root.val+left+right
    ans[0]=max(ans[0],cur)
    return max(left,right)+root.val


root=TreeNode(1)
root.left=TreeNode(2)
root.right=TreeNode(3)
root.left.left=TreeNode(4)
root.left.right=TreeNode(5)
root.left.right.left=TreeNode(6)
root.right.left=TreeNode(7)
root.right.right=TreeNode(8)=[0]
max_path(root)
print(ans[0])
