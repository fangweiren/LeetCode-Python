### 题意
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.  
给定两个有序整数数组 nums1 和 nums2，将 nums2 合并到 nums1 中，使得 num1 成为一个有序数组。

Note:  
The number of elements initialized in nums1 and nums2 are m and n respectively.  
初始化 nums1 和 nums2 的元素数量分别为 m 和 n。

You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2.  
你可以假设 nums1 有足够的空间（空间大小大于或等于 m + n）来保存 nums2 中的元素。

Example:
```python
Input:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3

Output: [1,2,2,3,5,6]
```
### 思路
数组 nums1 从 m 个元素往前比较，数组 nums2 从后往前比较。当两者都没到头时，根据大小从 m+n-1 处往前更新数组 nums1。循环结束，如果数组 nums2 没有到头，将数组 nums2 中剩余元素同位置赋给数组 nums1 即可。
```python
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        while m > 0 and n > 0:
            if nums1[m - 1] > nums2[n - 1]:
                nums1[m + n - 1] = nums1[m - 1]
                m = m -1
            else:
                nums1[m + n - 1] = nums2[n - 1]
                n = n - 1
        if n > 0:
            nums1[:n] = nums2[:n]
```
[LeetCode 88. Merge Sorted Array](https://leetcode.com/problems/merge-sorted-array/description/)
