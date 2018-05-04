### 题意
Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.  
给定一个非负整数 numRows，生成杨辉三角的前 numRows 行。

Example:
```python
Input: 5
Output:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
```
### 思路
杨辉三角的特点是每一行的第一和最后一个元素是 1，其它元素是上一行它左右两个元素之和。以 [1,3,3,1] 为例，下一行中间元素就是 [1+3,3+3,3+1]，也就是 [1,3,3] 和 [3,3,1] 对应数字求和。
```python
class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if not numRows:
            return []
        result = [[1]]
        while numRows > 1:
            result.append([1] + [a + b for a, b in zip(result[-1][:-1], result[-1][1:])] + [1])
            numRows -= 1
        return result
```
[LeetCode 118. Pascal's Triangle](https://leetcode.com/problems/pascals-triangle/description/)
