# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        queue1 = deque([p])
        queue2 = deque([q])
        
        while queue1 and queue2:
            for i in range(len(queue1)):
                val1 = queue1.popleft()
                val2 = queue2.popleft()

                if val1 is None and val2 is None:
                    continue
                
                if val1 is None or val2 is None or  val1.val != val2.val:
                    return False

                queue1.append(val1.left)
                queue1.append(val1.right)
                queue2.append(val2.left)
                queue2.append(val2.right)
        
        return True
                    
                