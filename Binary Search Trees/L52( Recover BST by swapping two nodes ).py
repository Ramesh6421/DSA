# problem link( https://leetcode.com/problems/recover-binary-search-tree/ )
'''
You are given the root of a binary search tree (BST),
where the values of exactly two nodes of the tree were swapped by mistake.
Recover the tree without changing its structure.

Input: root = [3,1,4,null,null,2]
Output: [2,1,4,null,null,3]
Explanation: 2 cannot be in the right subtree of 3 because 2 < 3. Swapping 2 and 3 makes the BST valid.

'''
# Complexity
'''
TC->O(N)
SC->O(N)
'''

class TreeNode:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

#Approach-1
#Complexity
'''
TC->O(N)+O(N)
SC->O(N)+O(N)
'''
def preOrder(root,arr=[]):
    if not root:
        return arr
    arr.append(root.val)
    preOrder(root.left)
    preOrder(root.right)
    return arr
a=preOrder(root)
a.sort()
i=[0]
def inOrder(root,i):
    if not root:
        return
    inOrder(root.left,i)
    if root.val!=a[i[0]]:
        root.val=a[i[0]]
    i[0]+=1
    inOrder(root.right,i)
inOrder(root,i)
print(root)

#Approach-2
#Complexity
'''
TC->O(N)
SC->O(4)
'''
def inorder(root):
    if not root:
        return
    inorder(root.left)
    if prev[0]!=None and root.val<prev[0].val:
        if first[0] is None:
            first[0]=prev[0]
            middle[0]=root
        else:
            last[0]=root
    prev[0]=root
    inorder(root.right)
        
prev=[None]
first=[None]
middle=[None]
last=[None]
        
inorder(root)
        
if last[0] is None:
    first[0].val,middle[0].val=middle[0].val,first[0].val
else:
    first[0].val,last[0].val=last[0].val,first[0].val

print(root)            
