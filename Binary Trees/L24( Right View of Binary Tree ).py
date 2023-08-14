# Approach-1
class TreeNode:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None


def rightView(root):
    ans=[]
    if not root:
        return ans
    queue=[]
    queue.append(root)
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
        ans.append(level[-1])
    return ans  

root=TreeNode(1)
root.left=TreeNode(2)
root.right=TreeNode(3)
root.left.left=TreeNode(4)
root.left.right=TreeNode(5)
root.right.left=TreeNode(6)
root.right.right=TreeNode(7)

print(rightView(root))


# Approach-2

class TreeNode:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
def rightView(root,level,arr=[]):
    if not root:
        return None
    if len(arr)==level:
        arr.append(root.val)
    if root.right:
        rightView(root.right,level+1,arr)
    if root.left:
        rightView(root.left,level+1,arr)
    return arr

root=TreeNode(1)
root.left=TreeNode(2)
root.right=TreeNode(3)
root.left.left=TreeNode(4)
root.left.right=TreeNode(5)
root.right.left=TreeNode(6)
root.right.right=TreeNode(7)
print(rightView(root,0))

	        
