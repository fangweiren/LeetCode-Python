### 题意
Given a positive integer num, write a function which returns True if num is a perfect square else False.  
给定一个正整数 num，编写一个函数，如果 num 是一个完全平方数，则返回 True，否则返回 False。

Note: Do not use any built-in library function such as sqrt.  
注意：不要使用任何内置的库函数，如 sqrt。
```python
Example 1:

Input: 16
Returns: True

Example 2:

Input: 14
Returns: False
```
### 思路
使用二分法
```python
class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        low, high = 0, num
        if num == 1:
            return True
        while low < high:
            mid = (low + high) / 2
            if mid * mid == num:
                return True
            elif mid * mid < num:
                low = mid + 1
            elif mid * mid > num:
                high = mid
        return False
```
[LeetCode 367. Valid Perfect Square](https://leetcode.com/problems/valid-perfect-square/description/)
