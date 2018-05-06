### 题意
Write an algorithm to determine if a number is "happy".  
编写一个算法来判断一个数是不是“快乐数”。

A happy number is a number defined by the following process:  
一个“快乐数”定义为：

Starting with any positive integer, replace the number by the sum of the squares of its digits,  
对于一个正整数，每一次将该数替换为它每个位置上的数字的平方和,

and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.  
然后重复这个过程直到这>个数变为 1，也可能是无限循环但始终变不到 1。

Those numbers for which this process ends in 1 are happy numbers.  
如果可以变为 1，那么这个数就是快乐数。

Example: 
```python
Input: 19
Output: true
Explanation: 
1**2 + 9**2 = 82
8**2 + 2**2 = 68
6**2 + 8**2 = 100
1**2 + 0**2 + 0**2 = 1
```
### 思路
按照 “happy number” 的定义，直接循环计算 n 每一位的平方和，观察是否收敛到 1，若为 1 则 n 是 happy number。为了判断循环是否开始重复，要用一个字典 (dict) 或集合 (set) 来保存已经出现的数字，dict 的效率更高。
```python
class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        c = set()
        while n not in c:
            c.add(n)
            n = sum([int(x) ** 2 for x in str(n)])
        return n == 1
```
[LeetCode 202. Happy Number](https://leetcode.com/problems/happy-number/description/)
