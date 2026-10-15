# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        second = slow.next
        slow.next = None
        prev, curr = None, second
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        
        curr1, curr2 = head, prev
        while curr2:
            tmp1, tmp2 = curr1.next, curr2.next
            curr1.next = curr2
            curr2.next = tmp1
            curr1, curr2 = tmp1, tmp2
        
       


        
        
