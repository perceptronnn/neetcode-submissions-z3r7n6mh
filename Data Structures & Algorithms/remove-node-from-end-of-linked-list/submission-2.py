# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        l = dummy
        r = head
        count = 0
        while r and count != n:
            r = r.next
            count += 1
        while r:
            l = l.next
            r = r.next
        l.next = l.next.next
        return dummy.next
        