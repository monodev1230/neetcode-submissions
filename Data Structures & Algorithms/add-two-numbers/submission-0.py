# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1:
            return l2
        if not l2:
            return l1
        carryOver = 0
        curr1, curr2 = l1, l2
        dummy = ListNode(0)
        tail = dummy
        while curr1 or curr2:
            curr1Val = curr1.val if curr1 else 0
            curr2Val = curr2.val if curr2 else 0 
            tempSum = curr1Val + curr2Val + carryOver
            if tempSum > 9:
                carryOver = 1
                tempSum = tempSum%10
            else:
                carryOver = 0
            tail.next = ListNode(tempSum)
            tail = tail.next
            curr1 = curr1.next if curr1 else None
            curr2 = curr2.next if curr2 else None
        if carryOver:
            tail.next = ListNode(carryOver)
        return dummy.next
                
            