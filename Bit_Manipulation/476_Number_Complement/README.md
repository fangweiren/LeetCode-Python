### 题意
Given a positive integer, output its complement number. The complement strategy is to flip the bits of its binary representation.  
给定一个正整数，输出它的补数。补数是对该数的二进制表示取反。

Note:

- The given integer is guaranteed to fit within the range of a 32-bit signed integer.
- 给定的整数保证在32位带符号整数的范围内。
- You could assume no leading zero bit in the integer’s binary representation.
- 你可以假定二进制数不包含前导零位。

Example 1:
```
Input: 5
Output: 2
Explanation: The binary representation of 5 is 101 (no leading zero bits), and its complement is 010. So you need to output 2.
解释: 5 的二进制表示为 101（没有前导零位），其补数为 010。所以你需要输出 2。
```
Example 2:
```
Input: 1
Output: 0
Explanation: The binary representation of 1 is 1 (no leading zero bits), and its complement is 0. So you need to output 0.
```

### 思路
位运算。
```python
class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        i = 1
        while i <= num:
            i = i << 1
        return (i-1) ^ num
```
[LeetCode 476. Number Complement](https://leetcode.com/problems/number-complement/description/)
