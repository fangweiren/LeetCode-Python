### 题意
Given a binary tree, find its maximum depth.  
给定一个二叉树，找出其最大深度。

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.  
二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。

Note: A leaf is a node with no children.  
说明: 叶子节点是指没有子节点的节点。

Example:
```
Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its depth = 3.
```

### 思路
深度优先搜索 (DFS)，递归求解。
```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
```
[LeetCode 104. Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/description/)
