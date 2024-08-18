# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        def is_leaf(node):
            return True if (not node.left and not node.right) else False
        leaf_list = []
        parent = {}
        def treval(root):
            nonlocal leaf_list
            nonlocal parent
            if is_leaf(root):
                leaf_list.append(root)
                return
            if root.left:
                parent[root.left] = root
                treval(root.left)
            if root.right:
                parent[root.right] = root
                treval(root.right)
        treval(root)
        count = 0
        
        for leaf in leaf_list:
            stack = []
            visited = {}
            stack.append([leaf,distance])
            visited[leaf] = True
            while stack:
                cur_leaf,dis = stack.pop()
                visited[cur_leaf] = True
                if is_leaf(cur_leaf) and 0 <= dis < distance:
                    count+=1
                    continue
                #distance = 0 is accepted but it can't call the subnode anymore
                if dis <= 0: continue 
                if cur_leaf.left and cur_leaf.left not in visited:
                    stack.append([cur_leaf.left,dis-1])
                if cur_leaf.right and cur_leaf.right not in visited:
                    stack.append([cur_leaf.right,dis-1])
                par =  parent.get(cur_leaf,None)
                if par and par not in visited:
                    stack.append([parent[cur_leaf],dis-1])
        return count//2
                


