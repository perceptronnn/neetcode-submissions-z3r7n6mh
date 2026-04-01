# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.valid = True
        def dfs(node, left, right):
            if not node or not self.valid:
                return
            if node.val <= left or node.val >= right:
                self.valid = False
                return
            dfs(node.left, left, node.val)
            dfs(node.right, node.val, right)
        dfs(root, -1001, 1001)
        return self.valid
        