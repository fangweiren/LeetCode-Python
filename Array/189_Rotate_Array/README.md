### 题意
Given an array, rotate the array to the right by k steps, where k is non-negative.  
给定一个数组，将数组中的元素向右移动 k 个位置，其中 k 是非负数。

Example 1:
```python
Input: [1,2,3,4,5,6,7] and k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
向右旋转 1 步
rotate 2 steps to the right: [6,7,1,2,3,4,5]
向右旋转 2 步
rotate 3 steps to the right: [5,6,7,1,2,3,4]
向右旋转 3 步
```
Example 2:
```python
Input: [-1,-100,3,99] and k = 2
Output: [3,99,-1,-100]
Explanation: 
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]
```
Note:  
Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.  
尽可能想出更多的解决方案，至少有三种不同的方法可以解决这个问题。

Could you do it in-place with O(1) extra space?  
要求使用空间复杂度为 O(1) 的原地算法。
### 思路
利用 Python 的数组 slice 的操作和赋值，实际上相当于创建了两个新的数组，分别保存原数组的前后部分，再依次将元素赋值给原数组。【时间复杂度O(n)，空间复杂度O(n)】
```python
class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        nums[:] = nums[n - k:] + nums[:n - k]
```
[LeetCode 189. Rotate Array](https://leetcode.com/problems/rotate-array/description/)
