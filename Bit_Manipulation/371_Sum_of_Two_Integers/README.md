### 题意
Calculate the sum of two integers a and b, but you are not allowed to use the operator + and -.  
不使用运算符 + 和 -，计算两整数 a 和 b 的和。

Example:
```
Given a = 1 and b = 2, return 3.
```

### 思路
不能使用加法和减法，那么就用位操作。下面以计算 5+4 的例子说明如何用位操作实现加法:  
1.用二进制表示两个加数，a=5=0101，b=4=0100  
2.用 and(&) 操作得到所有位上的进位 carry=0100  
3.用 xor(^) 操作找到 a 和 b 不同的位，赋值给 a，a=0001  
4.将进位 carry 左移一位，赋值给 b，b=1000  
5.循环直到进位 carry 为 0，此时得到 a=1001，即最后的 sum。
```python
class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        # 32 bits integer max       ('0b1111111111111111111111111111111')
        MAX = 0x7FFFFFFF
        # 32 bits interger min     ('0b10000000000000000000000000000000')
        MIN = 0x80000000
        # mask to get last 32 bits ('0b11111111111111111111111111111111')
        mask = 0xFFFFFFFF
        while b != 0:
            # ^ get different bits and & gets double 1s, << moves carry
            carry = a & b
            a = (a ^ b) & mask
            b = (carry << 1) & mask
        # if a is negative, get a's 32 bits complement positive first
        # then get 32-bit positive's Python complement negative
        return a if a <= MAX else ~(a ^ mask)
```
[LeetCode 371. Sum of Two Integers](https://leetcode.com/problems/sum-of-two-integers/description/)
