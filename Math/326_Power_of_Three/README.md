### 题意
Given an integer, write a function to determine if it is a power of three.  
给出一个整数，写一个函数来确定这个数是不是3的一个幂。

Follow up:  
Could you do it without using any loop / recursion?  
你能不使用循环或者递归完成本题吗？

### 思路
求对数，然后乘方，判断得数是否相等
```python
# 先不考虑进阶的要求，用循环的方法：每次尝试将输入的数除以 3，观察是否能整除，若不能则说明不是 3 的倍数；若能，则用除以 3 的结果循环上述过程，直至得到 1，说明输入是 3 的幂次。
class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False
        while n%3 == 0:
            n /= 3
        return n == 1

# 用递归的方法
class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False
        if n == 1:
            return True
        if n%3 == 0:
            return self.isPowerOfThree(n/3)
        else:
            return False

# 求对数，然后乘方，判断得数是否相等
class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n > 0:
            if 3 ** round(math.log(n, 3)) == n:
                return True
            else:
                return False
        else:
            return False
```
[LeetCode 326. Power of Three](https://leetcode.com/problems/power-of-three/description/)
