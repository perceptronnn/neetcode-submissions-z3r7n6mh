# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:        
        if self.isSameTree(root, subRoot):
            return True
        elif root:
            l = self.isSubtree(root.left, subRoot)
            r = self.isSubtree(root.right, subRoot)
            return l or r
        else:
            return False

    def isSameTree(self, node, subRoot):
        if not node and not subRoot:
            return True
        if (not node and subRoot) or (node and not subRoot) or (node.val != subRoot.val):
            return False
        return self.isSameTree(node.left, subRoot.left) and self.isSameTree(node.right, subRoot.right)        