# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right:
            return head
        prev, leftNode = None, head
        count = 0
        while leftNode:
            count += 1
            if count == left:
                break
            prev = leftNode
            leftNode = leftNode.next
        lHead = prev
        tail = prev
        curr = leftNode
        while curr and count <= right:
            temp = curr.next
            curr.next = tail
            tail = curr
            curr = temp
            count += 1
        print('tail', tail.val, 'lHead', lHead.val if lHead else -1)
        leftNode.next = curr
        if lHead:
            lHead.next = tail
        
        return head if lHead else tail
        