"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        oldToNew = {}
        def dfs(root):
            if root in oldToNew:
                return oldToNew[root]
    
            oldToNew[root] = Node(root.val)
            for neighbor in root.neighbors:    
                neighborCopy = dfs(neighbor)
                oldToNew[root].neighbors.append(neighborCopy)

            return oldToNew[root]
            
        return dfs(node) if node else None
