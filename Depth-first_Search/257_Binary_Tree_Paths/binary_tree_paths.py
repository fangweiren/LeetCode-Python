# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        res, path_list = [], []
        self.dfs(root, res, path_list)
        return res
    
    def dfs(self, root, res, path_list):
        if not root:
            return
        path_list.append(str(root.val))
        if not root.left and not root.right:
            res.append('->'.join(path_list))
        if root.left:
            self.dfs(root.left, res, path_list)
        if root.right:
            self.dfs(root.right, res, path_list)
        path_list.pop()
