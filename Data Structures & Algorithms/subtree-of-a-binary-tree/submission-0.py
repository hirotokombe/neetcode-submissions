# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def sameTree(root1, root2) -> bool:
            queue1 = deque([root1])
            queue2 = deque([root2])

            while queue1 and queue2:
                for _ in range(len(queue1)):
                    node1 = queue1.popleft()
                    node2 = queue2.popleft()

                    if node1 is None and node2 is None:
                        continue
                    
                    if node1 is None or node2 is None or node1.val != node2.val:
                        return False
                    
                    queue1.append(node1.left)
                    queue1.append(node1.right)
                    queue2.append(node2.left)
                    queue2.append(node2.right)

            return True

  
        if root is None:
            return False

        if sameTree(root, subRoot):
            return True

        return (
            self.isSubtree(root.left, subRoot)
            or
            self.isSubtree(root.right, subRoot)
        )

        
