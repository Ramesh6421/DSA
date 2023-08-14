# problem: link( https://leetcode.com/problems/two-sum-iv-input-is-a-bst/ )
'''
Given the root of a Binary Search Tree and a target number k,
return true if there exist two elements in the BST such that their sum is equal to the given target.

Input: root = [5,3,6,2,4,null,7], k = 9
Output: true

'''
# Complexity
'''
TC->O(N)
SC->O(N)
'''

# Approach using BSTIterator

class TreeNode:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

class BSTIterator:
    def __init__(self,root,isReverse):
        self.reverse=isReverse
        self.stack=[]
        self.pushAll(root)
        
    def pushAll(self,root):
        while root:
            self.stack.append(root)
            if self.reverse==True:
                root=root.right
            else:
                root=root.left
        return  
    def next(self):
        node=self.stack.pop()
        if self.reverse==False:
            self.pushAll(node.right)
        else:
            self.pushAll(node.left)
        return node.val
    
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        if not root:
            return False
        L=BSTIterator(root,False)
        R=BSTIterator(root,True)
        
        i=L.next()
        j=R.next()
        while i<j:
            if i+j==k:
                return True
            elif i+j<k:
                i=L.next()
            else:
                j=R.next()
        return False

obj=Solution()
obj.findTarget(root,k)
