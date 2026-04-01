# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.nodeMap = []
        def levelOrderHelper(node, idx):
            if not node:
                return
            if len(self.nodeMap) < idx + 1:
                self.nodeMap.append([])
            self.nodeMap[idx].append(node.val)
            levelOrderHelper(node.left, idx + 1)
            levelOrderHelper(node.right, idx + 1)
            return
        
        levelOrderHelper(root, 0)
        return self.nodeMap
        