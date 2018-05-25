### 题意
Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.  
给定一个二叉树和一个目标和，判断该树中是否存在根节点到叶子节点的路径，这条路径上所有节点值相加等于目标和。

Note: A leaf is a node with no children.  
说明: 叶子节点是指没有子节点的节点。

Example:
```
Given the below binary tree and sum = 22,

         5
        / \
       4   8
      /   / \
     11  13  4
    /  \      \
   7    2      1

return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.
返回 true, 因为存在目标和为 22 的根节点到叶子节点的路径 5->4->11->2。
```

### 思路
递归实现。如果根节点为空则返回 False ；如果左右子节点均为空，则返回节点值是否等于 sum；否则递归判断其左右子树，新 sum 为 sum 减去节点的值。
```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return False
        if not root.left and not root.right and root.val == sum:
            return True
        sum -= root.val
        return self.hasPathSum(root.left, sum) or self.hasPathSum(root.right, sum)
```
[LeetCode 112. Path Sum](https://leetcode.com/problems/path-sum/description/)
