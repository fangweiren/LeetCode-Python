### 题意
Given an array of integers, return indices of the two numbers such that they add up to a specific target.  
给定一个整数数组和一个目标值，找出数组中和为目标值的两个数。

You may assume that each input would have exactly one solution, and you may not use the same element twice.  
你可以假设每个输入只对应一种答案，且同样的元素不能被重复利用。

Example:
```python
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
```
### 思路一
暴力破解，两重循环，效率很低，不推荐。。。
```python
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        len_nums = len(nums)
        for i in range(len_nums):
            for j in range(i+1, len_nums):
                if nums[i] + nums[j] == target:
                    return [i,j]
```
### 思路二
遍历数组，用字典记录 {值: 索引}，并判断另一个数是否在字典中。
```python
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        num_dict = {}
        for i in range(len(nums)):
            another = target - nums[i]
            if another in num_dict:
                return [num_dict[another], i]
            else:
                num_dict[nums[i]] = i
```
[LeetCode 1. Two Sum](https://leetcode.com/problems/two-sum/description/)
