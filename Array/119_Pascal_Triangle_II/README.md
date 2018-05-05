### 题意
Given a non-negative index k where k ≤ 33, return the `k**th` index row of the Pascal's triangle.  
给定一个非负索引 k，其中 k ≤ 33，返回杨辉三角的第 k 行。

Note that the row index starts from 0.  
请注意，行索引从0开始。

Example:
```python
Input: 3
Output: [1,3,3,1]
```
Follow up:  
Could you optimize your algorithm to use only O(k) extra space?  
你可以优化你的算法到 O(k) 空间复杂度吗？

### 思路
因为有空间限制，在 Pascal's Triangle 的基础上节约空间。
```python
class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        row = [1]
        for _ in range(rowIndex):
            row = [x + y for x, y in zip([0]+row, row+[0])]
        return row
```
[LeetCode 119. Pascal's Triangle II](https://leetcode.com/problems/pascals-triangle-ii/description/)
