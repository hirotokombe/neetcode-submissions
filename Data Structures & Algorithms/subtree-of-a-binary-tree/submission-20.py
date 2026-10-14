# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
    
        if not subRoot:
            return True
        
        if not root:
            return False
        
        if self.sameTree(root, subRoot):
            return True
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        
    def sameTree(self, node: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not node and not subRoot:
            return True
        
        if node and subRoot and node.val == subRoot.val:
            return self.sameTree(node.left, subRoot.left) and self.sameTree(node.right, subRoot.right)
        
        return False