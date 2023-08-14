class TreeNode:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

def iter_inOrder(root):
    ans=[]
    stack=[]
    while True:
        if root:
            stack.append(root)
            root=root.left
        else:
            if not stack:
                break
            root=stack.pop()
            ans.append(root.val)
            root=root.right    
    return ans

root=TreeNode(1)
root.left=TreeNode(2)
root.right=TreeNode(3)
root.left.left=TreeNode(4)
root.left.right=TreeNode(5)
root.left.right.left=TreeNode(6)
root.right.left=TreeNode(7)
root.right.right=TreeNode(8)

print(iter_inOrder(root))    
