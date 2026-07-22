# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        prev, fast = dummy, head
        isShort = False
        while True:
            for _ in range(k):
                if fast:
                    fast = fast.next
                else:
                    isShort = True
            # fast 4, prev None, isShort False, tail None
            if not isShort:
                self.reverseKnodes(prev, fast, head, k)
                prev = head
                head = prev.next
            else:
                break
        return dummy.next
        
    def reverseKnodes(self, prevHead, tail, head, k):
        prev, curr = tail, head
        for _ in range(k):
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        prevHead.next = prev
        return prev