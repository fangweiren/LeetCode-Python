### 题意
Given two binary trees, write a function to check if they are the same or not.  
给定两个二叉树，编写一个函数来检验它们是否相同。

Two binary trees are considered the same if they are structurally identical and the nodes have the same value.  
如果两个树在结构上相同，并且节点具有相同的值，则认为它们是相同的。

Example 1:
```
Input:     1         1
          / \       / \
         2   3     2   3

        [1,2,3],   [1,2,3]

Output: true
```
Example 2:
```
Input:     1         1
          /           \
         2             2

        [1,2],     [1,null,2]

Output: false
```
Example 3:
```
Input:     1         1
          / \       / \
         2   1     1   2

        [1,2,1],   [1,1,2]

Output: false
```

### 思路
本题考察树的比较和遍历。本质上是遍历这两棵树，可以采用任何一种遍历方式，当找到两棵树的不同时返回 False。  
递归思想，首先判断两个根节点的值是否相同，如果相同，递归判断根的左右子树。
```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if q == None and p == None:
            return True
        if q and p and p.val == q.val:
           return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        return False
```
[LeetCode 100. Same Tree](https://leetcode.com/problems/same-tree/description/)
