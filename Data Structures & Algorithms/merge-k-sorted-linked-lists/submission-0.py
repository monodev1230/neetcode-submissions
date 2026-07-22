# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        res = ListNode()
        tail = res
        while True:
            minPtr = (float('inf'), -1)
            for i in range(len(lists)):
                if lists[i]:
                    if minPtr[0] > lists[i].val:
                        minPtr = (lists[i].val, i)

            if minPtr[1] == -1:
                break
            tail.next = lists[minPtr[1]]
            lists[minPtr[1]] = lists[minPtr[1]].next
            tail = tail.next
        return res.next