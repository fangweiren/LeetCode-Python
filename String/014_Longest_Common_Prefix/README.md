### 题意
Write a function to find the longest common prefix string amongst an array of strings.  
编写一个函数来查找字符串数组中的最长公共前缀。

If there is no common prefix, return an empty string "".  
如果不存在公共前缀，返回空字符串 ""。

Example 1:
```python
Input: ["flower","flow","flight"]
Output: "fl"
```
Example 2:
```python
Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.  
解释: 输入不存在公共前缀。
```
Note:  
All given inputs are in lowercase letters a-z.  
所有输入只包含小写字母 a-z 。
### 思路
从任意一个字符串开始，扫描该字符串，依次检查其他字符串的同一位置是否是一样的字符，当遇到不一样时则返回当前得到的前缀。
```python
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        res = ""
        for i in xrange(len(strs[0])):
            for j in range(1, len(strs)):
                if i >= len(strs[j]) or strs[j][i] != strs[0][i]:
                    return res
            res += strs[0][i]
        return res
```
