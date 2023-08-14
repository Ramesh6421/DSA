# Inorder successor/predecessor:
'''
Successor:
    Given a root of BST and node,return the next greater value than given node.

Predecessor:
    Given a root of BST and node,return the next smallest value than given node.'''
# Complexity
'''
TC-> O(H)
SC-> O(1)
'''
class TreeNode:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

def successor(root,node):
    res=None
    while root:
        if node.val>=root.val:
            root=root.right
        else:
            res=root
            root=root.left
    return res

def predecessor(root,node):
    res=None
    while root:
        if node.val<=root.val:
            root=root.left
        else:
            res=root
            root=root.right
    return res


root=TreeNode(5)
root.left=TreeNode(3)
root.right=TreeNode(7)
root.left.left=TreeNode(2)
root.left.right=TreeNode(4)
root.right.left=TreeNode(6)
root.right.right=TreeNode(9)
root.left.left.left=TreeNode(1)
root.right.right.left=TreeNode(8)
root.right.right.right=TreeNode(10)


#successor
node=root.right.right.left #8
ans=successor(root,node)
print(ans.val) #9

#predecessor
node=root.left.right #4            
ans=predecessor(root,node)
print(ans.val) #3
