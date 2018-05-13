### 题意
Given a non-empty array of integers, every element appears twice except for one. Find that single one.  
给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。

Note:  
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?  
你的算法应该具有线性时间复杂度。你可以不使用额外空间来实现吗？(时间复杂度 O(n)，空间复杂度 O(1))

Example 1:
```
Input: [2,2,1]
Output: 1
```
Example 2:
```
Input: [4,1,2,1,2]
Output: 4
```
### 思路
如果题目没有限制条件很容易想到利用 dict 来实现。然而要求 O(n) 的时间复杂度和 O(1) 的空间复杂度，可以利用“异或”操作实现。

异或操作：  
一个整数与自己异或的结果是 0(2^2=0)  
一个整数与 0 异或的结果是自己(2^0=2)  
异或操作满足交换律，即 a^b = b^a  
所以对所有数字进行异或操作后剩下的就是那个只出现一次的数字。
```python
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = nums[0]
        for num in nums[1:]:
            res ^= num
        return res
```
[LeetCode 136. Single Number](https://leetcode.com/problems/single-number/description/)
