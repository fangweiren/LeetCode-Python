### 题意
Given an integer n, return the number of trailing zeroes in n!.  
给定一个整数 n，返回 n! 结果尾数中零的数量。
```python
Example 1:

Input: 3
Output: 0
Explanation: 3! = 6, no trailing zero.
解释: 3! = 6, 尾数中没有零。

Example 2:

Input: 5
Output: 1
Explanation: 5! = 120, one trailing zero.
解释: 5! = 120, 尾数中有 1 个零。
```
Note: Your solution should be in logarithmic time complexity.  
说明: 你算法的时间复杂度应为 O(logN) 。

### 思路
所有尾部的 0 可以看做都是 2X5 得来的，所以通过计算所有的因子中 2 和 5 的个数就可以知道尾部 0 的个数。  
实际上，2 的个数肯定是足够的，所以只需计算 5 的个数即可。要注意，25 = 5X5 是有两个 5 的因子；125 = 5X5X5 有 3 个 5 的因子。  
比如，计算 135! 末尾 0 的个数。首先 135/5 = 27，说明 135 以内有 27 个 5 的倍数(5,10,...,25,...125,130,135)；27/5 = 5，说明 135 以内有 5 个 25 的倍数(25,50,75,100,125)；5/5 = 1，说明 135 以内有 1 个 125 的倍数(125)。当然其中有重复计数，算下来 135 以内因子 5 的个数为 27+5+1 = 33。
```python
class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        while n > 0:
            n /= 5
            count += n
        return count
```
[LeetCode 172. Factorial Trailing Zeroes](https://leetcode.com/problems/factorial-trailing-zeroes/description/)
