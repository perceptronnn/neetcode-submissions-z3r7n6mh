# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.gNodes = 0

        def goodNodesHelper(node, maxSofar):
            if not node:
                return
            
            if node.val >= maxSofar:
                self.gNodes += 1
                maxSofar = node.val
            goodNodesHelper(node.left, maxSofar)
            goodNodesHelper(node.right, maxSofar)
            
        goodNodesHelper(root, -101)
        return self.gNodes
        