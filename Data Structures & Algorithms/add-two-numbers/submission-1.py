# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode(0)
        prev = res
        carry = 0
        while l1 and l2:
            total = l1.val + l2.val + carry
            carry = total // 10
            curr = ListNode(total % 10)
            prev.next = curr
            prev = curr
            l1 = l1.next
            l2 = l2.next
        if l1:
            prev.next = l1
        if l2:
            prev.next = l2
        
        while carry:
            print(carry, prev.val, prev.next)
            print()
            print()
            if prev.next:
                total = prev.next.val + carry
                carry = total // 10
                prev.next.val = total % 10
                prev = prev.next
            else:
                prev.next = ListNode(carry)
                carry = 0
        return res.next

        