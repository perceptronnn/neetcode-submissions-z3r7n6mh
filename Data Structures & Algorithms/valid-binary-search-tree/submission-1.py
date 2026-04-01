# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        res = []
        resSet = set()
        def inOrder(node):
            if not node:
                return
            inOrder(node.left)
            res.append(node.val)
            resSet.add(node.val)
            inOrder(node.right)
        inOrder(root)
        print(res)
        print(sorted(res))
        return res == sorted(res) and len(res) == len(resSet)