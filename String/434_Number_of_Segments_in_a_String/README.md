题意  
Count the number of segments in a string, where a segment is defined to be a contiguous sequence of non-space characters.  
统计字符串中的单词个数，这里的单词指的是连续的非空字符。

Please note that the string does not contain any non-printable characters.  
请注意，你可以假定字符串里不包括任何不可打印的字符。

Example:
```
Input: "Hello, my name is John"
Output: 5
```
思路  
简单粗暴，直接使用 split()

```
class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        return len(s.split())
```

[LeetCode 434. Number of Segments in a String](https://leetcode.com/problems/number-of-segments-in-a-string/description/)
