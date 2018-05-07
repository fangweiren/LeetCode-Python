### 题意
Implement int sqrt(int x).  
实现 int sqrt(int x) 函数。

Compute and return the square root of x, where x is guaranteed to be a non-negative integer.  
计算并返回 x 的平方根，其中 x 是非负整数。

Since the return type is an integer, the decimal digits are truncated and only the integer part of the result is returned.  
由于返回类型是整数，结果只保留整数的部分，小数部分将被舍去。

Example 1:
```
Input: 4
Output: 2
```
Example 2:
```
Input: 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since 
             the decimal part is truncated, 2 is returned.
说明: 8 的平方根是 2.82842...,由于返回类型是整数，小数部分将被舍去。
```
### 思路
二分查找。

```python
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x <= 1:
            return x
        low, high = 0, x/2+1
        while low <= high:
            mid = (low + high) / 2
            if mid * mid == x:
                return mid
            elif mid * mid > x:
                high = mid - 1
            else:
                low = mid + 1
        return high
```
[LeetCode 69. Sqrt(x)](https://leetcode.com/problems/sqrtx/description/)
