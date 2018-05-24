### 题意
Given a binary tree, find its minimum depth.  
给定一个二叉树，找出其最小深度。

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.  
最小深度是从根节点到最近叶子节点的最短路径上的节点数量。

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

return its minimum depth = 2.
```

### 思路
分几种情况考虑：  
1.树为空，则为0。  
2.根节点如果只存在左子树或者只存在右子树，则返回值应为左子树或者右子树的 (最小深度+1) 。  
3.如果根节点的左子树和右子树都存在，则返回值为 (左右子树的最小深度的较小值 +1 ) 。
```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        if not root.left or not root.right:
            return self.minDepth(root.left) + self.minDepth(root.right) + 1
        return min(self.minDepth(root.left), self.minDepth(root.right)) + 1
```
[LeetCode 111. Minimum Depth of Binary Tree](https://leetcode.com/problems/minimum-depth-of-binary-tree/description/)
