# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next or not head.next.next:
            return 
        # find the middle
        slow, fast = head, head.next
        while fast and fast.next:
            #print("hi")
            slow = slow.next
            fast = fast.next.next
        curr = slow.next
        slow.next = None
        print('first half')
        self.printList(head)
        print('second half')
        self.printList(slow)
        
        # reverse the slow from the middle
        prev = None
        #curr = slow
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        self.printList(prev)

        
        # megre the lists
        l1 = head
        l2 = prev
        print("l1")
        self.printList(l1)
        print("l2")
        self.printList(l2)
        
        while l1 and l2:
            tmp1 = l1.next
            tmp2 = l2.next
            l1.next = l2
            l2.next = tmp1
            l1 = tmp1
            l2 = tmp2
        
        return

    def printList(self, head):
        l = []
        while head:
            l.append(head.val)
            head = head.next
        print(l)
        return
        