# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def dfs(head: Optional[TreeNode]):
            curr = head

            if not curr or not curr.left and not curr.right:
                return curr

            dfs(curr.left)
            dfs(curr.right)
            tmp = curr.left
            curr.left = curr.right
            curr.right = tmp
            
            return curr
        
        return dfs(root)