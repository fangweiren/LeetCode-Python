题意：  
Given an array of integers and an integer k, find out whether there are two distinct indices i and j in the array such that nums[i] = nums[j] and the absolute difference between i and j is at most k.  
给定一个数组，和一个整数 k，判断该数组中是否存在不同的索引 i 和 j，使得 nums[i] = nums[j]，且 i 和 j 的差不超过 k。

```
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        d1 = {}
        for i, v in enumerate(nums):
            if v in d1 and i - d1[v] <= k:
                return True
            d1[v] = i
        return False
```

[219. Contains Duplicate II](https://leetcode.com/problems/contains-duplicate-ii/description/)
