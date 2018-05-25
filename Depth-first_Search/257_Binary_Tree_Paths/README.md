### 题意
Given a binary tree, return all root-to-leaf paths.  
给定一个二叉树，返回所有从根节点到叶子节点的路径。

Note: A leaf is a node with no children.  
说明: 叶子节点是指没有子节点的节点。

Example:
```
Input:

   1
 /   \
2     3
 \
  5

Output: ["1->2->5", "1->3"]

Explanation: All root-to-leaf paths are: 1->2->5, 1->3
```

### 思路
递归实现深度优先遍历。

```python
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
```
[LeetCode 257. Binary Tree Paths](https://leetcode.com/problems/binary-tree-paths/description/)
