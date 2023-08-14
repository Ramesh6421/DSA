class TreeNode:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

def max_width(root):
    ans=0
    if not root:
        return ans
    queue=[]
    queue.append((root,0))
    while queue:
        size=len(queue)
        for i in range(size):
            node=queue.pop(0)
            temp=node[0]
            ind=node[1]
            if i==0:
                first=node[1]
            if i==size-1:
                last=node[1]
            if temp.left:
                queue.append((temp.left,ind*2+1))
            if temp.right:
                queue.append((temp.right,ind*2+2))
        ans=max(ans,(last-first+1))
    return ans    

root=TreeNode(1)
root.left=TreeNode(2)
root.right=TreeNode(3)
root.left.left=TreeNode(4)
root.left.right=TreeNode(5)
root.left.right.left=TreeNode(6)
root.left.right.right=TreeNode(7)
root.right.left=TreeNode(8)
root.right.right=TreeNode(9)

print(max_width(root))
