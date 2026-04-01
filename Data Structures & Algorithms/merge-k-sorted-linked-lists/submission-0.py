# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import heapq

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """
        setup heap: first element of each list (element, list_id)
        while heap is not empty:
            pop top element/tuple: add t[0] to answr
            if t1 is not empty:
                add next element from t[1]

        """
        h = []
        self.printList(lists)
        for idx in range(len(lists)):
            if lists[idx]:
                h.append((self.getFirstElement(lists[idx]), idx))
                lists[idx] = lists[idx].next
        self.printList(lists)
        heapq.heapify(h)
        dummy = ListNode()
        curr = dummy
        while len(h) > 0:
            print(h)
            top = heapq.heappop(h)
            curr.next = ListNode(top[0])
            curr = curr.next
            if lists[top[1]]:
                heapq.heappush(h, (self.getFirstElement(lists[top[1]]), top[1]))
                lists[top[1]] = lists[top[1]].next
        return dummy.next


    def getFirstElement(self,l):
        v = -1
        if l:
            v = l.val
            l = l.next
        return v
    
    def printList(self, l):
        for ll in l:
            self.pll(ll)
        return
    
    def pll(self, ll):
        p = ""
        while ll:
            p += str(ll.val)
            p += "->"
            ll = ll.next
        print(p)
        return




        