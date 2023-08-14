class TreeNode:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None


def max_depth(root):
    if not root:
        return 0
    return 1+max(max_depth(root.left),max_depth(root.right))

def levelorder(root):
    ans=0
    if not root:
        return level
    queue=[root]
    while queue:
        size=len(queue)
        level=[]
        for i in range(size):
            node=queue.pop(0)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            level.append(node.val)    
        ans+=1
    return ans

root=TreeNode(1)
root.left=TreeNode(2)
root.right=TreeNode(3)
root.left.left=TreeNode(4)
root.left.right=TreeNode(5)
root.left.right.left=TreeNode(6)
root.right.left=TreeNode(7)
root.right.right=TreeNode(8)

print(max_depth(root))
print(levelorder(root))
    
