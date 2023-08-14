# problem (link: https://leetcode.com/problems/kth-smallest-element-in-a-bst/ )
'''
Given the root of a binary search tree, and an integer k,
return the kth smallest value (1-indexed) of all the values of the nodes in the tree.

Input: root = [3,1,4,null,2], k = 1
Output: 1

'''
class TreeNode:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

# Approach-1
# Complexity
'''
TC-> O(N)
SC-> O(N)+O(N)
'''
def inorder1(root,arr=[]):
    if not root:
        return 
    inorder1(root.left)
    arr.append(root.val)
    inorder1(root.right)
    return arr

root=TreeNode(3)
root.left=TreeNode(1)
root.right=TreeNode(4)
root.left.right=TreeNode(2)

k=2
array=inorder1(root)
print(array[k-1])

#Approach-2
# Complexity
'''
TC-> O(N)
SC-> O(N)
'''
def inorder2(root,ans,count=[0]):
    if not root:
        return 
    inorder2(root.left,ans,count)
    count[0]+=1
    if count[0]==k:
        ans[0]=root.val
        return
    inorder2(root.right,ans,count)

root=TreeNode(3)
root.left=TreeNode(1)
root.right=TreeNode(4)
root.left.right=TreeNode(2)

k=2
ans=[0]
inorder2(root,ans)
print(ans[0])
