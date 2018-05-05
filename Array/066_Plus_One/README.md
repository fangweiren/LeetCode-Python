### 题意
Given a non-empty array of digits representing a non-negative integer, plus one to the integer.  
给定一个非负整数组成的非空数组，在该数的基础上加一，返回一个新的数组。

The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.  
最高位数字存放在数组的首位， 数组中每个元素只存储一个数字。

You may assume the integer does not contain any leading zero, except the number 0 itself.  
你可以假设除了整数 0 之外，这个整数不会以零开头。
```python
Example 1:

Input: [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
解释: 输入数组表示数字 123。

Example 2:

Input: [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
```
### 思路
从右向左遍历数组，末位加 1，有进位则变成 0 且保留进位。如果最高位产生了进位需要在数组的头部插入 1。
```python
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        flag = 1
        for i in range(len(digits)-1, -1, -1):
            if digits[i] + flag == 10:
                digits[i] = 0
                flag = 1
            else:
                digits[i] = digits[i] + flag
                flag = 0
                break      # 如果没有进位可以跳出循环，因为 plus one 已经完成。
        if flag == 1:
            digits.insert(0, 1)
        return digits
```
[LeetCode 66. Plus One](https://leetcode.com/problems/plus-one/description/)
