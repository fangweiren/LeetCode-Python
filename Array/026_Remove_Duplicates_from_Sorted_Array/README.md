### 题意
Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.  
给定一个排序数组，你需要在原地删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度。

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.  
不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成。
```python
Example 1:

Given nums = [1,1,2],

Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.
函数应该返回新的长度 2, 并且原数组 nums 的前两个元素被修改为 1, 2。

It doesn't matter what you leave beyond the returned length.
你不需要考虑数组中超出新长度后面的元素。

Example 2:

Given nums = [0,0,1,1,1,2,2,3,3,4],

Your function should return length = 5, with the first five elements of nums being modified to 0, 1, 2, 3, and 4 respectively.
函数应该返回新的长度 5, 并且原数组 nums 的前五个元素被修改为 0, 1, 2, 3, 4。

It doesn't matter what values are set beyond the returned length.
```
### 思路
这类题想明白了其实解题很简单，重复的需要去掉，无非就是遍历数组，发现重复，就把后面的往前移，把重复值覆盖掉。具体说，可以维护 2 个指针，慢指针开始指向数组第一个元素，快指针指向第二个元素，然后快指针不断判断自己当前元素和前一个元素是否相同，相同则快指针后移，不相同则将当前值赋值给慢指针的后一个元素，慢指针后移。最后慢指针指向的元素及前面所有元素都是不重复的。
```python
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0

        cur = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                cur += 1
                nums[cur] = nums[i]
        return cur+1
```
[LeetCode 26. Remove Duplicates from Sorted Array](https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/)
