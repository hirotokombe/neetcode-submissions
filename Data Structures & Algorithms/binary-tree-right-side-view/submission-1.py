# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        queue = deque()
        lst = []

        if root:
            queue.append(root)
        
        while len(queue) > 0:
            rightItem = None
            for i in range(len(queue)):
                curr = queue.popleft()
                rightItem = curr.val
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            lst.append(rightItem)
        return lst
