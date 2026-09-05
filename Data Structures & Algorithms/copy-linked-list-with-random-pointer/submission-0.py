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
        old_to_copy = {}

        def rec(original_node):
            if not original_node:
                return None

            node_copy = Node(original_node.val)
            old_to_copy[original_node] = node_copy
            node_copy.next = rec(original_node.next)
            return node_copy

        new_head = rec(head)
        curr = head

        while curr:
            if curr.random:
                old_to_copy[curr].random = old_to_copy[curr.random]
            curr = curr.next

        return new_head