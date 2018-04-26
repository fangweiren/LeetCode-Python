### 题意
Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.  
给定一个范围在  1 ≤ a[i] ≤ n ( n = 数组大小 ) 的 整型数组，数组中的元素一些出现了两次，另一些只出现一次。

Find all the elements of [1, n] inclusive that do not appear in this array.  
找到所有在 [1, n] 范围之间没有出现在数组中的数字。

Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.  
您能在不使用额外空间且时间复杂度为O(n)的情况下完成这个任务吗? 你可以假定返回的数组不算在额外空间内。

Example:
```python
Input:
[4,3,2,7,8,2,3,1]

Output:
[5,6]
```
### 思路
#### 正负号标记法
1.遍历数组nums，记当前元素为n，令nums[abs(n) - 1] = -abs(nums[abs(n) - 1])  
2.再次遍历nums，将正数对应的下标+1返回即为答案，因为正数对应的元素没有被上一步骤标记过。
```python
class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for num in nums:
            nums[abs(num) - 1] = -abs(nums[abs(num) - 1])
        return [ind + 1 for ind, val in enumerate(nums) if val > 0]
```
[LeetCode 448. Find All Numbers Disappeared in an Array](https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/description/)
