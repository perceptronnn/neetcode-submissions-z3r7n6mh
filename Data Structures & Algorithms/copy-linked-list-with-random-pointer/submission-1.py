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
        nodes = []
        randomMap = {}
        curr = head
        idx = 0
        while curr:
            nodes.append(curr)
            randomMap[curr] = idx
            idx += 1
            curr = curr.next
        copiedNodes = []
        for i in range(len(nodes)):
            n = Node(nodes[i].val)
            copiedNodes.append(n)
        #print(randomMap)
        for i in range(len(nodes)):
            if i + 1 < len(nodes):
                copiedNodes[i].next = copiedNodes[i+1]
            if nodes[i].random:
                copiedNodes[i].random = copiedNodes[randomMap[nodes[i].random]]
        return copiedNodes[0]
            
        