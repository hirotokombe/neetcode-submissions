# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        path = []

        def pathEqualsTargetSum(root):
            if not root:
                return False
            path.append(root.val)

            if not root.right and not root.left:
                if sum(path) == targetSum:
                    return True
            if pathEqualsTargetSum(root.left):
                return True
            if pathEqualsTargetSum(root.right):
                return True
            path.pop()
            return False
        return pathEqualsTargetSum(root)