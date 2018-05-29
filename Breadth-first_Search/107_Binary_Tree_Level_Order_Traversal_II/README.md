### 题意
Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).  
给定一个二叉树，返回其节点值自底向上的层次遍历。 （即按从叶子节点所在层到根节点所在的层，逐层从左向右遍历）

For example:  
Given binary tree [3,9,20,null,null,15,7],
```python
    3
   / \
  9  20
    /  \
   15   7
```
return its bottom-up level order traversal as:  
返回其自底向上的层次遍历为：
```python
[
  [15,7],
  [9,20],
  [3]
]
```

### 思路
将树每一层的节点存在一个列表中，遍历列表中的元素，如果该节点有左右节点的话，就把它们加入一个临时列表，这样当遍历结束时，下一层的节点也按照顺序存储好了，不断循环直到下一层的列表为空。最后将列表翻转就可以了。
```python
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
```
[LeetCode 107. Binary Tree Level Order Traversal II](https://leetcode.com/problems/binary-tree-level-order-traversal-ii/description/)
