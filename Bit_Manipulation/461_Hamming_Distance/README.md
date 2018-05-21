### 题意
The Hamming distance between two integers is the number of positions at which the corresponding bits are different.  
两个整数之间的汉明距离指的是这两个数字对应二进制位不同的位置的数目。

Given two integers x and y, calculate the Hamming distance.  
给出两个整数 x 和 y，计算它们之间的汉明距离。

Note:  
0 ≤ x, y < 2^31.

Example:
```
Input: x = 1, y = 4

Output: 2

Explanation:
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑

The above arrows point to positions where the corresponding bits are different.
上面的箭头指出了对应二进制位不同的位置。
```

### 思路
汉明距离是以理查德·卫斯里·汉明的名字命名的。在信息论中，两个等长字符串之间的汉明距离是两个字符串对应位置的不同字符的个数。换句话说，它就是将一个字符串变换成另外一个字符串所需要替换的字符个数。例如：  
1011101 与 1001001 之间的汉明距离是 2。  
2143896 与 2233796 之间的汉明距离是 3。  
"toned" 与 "roses" 之间的汉明距离是 3。

```python
class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        xor = x ^ y
        n = 0
        while xor:
            n += 1
            xor = xor & (xor - 1)
        return n
```
[LeetCode 461. Hamming Distance](https://leetcode.com/problems/hamming-distance/description/)
