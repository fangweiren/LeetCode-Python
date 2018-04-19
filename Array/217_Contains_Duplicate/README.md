题意：  
Given an array of integers, find if the array contains any duplicates. Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.  
给定一个整数数组，查找数组是否包含任何重复项。 如果任何值在数组中至少出现两次，则函数应该返回true，并且如果每个元素都不相同，则它应该返回false。  

```
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return len(nums) != len(set(nums))
```

[LeetCode 217. Contains Duplicate](https://leetcode.com/problems/contains-duplicate/description/)
