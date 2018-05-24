### 题意
Given a binary tree, determine if it is height-balanced.  
给定一个二叉树，判断它是否是高度平衡的二叉树。

For this problem, a height-balanced binary tree is defined as:  
本题中，一棵高度平衡二叉树定义为：

a binary tree in which the depth of the two subtrees of every node never differ by more than 1.  
一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过1。

Example 1:
```
Given the following tree [3,9,20,null,null,15,7]:
给定二叉树 [3,9,20,null,null,15,7]

    3
   / \
  9  20
    /  \
   15   7
返回 true 。
```

Example 2:
```
Given the following tree [1,2,2,3,3,null,null,4,4]:

       1
      / \
     2   2
    / \
   3   3
  / \
 4   4
Return false.
```

### 思路
本题中，平衡二叉树的定义是二叉树的任意节点的两颗子树之间的高度差小于等于 1 。首先要写一个计算二叉树高度的函数，二叉树的高度定义为：树为空时，高度为0。然后递归求解：树的高度 = max(左子树高度，右子树高度) + 1(根节点要算上)。高度计算函数实现后，递归求解每个节点的左右子树的高度差，如果有大于 1 的，则 return False。如果高度差小于等于 1，则继续递归求解。
```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def height(self, root):
        if not root:
            return 0
        return max(self.height(root.left), self.height(root.right)) + 1

    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        if abs(self.height(root.left) - self.height(root.right)) <= 1:
            return self.isBalanced(root.left) and self.isBalanced(root.right)
        else:
            return False
```
[LeetCode 110. Balanced Binary Tree](https://leetcode.com/problems/balanced-binary-tree/description/)
