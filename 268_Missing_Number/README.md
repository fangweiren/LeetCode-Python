题意  
Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.  
给定一个包含 0, 1, 2, ..., n 中 n 个不同数字的数组，找出数组中缺少的那个数字。

Example 1
```
Input: [3,0,1]  
Output: 2  
```
Example 2
```
Input: [9,6,4,2,3,5,7,0,1]  
Output: 8
```
Note:  
Your algorithm should run in linear runtime complexity. Could you implement it using only constant extra space complexity?  
您的算法应该以线性运行时复杂度运行。 你能否仅使用恒定的额外空间复杂度来实现它？

思路  
用等差数列求和公式求出和，那么减去给定数组的和，得到的结果就是缺失的数字。
![等差数列求和公式](https://github.com/fangweiren/LeetCode-Python/blob/master/screenshots/dengchashulieqiuhe.png)
等差数列和 = (首项0 + 末项n) * 项数(n+1) / 2 

```
class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return len(nums) * (len(nums) + 1) / 2 - sum(nums)
```

[LeetCode 268. Missing Number](https://leetcode.com/problems/missing-number/description/)
