### 题意
Given an array nums and a value val, remove all instances of that value in-place and return the new length.  
给定一个数组 nums 和一个值 val，你需要原地移除所有数值等于 val 的元素，返回移除后数组的新长度。

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.  
不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成。

The order of elements can be changed. It doesn't matter what you leave beyond the new length.  
元素的顺序可以改变。你不需要考虑数组中超出新长度后面的元素。
```python
Example 1:

Given nums = [3,2,2,3], val = 3,

Your function should return length = 2, with the first two elements of nums being 2.

It doesn't matter what you leave beyond the returned length.
你不需要考虑数组中超出新长度后面的元素。

Example 2:

Given nums = [0,1,2,2,3,0,4,2], val = 2,

Your function should return length = 5, with the first five elements of nums containing 0, 1, 3, 0, and 4.

Note that the order of those five elements can be arbitrary.  
注意这五个元素可为任意顺序。

It doesn't matter what values are set beyond the returned length.  
你不需要考虑数组中超出新长度后面的元素。

### 思路一
类似于 26 题的思路，要点是要把不等于目标值的元素放到数组前面。
```python
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        index = 0
        for num in nums:
            if val != num:
                nums[index] = num
                index += 1
        return index
```
### 思路二
遍历到等于 val 的值时，直接拿数组最末的数字填充，然后继续从这个填充位置向后遍历。
```python
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        left, right = 0, len(nums)
        while left < right:
            if nums[left] == val:
                nums[left] = nums[right-1]
                right -= 1
            else:
                left += 1
                
        return right
```
[LeetCode 27. Remove Element](https://leetcode.com/problems/remove-element/description/)
