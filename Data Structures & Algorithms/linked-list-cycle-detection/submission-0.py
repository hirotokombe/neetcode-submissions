# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        hashSet = set()
        curr = head
        while curr:
            hashSet.add(curr)
            if curr.next in hashSet:
                return True
            curr = curr.next
        
        return False