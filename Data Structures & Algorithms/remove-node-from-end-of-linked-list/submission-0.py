# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)

        def dfs(node):
            if not node:
                return 0

            count = 1 + dfs(node.next)

            if count == n + 1:
                node.next = node.next.next

            return count

        dfs(dummy)
        return dummy.next
        
         