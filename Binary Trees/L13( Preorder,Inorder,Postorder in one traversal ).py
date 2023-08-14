class TreeNode:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

def pre_in_post(root):
    if not root:
        return []
    pre=[]
    inn=[]
    post=[]
    stack=[[root,1]]
    while stack:
        node=stack.pop()
        if node[1]==1:
            pre.append(node[0].val)
            node[1]+=1
            stack.append(node)
            if node[0].left:
                stack.append([node[0].left,1])
        elif node[1]==2:
            inn.append(node[0].val)
            node[1]+=1
            stack.append(node)
            if node[0].right:
                stack.append([node[0].right,1])
        else:
            post.append(node[0].val)
    return [pre,inn,post]        
                
                         
root=TreeNode(1)
root.left=TreeNode(2)
root.right=TreeNode(3)
root.left.left=TreeNode(4)
root.left.right=TreeNode(5)
root.left.right.left=TreeNode(6)
root.right.left=TreeNode(7)
root.right.right=TreeNode(8)

print(pre_in_post(root))

    
