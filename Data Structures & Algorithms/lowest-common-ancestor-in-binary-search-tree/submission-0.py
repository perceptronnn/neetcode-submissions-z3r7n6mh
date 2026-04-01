# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root:
            return None
        if root.val == p.val or root.val == q.val:
            return root
        s, l = min(p.val, q.val), max(p.val, q.val)
        if root.val > s and root.val < l:
            return root
        if root.val > l:
            return self.lowestCommonAncestor(root.left, p, q)
        if root.val < s:
            return self.lowestCommonAncestor(root.right, p, q)
        