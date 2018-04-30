### 题意
You have a total of n coins that you want to form in a staircase shape, where every k-th row must have exactly k coins.  
你总共有 n 枚硬币，你需要将它们摆成一个阶梯形状，第 k 行就必须正好有 k 枚硬币。

Given n, find the total number of full staircase rows that can be formed.  
给定一个数字 n，找出可形成完整阶梯行的总行数。

n is a non-negative integer and fits within the range of a 32-bit signed integer.  
n 是一个非负整数，并且在32位有符号整型的范围内。
```python
Example 1:

n = 5

The coins can form the following rows:
¤
¤ ¤
¤ ¤

Because the 3rd row is incomplete, we return 2.
因为第三行不完整，所以返回2.

Example 2:

n = 8

The coins can form the following rows:
¤
¤ ¤
¤ ¤ ¤
¤ ¤

Because the 4th row is incomplete, we return 3.
```

### 思路
二分枚举法
```python
class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        k = 0
        while k * (k+1) / 2 <= n:
            k += 1
        return k-1


class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        low, high = 0, n
        while low <= high:
            mid = (low+high) / 2
            if mid * (mid+1) / 2 > n:
                high = mid - 1
            else:
                low = mid + 1
        return high
```
[LeetCode 441. Arranging Coins](https://leetcode.com/problems/arranging-coins/description/)
