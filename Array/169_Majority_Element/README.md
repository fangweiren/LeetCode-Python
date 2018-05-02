### 题意
Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.  
给定一个大小为 n 的数组，找到其中的众数。众数是指在数组中出现次数大于 ⌊ n/2 ⌋ 的元素。

You may assume that the array is non-empty and the majority element always exist in the array.  
你可以假设数组是非空的，并且给定的数组总是存在众数。
```python
Example 1:

Input: [3,2,3]
Output: 3

Example 2:

Input: [2,2,1,1,1,2,2]
Output: 2
```

### 思路
遍历数组，用一个字典记录所有出现过的元素及其个数。由于题目说明多数元素一定存在，故当找到某个元素出现次数大于 ⌊ n/2 ⌋ 时即可停止。  
```python
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dict = {}
        for num in nums:
            dict[num] = dict.get(num, 0) + 1
            if dict[num] > len(nums) / 2:
                return num
```
### 思路二
先对数组进行排序，因为多数元素一定存在，且个数超过总个数的一半，那么排序后最中间的那个元素一定是多数元素。
```python
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        return nums[len(nums)/2]
```
