# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        tree = []
        if not root:
            return tree
        curr_level = [root]
        while curr_level:
            level_list = []
            next_level = []
            for temp in curr_level:
                level_list.append(temp.val)
                if temp.left:
                    next_level.append(temp.left)
                if temp.right:
                    next_level.append(temp.right)
            tree.append(level_list)
            curr_level = next_level
        return tree[::-1]
