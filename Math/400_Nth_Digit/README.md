### 题意
Find the `n**th` digit of the infinite integer sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ...  
在无限的整数序列 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ...中找到第 n 个数字。

Note:  
n is positive and will fit within the range of a 32-bit signed integer (n < `2**31`).  
n 是正数且在 32 为整形范围内 ( n < `2**31`)。
```python
Example 1:

Input:
3
Output:
3

Example 2:

Input:
11
Output:
0

Explanation:
The 11th digit of the sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ... is a 0, which is part of the number 10.
第 11 个数字在序列 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ... 里是 0，它是 10 的一部分。
```
### 思路
```python
第一步:确定是在哪几位数之间
第二步:确定是哪个数
第三步:确定是这个数的哪一位数

举个例子，比如 n=23456，在 `9+90*2+900*3` 和 `9+90*2+900*3+9000*4` 之间，所以说明，这个数在 1000-9999 之间，是一个四位数。

一位数时，`9*1=9`个，
二位数时，`90*2=180`个，
三位数时，`900*3=2700`个，
。。。

以此类推，

所以 base 代表每位数的个数，9、90、900...，ith 代表每位数开始的那个数，1、10、100...，digit 代表几位数，1 2 3...这样，循环时，判断 n 与 `base*digit` 的大小，进入 n、base、ith、digit 的调整。

n = `23456 - 9 - 90*2 - 900*3 = 20567`

也就是，从 1000 开始，数 20567 位，那到底是落在哪个数字上呢？

num = 1000 + (20567-1)/4 = 6141

所以说，在 6141 的某一位上，就是第 n = 23456 位数，那到底是哪一位呢？

ind = (20567-1)%4 = 2

这说明，在 6141 的第 3 位上，也就是 4。

注意:这里最后计算是哪个数、哪一位时，要减去1，这是因为整除代表某个数的最后一位，所以需要减1。
```
```python
class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        digit = 1   # 确定是哪一位
        base = 9    # 每位的数的个数
        ith = 1     # 起始值
        while n > base * digit:
            n = n - base * digit
            digit += 1
            ith += base
            base *= 10
        num = ith + (n - 1) / digit
        ind = (n - 1) % digit
        print num, ind
        return int(str(num)[ind]) 
```
[LeetCode 400. Nth Digit](https://leetcode.com/problems/nth-digit/description/)
