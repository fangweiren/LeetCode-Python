### 题意
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.  
给定一个数组 nums, 编写一个函数将所有 0 移动到它的末尾，同时保持非零元素的相对顺序。

For example, given nums = [0, 1, 0, 3, 12], after calling your function, nums should be [1, 3, 12, 0, 0].  
例如，定义 nums = [0, 1, 0, 3, 12]，调用函数之后，nums 应为 [1, 3, 12, 0, 0]。

Note:  
You must do this in-place without making a copy of the array.  
必须在原数组上操作，不要为一个新数组分配额外空间。  
Minimize the total number of operations.  
尽量减少操作总数。

### 思路一
从后向前搜索，找到 0 就移除，然后在最后加 0。
```
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        for i in xrange(len(nums)-1,-1,-1):
            if nums[i] == 0:
                nums.pop(i)
                nums.append(0)
```
### 思路二
遍历 nums，遇到非 0 的数，就与 0 交换。
```python
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        zero = 0 # 0 的位置
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[zero] = nums[zero], nums[i]
                zero += 1
```
[LeetCode 283. Move Zeroes](https://leetcode.com/problems/move-zeroes/description/)
