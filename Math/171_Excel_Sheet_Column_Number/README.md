### 题意
Given a column title as appear in an Excel sheet, return its corresponding column number.  
给定一个 Excel 表格中的列名称，返回其相应的列序号。

For example:
```
    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28 
    ...
```
Example 1:
```
Input: "A"
Output: 1
```
Example 2:
```
Input: "AB"
Output: 28
```
Example 3:
```
Input: "ZY"
Output: 701
```

### 思路
168 题逆向思维。
```python
class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        sum = 0
        for c in s:
            sum = sum * 26 + ord(c) - ord('A') + 1
        return sum
```
[LeetCode 171. Excel Sheet Column Number](https://leetcode.com/problems/excel-sheet-column-number/description/)
