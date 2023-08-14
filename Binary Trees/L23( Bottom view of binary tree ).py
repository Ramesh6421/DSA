class TreeNode:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

def bottomView(root):
    dic={}
    if not root:
        return []
    queue=[(root,0)]
    while queue:
        temp=queue.pop(0)
        vertical=temp[1]
        node=temp[0]
        dic[vertical]=node.val
        if node.left:
            queue.append((node.left,vertical-1))
        if node.right:
            queue.append((node.right,vertical+1))
            
    d=[i[1] for i in sorted(dic.items())]
    return d

root=TreeNode(1)
root.left=TreeNode(2)
root.right=TreeNode(3)
root.left.left=TreeNode(4)
root.left.right=TreeNode(5)
root.right.left=TreeNode(6)
root.right.right=TreeNode(7)
print(bottomView(root))
