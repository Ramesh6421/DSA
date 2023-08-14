class TreeNode:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

def iter_postOrder(root):
    ans=[]
    if not root:
        return ans
    stack=[root]
    while stack:
        node=stack.pop()
        ans.append(node.val)
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)

    ans.reverse()
    return ans

root=TreeNode(1)
root.left=TreeNode(2)
root.right=TreeNode(3)
root.left.left=TreeNode(4)
root.left.right=TreeNode(5)
root.left.right.left=TreeNode(6)
root.right.left=TreeNode(7)
root.right.right=TreeNode(8)

print(iter_postOrder(root))

    
