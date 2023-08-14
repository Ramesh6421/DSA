def mark_Parents(root):
    mp={}
    queue=[root]
    while queue:
        node=queue.pop(0)
        if node.left:
            mp[node.left]=node
            queue.append(node.left)
        if node.right:
            mp[node.right]=node
            queue.append(node.right)
    return mp
def min_Burn(root):
    parentMap=mark_Parents(root)
    queue=[root]
    visited=[root]
    time=0
    while queue:
        size=len(queue)
        for i in range(size):
            node=queue.pop(0)
            if node.left and node.left not in visited:
                queue.append(node.left)
                visited.append(node.left)
            if node.right and node.right not in visited:
                queue.append(node.right)
                visited.append(node.right)
            if node in parentMap and node not in visted:
                queue.append(node)
                visited.append(node)
        time+=1
    return time
ans=min_Burn(root)
return ans
    
