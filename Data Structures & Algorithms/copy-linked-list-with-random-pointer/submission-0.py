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
        nodes = {}
        curr = head
        while curr:
            nodes[curr] = Node(curr.val)
            curr = curr.next
        curr = head
        res = None
        prev = None
        while curr:
            if not res:
                res = nodes[curr]
            if prev:
                nodes[prev].next = nodes[curr]
            if curr.random:
                nodes[curr].random = nodes[curr.random]
            prev = curr
            curr = curr.next
        return res