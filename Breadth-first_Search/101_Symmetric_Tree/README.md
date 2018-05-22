### 题意
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).  
给定一个二叉树，检查它是否是镜像对称的。

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:  
例如，二叉树 [1,2,2,3,4,4,3] 是对称的。
```
    1
   / \
  2   2
 / \ / \
3  4 4  3
```
But the following [1,2,2,null,3,null,3] is not:  
但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:
```
    1
   / \
  2   2
   \   \
   3    3
```
Note:  
Bonus points if you could solve it both recursively and iteratively.  
如果你可以运用递归和迭代两种方法解决这个问题，会很加分。

### 思路
需要用一个辅助函数，当然也是递归的。当存在左右子树时，判断左右子树的根节点值是否相等，如果相等继续递归判断左子树根的右子树根节点和右子树根的左子树根节点以及左子树根的左子树根节点和右子树根的右子树根节点的值是否相等。然后一直递归判断下去就可以了。

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root:
            return self.mirror(root.left, root.right)
        return True
    
    def mirror(self, p, q):
        if p == None and q == None:
            return True
        if p and q and p.val == q.val:
            return self.mirror(p.left, q.right) and self.mirror(p.right, q.left)
        return False
```
[LeetCode 101. Symmetric Tree](https://leetcode.com/problems/symmetric-tree/description/)
