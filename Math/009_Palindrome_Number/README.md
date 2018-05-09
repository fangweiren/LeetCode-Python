### 题意
Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.  
判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。

Example 1:
```
Input: 121
Output: true
```
Example 2:
```
Input: -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.  
解释:从左向右读,为 -121 。从右向左读,为 121- 。因此它不是一个回文数。
```
Example 3:
```
Input: 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
解释: 从右向左读, 为 01 。因此它不是一个回文数。
```
Follow up:  
Coud you solve it without converting the integer to a string?  
你能不将整数转为字符串来解决这个问题吗？

### 思路
1.负数没有回文数。
2.得到 x 是几位数，如 x=12321，得到 count=10000。
3.分别判断最左边一位和最右边一位是否相等。
4.x 去掉左右一位，先对 count 取余再除以 10，而 count 则缩小 100 倍。
```python
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        count = 1
        while x / count >= 10:
            count *= 10
        while x:
            left = x / count
            right = x % 10
            if left != right:
                return False
            x = (x % count) / 10
            count /= 100
        return True
```
[LeetCode 9. Palindrome Number](https://leetcode.com/problems/palindrome-number/description/)
