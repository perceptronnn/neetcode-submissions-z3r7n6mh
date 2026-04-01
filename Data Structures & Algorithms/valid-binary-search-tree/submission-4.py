# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        q = collections.deque()
        q.append([root, -1001, 1001])
        while q:
            qLen = len(q)
            item = q.popleft()
            node, l, r = item[0], item[1], item[2]
            if node:
                if node.val <= l or node.val>= r:
                    return False
                q.append([node.left, l, node.val])
                q.append([node.right, node.val, r])
        return True
            
        