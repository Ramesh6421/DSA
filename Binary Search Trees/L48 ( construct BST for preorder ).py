# problem : link(https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal/)
'''
Given an array of integers preorder, which represents the preorder traversal of a BST (i.e., binary search tree),
construct the tree and return its root.

It is guaranteed that there is always possible to find a binary search tree
with the given requirements for the given test cases.

A binary search tree is a binary tree where for every node,
any descendant of Node.left has a value strictly less than Node.val,
and any descendant of Node.right has a value strictly greater than Node.val.

A preorder traversal of a binary tree displays the value of the node first,
then traverses Node.left, then traverses Node.right.

Input: preorder = [8,5,1,7,10,12]
Output: [8,5,10,1,7,null,12]

Input: preorder = [1,3]
Output: [1,null,3]

'''

class TreeNode:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

# Approach-1
# Complexity
'''
TC-> O(N*N)
SC-> O(H)
'''
def construct_From_Preorder(preorder):
    def insert(root,node):
        if root.val<node.val:
            if root.right:
                insert(root.right,node)
            else:
                root.right=node
                return
        else:
            if root.left:
                insert(root.left,node)
            else:
                root.left=node
                return
    if len(preorder)==0:
        return
    root=TreeNode(preorder[0])
    for i in range(1,len(preorder)):
        node=TreeNode(preorder[i])
        insert(root,node)
    return root
preorder = [8,5,1,7,10,12]
root=construct_From_Preorder(preorder)
print(root)

    
# Approach-2
# Complexity
'''
TC-> O(Nlogn)+O(N)
SC-> O(N)+O(N)
'''    
def construct_from_pre_and_inorder(preorder):
    
    def BST(pre,prest,preend,ino,inst,inend,d):
        if prest>preend or inst>inend:
            return None
        root=TreeNode(pre[prest])
        k=d[root.val]
        n=k-inst
        root.left=BST(pre,prest+1,prest+n,ino,inst,k-1,d)
        root.right=BST(pre,prest+n+1,preend,ino,k+1,inend,d)
        return root
    inorder=preorder.copy()
    inorder.sort()
    d={}
    ind=0
    for i in inorder:
        d[i]=ind
        ind+=1
    prest=0
    preend=len(preorder)-1
    inst=0
    inend=len(inorder)-1
    ans=BST(preorder,prest,preend,inorder,inst,inend,d)
    return ans

preorder = [8,5,1,7,10,12]
root = construct_from_pre_and_inorder(preorder)
print(root)

# Approach-3
# Complexity
'''
TC-> O(Nlogn)
SC-> O(N)
'''
def BST(a):
    if not a:
        return None
    root=TreeNode(a[0])
    k=len(a)
    for i in range(1,len(a)):
        if a[i]>a[0]:
            k=i
            break
    root.left=BST(a[1:k])
    root.right=BST(a[k:])
    return root

preorder = [8,5,1,7,10,12]
root = BST(preorder)
print(root)
