# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return None
        s, f = head, head.next
        # find mid
        while f and f.next:
            s = s.next
            f = f.next.next
        mid = s.next
        s.next = None
        # reverse mid
        p, c = None, mid
        while c:
            t = c.next
            c.next = p
            p = c
            c = t
        # merge p and head
        first, second = head, p
        while second:
            t1, t2 = first.next, second.next
            first.next = second
            second.next = t1
            second = t2
            first = t1
