# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from math import gcd
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        while cur.next:
            newNode = ListNode(gcd(cur.val, cur.next.val), cur.next)
            cur.next = newNode
            cur = newNode.next
        return head
