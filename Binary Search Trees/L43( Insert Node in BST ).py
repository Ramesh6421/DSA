class TreeNode:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

class Solution:
    # Iterative approach
    def insert_iter(self,root,val):
        node=TreeNode(val)
        if not root:
            return node
        cur=root
        while True:
            if cur.val<=val:
                if cur.right:
                    cur=cur.right
                else:
                    cur.right=node
                    break
            else:
                if cur.left:
                    cur=cur.left
                else:
                    cur.left=node
                    break
        return root

    # Recursive approach
    def insert_rec(self,root,val):
        if not root:
            node=TreeNode(val)
            return node
        if root.val<=val:
            if root.right:
                self.insert_rec(root.right,val)
            else:
                node=TreeNode(val)
                root.right=node
                return
        else:
            if root.left:
                self.insert_rec(root.left,val)
            else:
                node=TreeNode(val)
                root.left=node
                return


root=TreeNode(4)
root.left=TreeNode(2)
root.right=TreeNode(7)
root.left.left=TreeNode(1)
root.left.right=TreeNode(3)

obj=Solution()
ans=obj.insert_iter(root,5)
print(ans)

obj.insert_rec(root,8)
print(root)
