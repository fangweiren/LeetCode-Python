### 题意
Count the number of prime numbers less than a non-negative number, n.  
求小于 n 的所有素数的个数。

Example:
```python
Input: 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
解释: 小于 10 的质数一共有 4 个, 它们是 2, 3, 5, 7 。
```
### 思路
从下面的厄拉多塞筛法可以看出，我们只需遍历 [2, `n**0.5`]，因为超过 `n**0.5`(根号 n) 部分如果不是素数，则作为因子在前面的数已经被删除了。同时这里利用了 Python 里 list 的特性 [::i] 取 i 的倍数。
![厄拉多塞筛法](http://img1.ph.126.net/ReCXM6aHuw2AqdoW0kS82A==/6632742321909826660.png)
```python
class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 3:
            return 0
        primes = [True] * n
        primes[0] = primes[1] = False
        for i in range(2, int(n ** 0.5) + 1):
            if primes[i]:
                primes[i * i: n: i] = [False] * len(primes[i * i: n: i])
        return sum(primes)
```
[LeetCode 204. Count Primes](https://leetcode.com/problems/count-primes/description/)
