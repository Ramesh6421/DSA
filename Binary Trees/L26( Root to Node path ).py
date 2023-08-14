# Problem: link(https://www.interviewbit.com/problems/path-to-given-node/)
'''
Given a Binary Tree A containing N nodes.
You need to find the path from Root to a given node B.

'''
#Complexity:
'''
TC-> O(N)
SC-> O(N)
'''

class TreeNode:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
        
def root_to_node(root,k,arr):
    if not root:
        return False
    arr.append(root.val)
    if root.val==k:
        return True
    if root_to_node(root.left,k,arr) or root_to_node(root.right,k,arr):
        return True
    arr.pop()
    return False 

root=TreeNode(1)
root.left=TreeNode(2)
root.right=TreeNode(3)
root.left.left=TreeNode(4)
root.left.right=TreeNode(5)
root.left.right.left=TreeNode(6)
root.left.right.right=TreeNode(7)

arr=[]
node=7
root_to_node(root,node,arr) 
print(arr)      
                
                

