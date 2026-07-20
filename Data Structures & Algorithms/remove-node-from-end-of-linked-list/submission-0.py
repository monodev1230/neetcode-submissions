# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return head
        c = head
        count = 0
        while c:
            c = c.next
            count += 1

        print(count)
        if n > count:
            return []
        idx = count - n - 1
        if idx == -1:
            head = head.next

        cnt = 0
        ptr = head
        while ptr:
            if cnt == idx:
                ptr.next = ptr.next.next
            ptr = ptr.next
            cnt += 1

        return head