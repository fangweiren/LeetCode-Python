### 题意
Write a program to check whether a given number is an ugly number.  
编写程序判断给定的数是否为丑数。

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. For example, 6, 8 are ugly while 14 is not ugly since it includes another prime factor 7.  
丑数就是只包含质因子 2, 3, 5 的正整数。例如， 6, 8 是丑数，而 14 不是，因为它包含了另外一个质因子 7。

Note:  
1. 1 is typically treated as an ugly number.  
1. 1 也可以被当做丑数。  
2. Input is within the 32-bit signed integer range.  
2. 输入不会超过32位整数的范围。

### 思路
根据丑数定义，依次将所给的数除以 2、3、5，直至无法除尽，如果这时得到 1 则说明所给的数的质因子不超出 2，3，5三个数，否则说明有其他质因数。

```python
class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        while True:
            if num <= 0:
                return False
            if num == 1:
                return True
            elif num % 2 == 0:
                num /= 2
            elif num % 5 == 0:
                num /= 5
            elif num % 3 == 0:
                num /= 3
            else:
                return False

# Another
class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 0:
            return False
        for i in [2, 3, 5]:
            while num % i == 0:
                num /= i
        return True if num == 1 else False
```
[LeetCode 263. Ugly Number](https://leetcode.com/problems/ugly-number/description/)
