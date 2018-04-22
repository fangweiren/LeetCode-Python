### 题意
Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.  
给定一个仅包含大小写字母和空格 ' ' 的字符串，返回其最后一个单词的长度。

If the last word does not exist, return 0.  
如果不存在最后一个单词，请返回 0 。

Note: A word is defined as a character sequence consists of non-space characters only.  
说明：一个单词是指由字母组成，但不包含任何空格的字符串。

Example:
```python
Input: "Hello World"
Output: 5
```
### 思路一
利用 Python 的内置函数 string.rstrip() 和 string.split() 。先将字符串后面的空格部分删除，再按照空格字符将剩余部分分成若干部分，此时最后一部分即为最后一个单词（也可能是' '），直接返回其长度即可。
```python
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        return 0 if len(s.split()) == 0 else len(s.split()[-1])
        # return len(s.rstrip(' ').split(' ')[-1])
```
### 思路二：

与上面类似，不过不再用内置string处理函数了，在删除后面的空格后，从后面开始数非空格字符的个数，即为所求。
```python
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        i = len(s) - 1
        while i >= 0 and s[i] == ' ':
            i -= 1
        length = 0
        while i >= 0 and s[i] != ' ':
            length += 1
            i -= 1
        return length
```
