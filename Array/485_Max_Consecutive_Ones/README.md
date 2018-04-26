### 题意
Given a binary array, find the maximum number of consecutive 1s in this array.  
给定一个二进制数组， 计算其中最大连续1的个数。

Example 1:
```python
Input: [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s.
    The maximum number of consecutive 1s is 3.
解释: 开头的两位和最后的三位都是连续1，所以最大连续1的个数是 3.
```
Note:

The input array will only contain 0 and 1.  
The length of input array is a positive integer and will not exceed 10,000。  
输入数组的长度是正整数，且不超过 10,000。
### 思路
遍历+计数器
```python
class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = maxCount = 0
        for num in nums:
            if num == 1:
                count += 1
                maxCount = max(count, maxCount)
            else:
                count = 0
        return maxCount
```
[LeetCode 485. Max Consecutive Ones](https://leetcode.com/problems/max-consecutive-ones/description/)
