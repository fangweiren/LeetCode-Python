题意：  
Given an integer, write a function to determine if it is a power of two.  
给定一个整数，写一个函数来判断它是否是2的若干次幂。

思路：  
2的幂次 x 表示成二进制一定是一个1后面若干个0，那么 x-1 一定是一个0后面若干个1，所以 x & (x-1) = 0 ，非2的幂无法得到0。
```
>>> bin(2)
'0b10'
>>> bin(4)
'0b100'
>>> bin(8)
'0b1000'
>>> bin(16)
'0b10000'
>>> bin(32)
'0b100000'
>>> bin(64)
'0b1000000'
>>> 
```

```
class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n > 0 and not (n & n-1)
```

[231. Power of Two](https://leetcode.com/problems/power-of-two/description/)  
[231. Power of Two [easy] (Python)](http://blog.csdn.net/coder_orz/article/details/51322908)
