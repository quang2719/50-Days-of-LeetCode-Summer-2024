# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        res = []
        def cut_leaf(root):
            nonlocal to_delete
            if not root: return None
            if root.val in to_delete:
                new_root_left = cut_leaf(root.left)
                new_root_right = cut_leaf(root.right)
                if new_root_left: res.append(new_root_left)
                if new_root_right: res.append(new_root_right)
                return None
            else:
                root.left = cut_leaf(root.left)
                root.right = cut_leaf(root.right)
            return root
        
        if root.val not in to_delete:
            res.append(root)

        cut_leaf(root)
        return res



