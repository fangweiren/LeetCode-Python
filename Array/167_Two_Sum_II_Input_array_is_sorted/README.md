### 题意
Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.  
给定一个已按照升序排列的有序数组，找到两个数使得它们相加之和等于目标数。

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2.  
函数应该返回这两个下标值 index1 和 index2，其中 index1 必须小于 index2。

Note:
- Your returned answers (both index1 and index2) are not zero-based.  
- 返回的下标值（index1 和 index2）不是从零开始的。

- You may assume that each input would have exactly one solution and you may not use the same element twice.  
- 你可以假设每个输入只对应唯一的答案，而且你不可以重复使用相同的元素。

Example:
```python
Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.
解释: 2 与 7 之和等于目标数 9 。因此 index1 = 1, index2 = 2 。
```
### 题目分析：
题目说了两个重要条件：1.有序数组；2.有唯一解。所以解的两个数一定都是数组中唯一存在的数。
### 思路一
利用两个指针从数组的两侧开始向中间移动，寻找第一对和为 target 的两个数即为所求。
```python
class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        left, right = 0, len(numbers)-1
        while left < right:
            if numbers[left] + numbers[right] == target:
                return [left+1, right+1]
            elif numbers[left] + numbers[right] > target:
                right -= 1
            else:
                left += 1
```
### 思路二
遍历数组，用字典记录 {值: 索引}，并判断另一个数是否在字典中。
```python
class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        num_dict = {}
        for ind, num in enumerate(numbers):
            another = target - num
            if another in num_dict.keys():
                return [num_dict[another]+1, ind+1]
            else:
                num_dict[num] = ind
```
[LeetCode 167. Two Sum II - Input array is sorted](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/)
