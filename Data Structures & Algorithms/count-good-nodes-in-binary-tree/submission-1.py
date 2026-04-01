# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def goodNodesHelper(node, maxSofar):
            if not node:
                return 0
            res = 0
            if node.val >= maxSofar:
                res = 1
                maxSofar = node.val
            res += goodNodesHelper(node.left, maxSofar)
            res += goodNodesHelper(node.right, maxSofar)
            return res
            
        return goodNodesHelper(root, -101)
        