### 题意
Given a non-empty integer array of size n, find the minimum number of moves required to make all array elements equal, where a move is incrementing n - 1 elements by 1.  
给定一个长度为 n 的非空整数数组，找到让数组所有元素相等的最小移动次数。每次移动可以使 n - 1 个元素增加 1。

Example:
```python
Input:
[1,2,3]

Output:
3

Explanation:
Only three moves are needed (remember each move increments two elements):
只需要3次移动（注意每次移动会增加两个元素的值）：

[1,2,3]  =>  [2,3,3]  =>  [3,4,3]  =>  [4,4,4]
```
### 思路
一次移动将 n - 1 个元素加 1，等价于将剩下的 1 个元素减 1。因此数组中各元素之和与数组中的最小值只差就是最小移动次数。
```python
class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sum(nums) - min(nums) * len(nums)
```
[LeetCode 453. Minimum Moves to Equal Array Elements](https://leetcode.com/problems/minimum-moves-to-equal-array-elements/description/)
