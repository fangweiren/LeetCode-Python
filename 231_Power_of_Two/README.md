题意：  
Given an integer, write a function to determine if it is a power of two.  
给定一个整数，写一个函数来判断它是否是2的若干次幂。

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
[参考](http://blog.csdn.net/coder_orz/article/details/51322908)
