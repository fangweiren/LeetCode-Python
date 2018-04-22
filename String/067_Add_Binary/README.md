### 题意  
Given two binary strings, return their sum (also a binary string).  
给定两个二进制字符串，返回他们的和（用二进制表示）。

The input strings are both non-empty and contains only characters 1 or 0.  
输入为非空字符串且只包含数字 1 和 0。

Example 1:
```python
Input: a = "11", b = "1"
Output: "100"
```
Example 2:
```python
Input: a = "1010", b = "1011"
Output: "10101"
```
### 思路  
采用递归的思路，从末位开始相加，要分五种情况进行讨论：  
1、a 为空，返回 b  
2、b 为空，返回 a  
3、a 和 b 的末位都是 1，递归的同时，末位添 0，同时前面要再和 '1' 想加  
4、a 和 b 的末位都是 0，递归的同时，末位添 0  
5、a 和 b 的末位有一个为 1，递归的同时，末位添 1
```python
class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        if a == '':
            return b
        if b == '':
            return a
        if a[-1] == '1' and b[-1] == '1':
            return self.addBinary(self.addBinary(a[:-1], b[:-1]), '1') + '0'
        elif a[-1] == '0' and b[-1] == '0':
            return self.addBinary(a[:-1], b[:-1]) + '0'
        else:
            return self.addBinary(a[:-1], b[:-1]) + '1'
```
![递归运行图](https://github.com/fangweiren/LeetCode-Python/blob/master/screenshots/addBinary.JPG?raw=true)
[LeetCode 67. Add Binary](https://leetcode.com/problems/add-binary/description/)
