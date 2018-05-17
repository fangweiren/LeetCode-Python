### 题意
Write a function that takes an unsigned integer and returns the number of '1' bits it has (also known as the Hamming weight).  
编写一个函数，输入是一个无符号整数，返回其二进制表达式中数字位数为 ‘1’ 的个数（也被称为汉明重量）。

Example 1:
```
Input: 11
Output: 3
Explanation: Integer 11 has binary representation 00000000000000000000000000001011
```
Example 2:
```
Input: 128
Output: 1
Explanation: Integer 128 has binary representation 00000000000000000000000010000000
```

### 思路一
利用 n & (n-1) 可以将 n 最低位的 1 变成 0。循环进行计数。
![](https://github.com/fangweiren/leetcode/blob/master/screenshots/1234.jpg?raw=true)
```python
class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        while n:
            n = n & (n-1)
            count += 1
        return count
```

### 思路二
通过移位操作，每次向右移动一位，一位一位的判定是否是数字 1。
![](https://github.com/fangweiren/leetcode/blob/master/screenshots/2234.jpg?raw=true)
```python
class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        while n:
            count += n & 1
            n >>= 1
        return count
```

### 思路三
将输入的数转换为二进制的字符串，数一下有多少个 1 即可。
```python
class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        return bin(n).count('1')
```
[LeetCode 191. Number of 1 Bits](https://leetcode.com/problems/number-of-1-bits/description/)
