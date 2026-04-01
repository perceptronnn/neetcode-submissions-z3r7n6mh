# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        prev = head
        curr = head.next
        first = True
        while curr:
            temp = curr.next
            curr.next = prev
            if first:
                prev.next = None
                first = False
            prev = curr
            curr = temp

        print("kippi")
        p = prev
        while p:
            print(p.val)
            p = p.next
        return prev
        