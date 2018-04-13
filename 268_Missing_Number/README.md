题意  
Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.

Example 1

Input: [3,0,1]  
Output: 2  
Example 2

Input: [9,6,4,2,3,5,7,0,1]  
Output: 8

Note:  
Your algorithm should run in linear runtime complexity. Could you implement it using only constant extra space complexity?

思路  
用等差数列求和公式求出和，那么减去给定数组的和，得到的结果就是缺失的数字。

```
class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return len(nums) * (len(nums) + 1) / 2 - sum(nums)
```
