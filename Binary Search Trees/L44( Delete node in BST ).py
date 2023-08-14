# problem ( link: https://leetcode.com/problems/delete-node-in-a-bst/ )
'''
Given a root node reference of a BST and a key, delete the node with the given key in the BST.
Return the root node reference (possibly updated) of the BST.

Basically, the deletion can be divided into two stages:

Search for a node to remove.
If the node is found, delete the node.

Input: root = [5,3,6,2,4,null,7], key = 3
Output: [5,4,6,2,null,null,7]
Explanation: Given key to delete is 3. So we find the node with value 3 and delete it.
One valid answer is [5,4,6,2,null,null,7], shown in the above BST.
Please notice that another valid answer is [5,2,6,null,4,null,7] and it's also accepted.

'''
# Complexity
'''
TC-> O(H)
SC-> None
'''
class TreeNode:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

def helper(root):
    if not root.left:
        return root.right
    if not root.right:
        return root.left
    rightchild=root.right
    lastright=findlastright(root.left)
    lastright.right=rightchild
    return root.left
        
def findlastright(root):
    if not root.right:
        return root
    return findlastright(root.right)

def solve(root,key):        
    if not root:
        return None
    if root.val==key:
        return helper(root)
    dummy=root
    while root!=None:
        if root.val>key:
            if root.left and root.left.val==key:
                root.left=helper(root.left)
                break
            else:
                root=root.left
        else:
            if root.right and root.right.val==key:
                root.right=helper(root.right)
                break
            else:
                root=root.right
    return dummy

root=TreeNode(8)
root.left=TreeNode(5)
root.right=TreeNode(12)
root.left.left=TreeNode(2)
root.left.right=TreeNode(7)
root.right.left=TreeNode(10)
root.right.right=TreeNode(13)
root.left.left.left=TreeNode(1)
root.left.left.right=TreeNode(3)
root.left.right.left=TreeNode(6)
root.left.right.right=TreeNode(8)
root.left.left.right.right=TreeNode(4)

ans_root=solve(root,5)
print(ans_root)
