### 题意
Given a 32-bit signed integer, reverse digits of an integer.  
给定一个 32 位有符号整数，将整数中的数字进行反转。

Example 1:
```
Input: 123
Output: 321
```
Example 2:
```
Input: -123
Output: -321
```
Example 3:
```
Input: 120
Output: 21
```
Note:

Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−2^31,  2^31 − 1].  
假设我们的环境只能存储 32 位有符号整数，其数值范围是 [−2^31,  2^31 − 1]。

For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.  
根据这个假设，如果反转后的整数溢出，则返回 0。

### 思路
利用 Python 的字符串反转操作来实现对整数的反转，反转后的字符串要重新转换为整数。同时，要注意正负和溢出情况。
```python
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        revx = int(str(abs(x))[::-1])
        if revx > math.pow(2, 31):
            return 0
        else:
            return revx * cmp(x, 0)
```
[LeetCode 7. Reverse Integer](https://leetcode.com/problems/reverse-integer/description/)
