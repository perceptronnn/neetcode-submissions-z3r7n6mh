# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ans = self.maxPathSumInternal(root)
        return ans[0]

    def maxPathSumInternal(self, node) -> (int, int):
        if not node:
            return (-10000, -10000)
        if not node.left and not node.right:
            return (node.val, node.val)
        l = self.maxPathSumInternal(node.left)
        r = self.maxPathSumInternal(node.right)
        return (max(l[0], r[0], node.val + max(l[1], 0) + max(r[1], 0)), max(l[1] + node.val, r[1] + node.val, node.val))

        
        