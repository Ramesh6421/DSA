# Boundary traversal
'''
TC-> O(N)
SC-> O(N)
'''
class TreeNode:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

def isleaf(node):
    if not node.right and not node.left:
        return True
    return False

def leftBoundary(node,ans):
    cur=node.left
    while cur:
        if not (isleaf(cur)):
            ans.append(cur.val)
        if cur.left:
            cur=cur.left
        else:
            cur=cur.right

def rightBoundary(node,ans):
    cur=node.right
    R=[]
    while cur:
        if not isleaf(cur):
            R.append(cur.val)
        if cur.right:
            cur=cur.right
        else:
            cur=cur.left
    
    R.reverse()
    for i in R:
        ans.append(i)
    
def leaves(node,ans):
    if isleaf(node):
        ans.append(node.val)
    if node.left:
        leaves(node.left,ans)
    if node.right:
        leaves(node.right,ans)


root=TreeNode(1)
root.left=TreeNode(2)
root.right=TreeNode(7)
root.left.left=TreeNode(3)
root.right.right=TreeNode(8)
root.left.left.right=TreeNode(4)
root.left.left.right.left=TreeNode(5)
root.left.left.right.right=TreeNode(6)
root.right.right.left=TreeNode(9)
root.right.right.left.left=TreeNode(10)
root.right.right.left.right=TreeNode(11)

ans=[]
if not root:
    print(ans)
elif isleaf(root):
    ans=[root.val]
    print(ans)
else:
    ans=[root.val]
    leftBoundary(root,ans)
    leaves(root,ans)
    rightBoundary(root,ans)
    print(ans)
    
        
        
            
