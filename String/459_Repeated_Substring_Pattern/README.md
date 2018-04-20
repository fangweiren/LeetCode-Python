题意  
Given a non-empty string check if it can be constructed by taking a substring of it and appending multiple copies of the substring together. You may assume the given string consists of lowercase English letters only and its length will not exceed 10000.  
给定一个非空的字符串，判断它是否可以由它的一个子串重复多次构成。给定的字符串只含有小写英文字母，并且长度不超过10000。

Example 1:
```python
Input: "abab"

Output: True

Explanation: It's the substring "ab" twice.
# 解释: 可由子字符串 "ab" 重复两次构成。
```
Example 2:
```python
Input: "aba"

Output: False
```
Example 3:
```python
Input: "abcabcabcabc"

Output: True

Explanation: It's the substring "abc" four times. (And the substring "abcabc" twice.)
# 解释: 可由子字符串 "abc" 重复四次构成。 (或者子字符串 "abcabc" 重复两次构成。)
```
思路  

```
class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        ss = (s + s)[1:-1]
        return s in ss
```
[LeetCode 459. Repeated Substring Pattern](https://leetcode.com/problems/repeated-substring-pattern/description/)
