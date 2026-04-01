# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        a, b, c = self.diameterHelper(root)
        return c

    def diameterHelper(self, node):
        if not node:
            return -1, -1, 0
        
        ll, lr, lm = self.diameterHelper(node.left)
        rl, rr, rm = self.diameterHelper(node.right)

        l = max(ll, lr) + 1
        r = max(rl, rr) + 1
        m = max(l + r, lm, rm)
        return l, r, m  