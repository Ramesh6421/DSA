class TreeNode:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

def zig_zag(root):
    ans=[]
    if not root:
        return ans
    queue=[root]
    flag=0
    while queue:
        size=len(queue)
        level=[]
        for i in range(size):
            node=queue.pop(0)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            if flag==1:
                level=[node.val]+level
            if flag==0:
                level.append(node.val)
        ans.append(level)
        if flag==0:
            flag=1
        else:
            flag=0
    return ans        
        
    
root=TreeNode(1)
root.left=TreeNode(2)
root.right=TreeNode(3)
root.left.left=TreeNode(4)
root.left.right=TreeNode(5)
root.left.right.left=TreeNode(6)
root.right.left=TreeNode(7)
root.right.right=TreeNode(8)

print(zig_zag(root))
