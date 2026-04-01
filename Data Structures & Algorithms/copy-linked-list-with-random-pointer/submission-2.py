"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        oldNewMap = {}
        curr = head
        while curr:
            n = Node(curr.val)
            oldNewMap[curr] = n
            curr = curr.next
        curr = head
        while curr:
            if curr.next:
                oldNewMap[curr].next = oldNewMap[curr.next]
            if curr.random:
                oldNewMap[curr].random = oldNewMap[curr.random]
            curr = curr.next
        return oldNewMap[head]

        