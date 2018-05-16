### 题意
Reverse bits of a given 32 bits unsigned integer.  
颠倒给定的 32 位无符号整数的二进制位。

Example:
```
Input: 43261596
Output: 964176192
Explanation: 43261596 represented in binary as 00000010100101000001111010011100, 
             return 964176192 represented in binary as 00111001011110000010100101000000.
解释: 43261596 的二进制表示形式为 00000010100101000001111010011100 ，返回 964176192，其二进制表示形式为 00111001011110000010100101000000 。
```
Follow up:
If this function is called many times, how would you optimize it?  
如果多次调用这个函数，你将如何优化你的算法？

### 思路
1.先转换成 32 位二进制，不足 32 位在前面填充 0。  
2.翻转  
3.转换回整数
```python
class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        oribin = '{:032b}'.format(n)
        reversebin = oribin[::-1]
        return int(reversebin, 2)

#-------------------------------------------------
class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        b = bin(n)[:1:-1]
        return int(b + '0'*(32-len(b)), 2)
```
[LeetCode 190. Reverse Bits](https://leetcode.com/problems/reverse-bits/description/)
