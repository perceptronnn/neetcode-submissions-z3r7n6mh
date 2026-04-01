# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0
        q = collections.deque()
        q.append([root, -101])
        while q:
            qLen = len(q)
            for i in range(qLen):
                item = q.popleft()
                node = item[0]
                maxSoFar = item[1]
                if node:
                    if node.val >= maxSoFar:
                        res += 1
                        maxSoFar = node.val
                    q.append([node.left, maxSoFar])
                    q.append([node.right, maxSoFar])
        return res
                
                
            
        