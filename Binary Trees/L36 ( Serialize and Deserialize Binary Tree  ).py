# problem: link(https://leetcode.com/problems/serialize-and-deserialize-binary-tree/)
'''
Serialization is the process of converting a data structure or object into a sequence of bits so that
it can be stored in a file or memory buffer, or transmitted across a network connection link to be
reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree.
There is no restriction on how your serialization/deserialization algorithm should work.
You just need to ensure that a binary tree can be serialized to a string and this string
can be deserialized to the original tree structure.

Clarification: The input/output format is the same as how LeetCode serializes a binary tree.
You do not necessarily need to follow this format,
so please be creative and come up with different approaches yourself.

Input: root = [1,2,3,null,null,4,5]
Output: [1,2,3,null,null,4,5]

'''
# Complexity:
'''
TC-> O(N)
SC-> O(N)
'''

class TreeNode:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

def serialize(root):
    st=''
    if not root:
        return st
    q=[root]
    while q:
        node=q.pop(0)
        if node is None:
            st+='#,'
        else:    
            st+=str(node.val)+','
            q.append(node.left)
            q.append(node.right)
    return st[:-1]

def deserialize(data):
    if len(data)==0:
        return None
    a=[x for x in data.split(',')]
    ind=0
    root=TreeNode(int(a[ind]))
    q=[root]
    while q:
        node=q.pop(0)
        ind+=1
        st=a[ind]
        if st=='#':
            node.left=None
        else:
            leftNode=TreeNode(int(st))
            node.left=leftNode
            q.append(leftNode)
        ind+=1
        st=a[ind]
        if st=='#':
            node.right=None
        else:
            rightNode=TreeNode(int(st))
            node.right=rightNode
            q.append(rightNode)
    return root        
string=serialize(root)
final_root=deserialize(string)
print(final_root)
