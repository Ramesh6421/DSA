from sys import maxsize
class TreeNode:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

# Complexity
'''
TC->O(N)
SC->O(3)
'''
def largerBST(root):
    if not root:
        return [maxsize,-(maxsize-1),0]
    L=largerBST(root.left)
    R=largerBST(root.right)
    if L[0]<root.val<R[1]:
        mn=min(root.val,L[1])
        mx=max(root.val,R[0])
        nodes=1+L[2]+R[2]
        return [mn,mx,nodes]
    return [-(maxsize-1),maxsize,max(L[2],R[2])]
    

root=TreeNode(20)
root.left=TreeNode(15)
root.right=TreeNode(40)
root.left.left=TreeNode(14)
root.left.right=TreeNode(18)
root.right.left=TreeNode(30)
root.right.right=TreeNode(60)
root.left.left.right=TreeNode(17)
root.left.right.left=TreeNode(16)
root.left.right.right=TreeNode(19)
root.right.right.left=TreeNode(50)

ans=largerBST(root)
res=ans[2]
print(res)
        
