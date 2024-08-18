
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        def lca(node):
            if not node or node.val in (startValue, destValue):
                return node
            left, right = lca(node.left), lca(node.right)
            return node if left and right else left or right
        
        root = lca(root)
        
        start_path, dest_path = "", ""
        stack = [(root, "")]
        while stack:
            node, path = stack.pop()
            if node.val == startValue:
                start_path = path
            if node.val == destValue:
                dest_path = path
            if node.left:
                stack.append((node.left, path + "L"))
            if node.right:
                stack.append((node.right, path + "R"))
        return "U" * len(start_path) + dest_path