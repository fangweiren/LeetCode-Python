### 题意
Given a positive integer, return its corresponding column title as appear in an Excel sheet.  
给定一个正整数，返回它在Excel表中相对应的列名称。

For example:
```
    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB 
    ...
```
Example 1:
```
Input: 1
Output: "A"
```
Example 2:
```
Input: 28
Output: "AB"
```
Example 3:
```
Input: 701
Output: "ZY"
```
### 题目分析
首先，我们要知道 Excel 里这个对应关系是什么样的。从 A-Z 对应 1-26，当列标题进一位变成 AA 时，列对应的数字变成 27。所以这个题本质上是一个 10 进制转 26 进制的问题，不过 A 从 1 开始，而不是 0，要注意。

### 思路
采用除余结合的思想，但是要考虑 26 % 26 为 0 的情况，所以先 n-1，再除以 26，再加上 'A'。
```python
class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        res = ''
        while n:
            res = chr((n-1) % 26 + 65) + res
            n = (n-1) / 26
        return res
```
[LeetCode 168. Excel Sheet Column Title](https://leetcode.com/problems/excel-sheet-column-title/description/)
