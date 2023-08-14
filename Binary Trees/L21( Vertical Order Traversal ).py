class TreeNode:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

def vertical_Order(root):
    dic={}
    queue=[]
    queue.append([root,0,0])
    while queue:
        p=queue.pop(0)
        temp=p[0]
        x=p[1]
        y=p[2]
        if x not in dic:
            dic[x]=[]
            dic[x].append((y,temp.val))
        else:
            dic[x].append((y,temp.val))
        if temp.left:
            queue.append([temp.left,x-1,y+1])
        if temp.right:
            queue.append([temp.right,x+1,y+1])
    ans=[]
    for k in sorted(dic.keys()):
        cur=[i[1] for i in sorted(dic[k])]
        ans.append(cur)
    return ans    
        
root=TreeNode(1)
root.left=TreeNode(2)
root.left.left=TreeNode(4)
root.left.right=TreeNode(10)
root.right=TreeNode(3)
root.right.left=TreeNode(9)
root.right.right=TreeNode(11)
root.left.left.right=TreeNode(5)
root.left.left.right.right=TreeNode(6)

print(vertical_Order(root))            
            
            
        
