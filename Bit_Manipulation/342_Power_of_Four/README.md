### 题意
Given an integer (signed 32 bits), write a function to check whether it is a power of 4.  
给定一个整数 (32位有符整数型)，请写出一个函数来检验它是否是4的幂。

Example:
```
Given num = 16, return true. Given num = 5, return false.
```

Follow up: Could you solve it without loops/recursion?  
问题进阶：你能不使用循环/递归来解决这个问题吗？

### 思路一
本题要求判断是不是 4 的幂。可以利用判断是否是 2 的幂的方法。

如果一个整数 num 是 2 的幂，则 num & (num-1) == 0，2 的幂自然是 4 的幂，只需要再添加一个条件，即：二进制的 num 中 0 的个数是偶数个即可。
```python
class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        # Python 里将数转成二进制后的表示为 “0bxxxx”，最前面有个 0，在计算 0 的个数时要考虑到。
        return num & (num-1) == 0 and bin(num).count('0') % 2 == 1
```

### 思路二
4 的幂次表现在二进制上是首位为 1，后面有偶数个 0。所以先将输入的数转换成二进制，再判断二进制中 0 和 1 的个数即可。
```python
class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        return num > 0 and bin(num).count('1') == 1 and bin(num).count('0') % 2 == 1
```

### 思路三
类似上面，我们可以先判断输入数的二进制形式为 1 后面若干个 0，再判断 1 是否在奇数位即可。
```python
class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        return num > 0 and num & (num-1) == 0 and (num & 0x55555555) != 0

# 0x55555555 是 16进制，二进制是 1010101010101010101010101010101
#>>> 64 & 0x55555555
#64
```

### 思路四
循环。
```python
class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 0:
            return False
        while num % 4 == 0:
            num /= 4
        return num == 1
```

### 思路五
递归思想。
```python
class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 0:
            return False
        if num == 1:
            return True
        if num % 4 == 0:
            return self.isPowerOfFour(num/4)
        else:
            return False
```
[LeetCode 342. Power of Four](https://leetcode.com/problems/power-of-four/description/)
