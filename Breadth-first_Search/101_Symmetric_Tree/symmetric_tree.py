# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sym(self, p , q):
        if p == None and q == None:
            return True
        if p and q and p.val == q.val:
            return self.sym(p.left, q.right) and self.sym(p.right, q.left)
        return False

    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root:
            return self.sym(root.left, root.right)
        return True
