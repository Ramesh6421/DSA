class TreeNode:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

def iter_postOrder(root):
    ans=[]
    if not root:
        return ans
    stack=[]
    while root or stack:
        if root:
            stack.append(root)
            root=root.left
        else:
            temp=stack[-1].right
            if not temp:
                temp=stack.pop()
                ans.append(temp.val)
                while stack and temp==(stack[-1].right):
                    temp=stack.pop()
                    ans.append(temp.val)
            else:
                root=temp
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

    
