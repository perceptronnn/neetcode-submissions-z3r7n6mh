# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1
        l1 = list1
        l2 = list2
        m, c = None, None
        while l1 and l2:
            if c:
                c.next = ListNode(min(l1.val, l2.val), None)
                c = c.next
                #print(n.val)
            else:
                print("yo")
                #print(n.val)
                c = ListNode(min(l1.val, l2.val), None)
                m = c
            if l1.val < l2.val:
                l1 = l1.next
            else:
                l2 = l2.next
            #c = c.next
        if l1:
            c.next = l1
        if l2:
            c.next = l2
        return m
