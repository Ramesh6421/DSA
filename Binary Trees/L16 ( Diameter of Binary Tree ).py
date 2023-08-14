# Brute Force Approach
'''
-> for every node finding the maximum depth of left subtree and right subtree
-> i.e, max_depth(left_subtree)+max_depth(right_subtree)
-> Take max of all the nodes

'''
# Complexity
'''
TC-> O(N*N)
SC-> O(1)+O(H)  H is height of tree
'''
class TreeNode:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

# maximum depth of tree
def max_depth(root):
    if not root:
        return 0
    lh=max_depth(root.left)
    rh=max_depth(root.right)
    return 1+max(lh,rh)

# traversing every node
def pre_order(root):
    if not root:
        return 0
    lh=max_depth(root.left)
    rh=max_depth(root.right)
    ans[0]=max(ans[0],lh+rh)
    pre_order(root.left)
    pre_order(root.right)
    
    

root=TreeNode(1)
root.left=TreeNode(2)
root.right=TreeNode(3)
root.left.left=TreeNode(4)
root.left.right=TreeNode(5)
root.left.right.left=TreeNode(6)
root.right.left=TreeNode(7)
root.right.right=TreeNode(8)

ans=[0]
pre_order(root)
print(ans[0])    



# Approach - 2
#complexity
'''
TC-> O(N)
SC-> o(1)
'''

# maximum depth of tree
def max_depth(root):
    if not root:
        return 0
    lh=max_depth(root.left)
    rh=max_depth(root.right)
    ans[0]=max(ans[0],lh+rh)
    return 1+max(lh,rh)

root=TreeNode(1)
root.left=TreeNode(2)
root.right=TreeNode(3)
root.left.left=TreeNode(4)
root.left.right=TreeNode(5)
root.left.right.left=TreeNode(6)
root.right.left=TreeNode(7)
root.right.right=TreeNode(8)

ans=[0]
max_depth(root)
print(ans[0])
    
