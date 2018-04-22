题意  
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.  
给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。

Note: For the purpose of this problem, we define empty string as valid palindrome.  
说明：本题中，我们将空字符串定义为有效的回文串。

Example 1:
```python
Input: "A man, a plan, a canal: Panama"
Output: true
```
Example 2:
```python
Input: "race a car"
Output: false
```
思路  
先将字符串中的非字母和数字的字符去除，同时把所有的字母转换为小写，再判断新的字符串与自己翻转的字符串是否相等。
```python
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        newstr = [x for x in s.lower() if x.isalnum()]
        return newstr == newstr[::-1]
```
