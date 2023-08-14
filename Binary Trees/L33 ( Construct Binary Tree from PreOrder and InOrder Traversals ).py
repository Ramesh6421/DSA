# Problem:
'''
Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree
and inorder is the inorder traversal of the same tree, construct and return the binary tree.

Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
Output: [3,9,20,null,null,15,7] 
'''
# Complexity
'''
TC-> O(N)
SC-> O(N)
'''
class TreeNode:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

def construct(preorder,prest,preend,inorder,inst,inend,d):
    if prest>preend or inst>inend:
        return None
    root=TreeNode(preorder[prest])
    elem=d[root.val]
    nelem=elem-inst
    root.left=construct(preorder,prest+1,prest+nelem,inorder,inst,elem-1,d)
    root.right=construct(preorder,prest+nelem+1,preend,inorder,elem+1,inend,d)
    return root


preorder=[10,20,40,50,30,60]
inorder=[40,20,50,10,60,30]

d={}
ind=0
for i in inorder:
    d[i]=ind
    ind+=1
prest=0
preend=len(preorder)-1
inst=0
inend=len(inorder)-1
ans=construct(preorder,prest,preend,inorder,inst,inend,d)
print(ans)        
