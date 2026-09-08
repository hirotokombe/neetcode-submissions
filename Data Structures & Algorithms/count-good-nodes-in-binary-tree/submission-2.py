# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0
        def dfs(node, maxVal):
            nonlocal count

            if not node:
                return 

            maxVal = max(maxVal, node.val)
            if max(maxVal, node.val) == node.val:
                count += 1

            dfs(node.left, maxVal)
            dfs(node.right, maxVal)
            
            
     
            
            return count

        count = dfs(root, root.val)
        return count