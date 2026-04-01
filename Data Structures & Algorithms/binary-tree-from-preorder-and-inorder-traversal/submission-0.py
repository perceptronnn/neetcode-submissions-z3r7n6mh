# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def buildTreeHelper(pS, pE, iS, iE):
            if pS > pE:
                return None
            if pS == pE:
                return TreeNode(preorder[pS])
            if pS > pE or iS > iE:
                return None
            root = TreeNode(preorder[pS])
            leftCount = 0
            idx = iS
            while idx <= iE and inorder[idx] != preorder[pS]:
                leftCount += 1
                idx += 1
            if idx == len(inorder) and inorder[idx - 1] != preorder[pS]:
                return None
            root.left = buildTreeHelper(pS+1, pS + leftCount, iS,idx - 1)
            root.right = buildTreeHelper(pS + leftCount + 1, pE, idx + 1, iE)
            return root
        return buildTreeHelper(0, len(preorder) - 1, 0, len(inorder) - 1)
        