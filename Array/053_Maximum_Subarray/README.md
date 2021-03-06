### 题意
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.  
给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

Example:
```python
Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。

Follow up:  
If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.  
如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的分治法求解。

### 思路
两个指针，一个指针记录当前的最大值 curSum，一个记录循环每个元素时的最大值 maxSum。
```python
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        curSum = maxSum = nums[0]
        for num in nums[1:]:
            curSum = max(num, curSum + num)
            maxSum = max(maxSum, curSum)
            
        return maxSum
```
[LeetCode 53. Maximum Subarray](https://leetcode.com/problems/maximum-subarray/description/)
