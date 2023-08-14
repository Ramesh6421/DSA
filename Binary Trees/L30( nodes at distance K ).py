# problem ( https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/ )
'''
Given the root of a binary tree, the value of a target node target, and an integer k,
return an array of the values of all nodes that have a distance k from the target node.
You can return the answer in any order.

Input: root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, k = 2
Output: [7,4,1]
Explanation: The nodes that are a distance 2 from the target node (with value 5) have values 7, 4, and 1.

'''
# Complexity
'''
Tc-> O(N)+O(N)
Sc-> O(N)*4
'''
class TreeNode:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
def mark_parents(root):
    mark_p={}
    queue=[root]
    while queue:
        cur=queue.pop(0)
        if cur.left:
            mark_p[cur.left]=cur
            queue.append(cur.left)
        if cur.right:
            mark_p[cur.right]=cur
            queue.append(cur.right)
    return mark_p
def nodes_at_distance_k(root,target,k):
    mark_p=mark_parents(root)
    #print(mark_p)
    queue=[target]
    visited=[target]
    level=0
    while queue:
        size=len(queue)
        if level==k:
            break   
        for i in range(size):
            cur=queue.pop(0)
            #print(cur.val)
            if cur.left and cur.left not in visited:
                queue.append(cur.left)
                visited.append(cur.left)
            if cur.right and cur.right not in visited:
                queue.append(cur.right)
                visited.append(cur.right)
            if cur in mark_p and mark_p[cur] not in visited:
                queue.append(mark_p[cur])
                visited.append(mark_p[cur])
        level+=1
    result=[]
    while queue:
        cur=queue.pop(0)
        result.append(cur.val)
    return result
        
root=TreeNode(3)
root.left=TreeNode(5)
root.right=TreeNode(1)
root.left.left=TreeNode(6)
root.left.right=TreeNode(2)
root.right.left=TreeNode(0)
root.right.right=TreeNode(8)
ans=nodes_at_distance_k(root,5,2)
print(ans)
                
                
        
        
    
    
    
            
            
            
        
        
    
    
        
