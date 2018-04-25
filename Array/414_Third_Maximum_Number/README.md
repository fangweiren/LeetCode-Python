### 题意
Given a non-empty array of integers, return the third maximum number in this array. If it does not exist, return the maximum number. The time complexity must be in O(n).  
给定一个非空数组，返回此数组中第三大的数。如果不存在，则返回数组中最大的数。要求算法时间复杂度必须是O(n)。

Example 1:
```python
Input: [3, 2, 1]

Output: 1

Explanation: The third maximum is 1.
```
Example 2:
```python
Input: [1, 2]

Output: 2

Explanation: The third maximum does not exist, so the maximum (2) is returned instead.
```
Example 3:
```python
Input: [2, 2, 3, 1]

Output: 1

Explanation: Note that the third maximum here means the third maximum distinct number.
解释: 注意，要求返回第三大的数，是指第三大且唯一出现的数。
Both numbers with value 2 are both considered as second maximum.
存在两个值为2的数，它们都排第二。

### 思路一
遍历 nums 分别与 top1 top2 top3 比较。
```python
class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        top1 = top2 = top3 = float('-inf')
        for num in nums:
            if num not in (top1, top2, top3):
                if num > top1:
                    top1, num = num, top1  # 此时 num = top1 参与后续计算
                if num > top2:
                    top2, num = num, top2
                if num > top3:
                    top3, num = num, top3
        if top3 == float('-inf'):
            return top1
        return top3
```
### 思路二
把数组中重复的元素通过 set 去掉，然后 remove 掉两次最大值，在整下的元素里面取最大值，就是第三大值。
```python
class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = set(nums)
        if len(nums) <= 2:
            return max(nums)
        nums.remove(max(nums))
        nums.remove(max(nums))
        return max(nums)
```
[LeetCode 414. Third Maximum Number](https://leetcode.com/problems/third-maximum-number/description/)
