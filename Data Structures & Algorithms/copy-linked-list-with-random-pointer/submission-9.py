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
        newNode = defaultdict(lambda : Node(0))
        newNode[None] = None
        cur = head
        while cur:
            newNode[cur].val = cur.val
            newNode[cur].next = newNode[cur.next]
            newNode[cur].random = newNode[cur.random]
            cur = cur.next
        
        return newNode[head]