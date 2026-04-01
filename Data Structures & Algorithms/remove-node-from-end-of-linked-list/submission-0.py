# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        l = self.getLength(head)
        target = l - n
        dummy = ListNode(0, head)
        curr = dummy
        count = 0
        while curr and count != target:
            count += 1
            curr = curr.next
        if curr and curr.next:
            curr.next = curr.next.next 
        return dummy.next
        
    def getLength(self, head):
        l = 0
        while head:
            l += 1
            head = head.next
        return l