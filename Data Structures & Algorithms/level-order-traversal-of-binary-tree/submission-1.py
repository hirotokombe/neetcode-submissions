# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque()
        lst = []
        if root:
            queue.append(root)
        while len(queue) > 0:
            level = []
            for i in range(len(queue)):
                curr = queue.popleft()
                level.append(curr.val)
                currLeft, currRight = curr.left, curr.right
                if currLeft:
                    queue.append(curr.left)
                if currRight:
                    queue.append(curr.right)
            lst.append(level)
        return lst