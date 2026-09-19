"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        map = defaultdict(lambda : Node(0))
        map[None] = None
    
        curr = head

        while curr:
            map[curr].val = curr.val
            map[curr].next = map[curr.next]
            map[curr].random = map[curr.random]
            curr = curr.next
        
        return map[head]