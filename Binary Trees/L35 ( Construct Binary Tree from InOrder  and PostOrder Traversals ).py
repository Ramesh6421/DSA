# problem: (https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/)
'''
Given two integer arrays inorder and postorder where inorder is the inorder traversal of a binary tree
and postorder is the postorder traversal of the same tree, construct and return the binary tree.

Input: inorder = [9,3,15,20,7],
postorder = [9,15,7,20,3]
Output: [3,9,20,null,null,15,7]
 
'''
# Comlexity
'''
TC-> O(N)
SC-> O(N)
'''
class TreeNode:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None


def construct(postorder,postst,postend,inorder,inst,inend,d):
    if postst>postend or inst>inend:
        return None
    root=TreeNode(postorder[postend])
    inRoot=d[postorder[postend]]
    numsleft=inRoot-inst
    L=construct(postorder,postst,postst+numsleft-1,inorder,inst,inRoot-1,d)          
    R=construct(postorder,postst+numsleft,postend-1,inorder,inRoot+1,inend,d)
    root.left=L
    root.right=R
    return root



inorder=[40,20,50,10,60,30]
postorder=[40,50,20,60,30,10]

d={}
ind=0
for i in inorder:
    d[i]=ind
    ind+=1
inst=0
inend=len(inorder)-1
postst=0
postend=len(postorder)-1
ans=construct(postorder,postst,postend,inorder,inst,inend,d)
print(ans)


                                                        
