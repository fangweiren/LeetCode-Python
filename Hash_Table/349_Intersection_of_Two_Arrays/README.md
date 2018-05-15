### 题意
Given two arrays, write a function to compute their intersection.  
给定两个数组，写一个函数来计算它们的交集。

Example:
```
Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2].
```
Note:  
- Each element in the result must be unique.
- 每个在结果中的元素必定是唯一的。
- The result can be in any order.
- 我们可以不考虑输出结果的顺序。

### 思路一
利用 set 函数求交集。
```python
class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        return list(set(nums1) & set(nums2))
```
### 思路二
遍历 nums1 的每个元素，在 nums2 中查找该元素是否出现，若出现且 result 中没有，则加入到结果集中。
```python
class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        result = []
        for num in nums1:
            if num in nums2 and num not in result:
                result.append(num)
        return result
```
### 思路三
用字典 result 统计 nums1 中出现了哪些数，然后遍历 nums2，如果出现在 result 中则把该数加入到 结果列表 res 中，同时字典中删除该数。
```python
class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        result = {}
        res = []
        for num in nums1:
            if num not in result:
                result[num] = 1
        for num in nums2:
            if num in result:
                res.append(num)
                result.pop(num)
        return res
```
[LeetCode 349. Intersection of Two Arrays](https://leetcode.com/problems/intersection-of-two-arrays/description/)
