### 题意
Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.  
给定两个字符串形式的非负整数 num1 和 num2 ，计算它们的和。

```python
Note:
  1.The length of both num1 and num2 is < 5100.
  1.num1 和 num2 的长度都小于 5100。
  2.Both num1 and num2 contains only digits 0-9.
  2.num1 和 num2 都只包含数字 0-9。
  3.Both num1 and num2 does not contain any leading zero.
  3.num1 和 num2 都不包含任何前导零。
  4.You must not use any built-in BigInteger library or convert the inputs to integer directly.
  4.你不能使用任何內建 BigInteger 库，也不能直接将输入的字符串转换为整数形式。
```
### 思路
曲线救国，先转成 list,在转成 num，最后相加。
```python
class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        digits1 = list(num1)
        digits2 = list(num2)
        
        sum1 = 0
        sum2 = 0
        for i in digits1:
            sum1 *= 10
            sum1 += int(i)
            
        for i in digits2:
            sum2 *= 10
            sum2 += int(i)

        return str(sum1 + sum2)           
```
[LeetCode 415. Add Strings](https://leetcode.com/problems/add-strings/description/)
