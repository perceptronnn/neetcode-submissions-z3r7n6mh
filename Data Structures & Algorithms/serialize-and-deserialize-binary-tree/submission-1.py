# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        nodes = []
        def dfs(node, nodes):
            if not node:
                nodes.append("N")
                return
            nodes.append(str(node.val))
            dfs(node.left, nodes)
            dfs(node.right, nodes)
            return
        dfs(root, nodes)

        nds = (',').join(nodes)
        print(nds)
        return nds
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        nodeVals = data.split(',')
        self.i = 0

        def dfs():
            if nodeVals[self.i] == "N":
                self.i += 1
                return None
            node = TreeNode(int(nodeVals[self.i]))
            self.i += 1
            node.left = dfs()
            node.right = dfs()
            return node
        print(nodeVals)
        return dfs()
        
