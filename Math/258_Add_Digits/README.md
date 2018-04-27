### 题意
Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.  
给一个非负整数 num，反复添加所有的数字，直到结果只有一个数字。

For example:  
Given num = 38, the process is like: 3 + 8 = 11, 1 + 1 = 2. Since 2 has only one digit, return it.  
设定 num = 38，过程就像： 3 + 8 = 11, 1 + 1 = 2。 由于 2 只有 1 个数字，所以返回它。

Follow up:  
进阶:  
Could you do it without any loop/recursion in O(1) runtime?  
你可以不用任何的循环或者递归算法，在 O(1) 的时间内解决这个问题么？

### 思路
先分析。一个数，假如设为 ABCD，则实际上这个数可以表达为 `num = A*1000 + B*100 + C*10 + D`。  
可分解为 `num = (A+B+C+D) + (999*A+99*B+9*C)`，因为我们需要求的是 A+B+C+D，所以我们可以采用 % 的方法。  
因为 `(999*A+99*B+9*C)` 肯定是 9 的倍数，则 `num % 9 = A+B+C+D`，如果 A+B+C+D>=10，对 9 取余，可依照刚才的方法继续分析，结果是一样的。  
但是，当 `num = 9` 时，`9 % 9 = 0`，不符合题目的要求，所以算法的核心是  
`result = （num - 1）% 9 + 1`
```python
class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num == 0:
            return 0
        elif num % 9 == 0:
            return 9
        else:
            return num % 9

# Another
class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num == 0:
            return 0
        result = (num-1) % 9 + 1
        return result
```
[LeetCode 258. Add Digits](https://leetcode.com/problems/add-digits/description/)
