# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        dic = {}
        child_val_list = []
        for des in descriptions:
            par,chi,left = des 
            child_val_list.append(chi)  

            parent = dic.setdefault(par,TreeNode(par))
            child = dic.setdefault(chi,TreeNode(chi))
            if left:
                parent.left = child
            else:
                parent.right = child
        return dic[[x for x in dic if x not in child_val_list][0]]
            

        