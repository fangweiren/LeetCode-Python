### 题意
Given an array where elements are sorted in ascending order, convert it to a height balanced BST.  
将一个按照升序排列的有序数组，转换为一棵高度平衡二叉搜索树。

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.  
本题中，一个高度平衡二叉树是指一个二叉树每个节点的左右两个子树的高度差的绝对值不超过 1。

Example:
```
Given the sorted array: [-10,-3,0,5,9],

One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:
一个可能的答案是：[0,-3,9,-10,null,5]，它可以表示下面这个高度平衡二叉搜索树：

      0
     / \
   -3   9
   /   /
 -10  5
```

### 思路
由于要求二叉查找树是平衡的。所以可以选在数组的中间那个数当树根root，然后这个数左边的数组为左子树，右边的数组为右子树，分别递归产生左右子树就可以了。
```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        length = len(nums)
        if length == 0:
            return None
        if length == 1:
            return TreeNode(nums[0])
        root = TreeNode(nums[length / 2])
        root.left = self.sortedArrayToBST(nums[:length / 2])
        root.right = self.sortedArrayToBST(nums[length / 2 + 1:])
        return root
```
[LeetCode 108. Convert Sorted Array to Binary Search Tree](https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/description/)
