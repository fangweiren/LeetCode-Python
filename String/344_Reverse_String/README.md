题意  
Write a function that takes a string as input and returns the string reversed.  
编写一个将字符串作为输入的函数，并返回反转的字符串。

Example:
Given s = "hello", return "olleh".

思路  
```
class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        return s[::-1]
```
思路二  
依次交换前面和后面的字符直至中间字符，完成反转。需要注意Python不能直接修改字符串的某一位，所以需要先转成字符串数组再处理。该思路也用双指针实现。
```
class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = list(s)
        for i in xrange(0, len(s)/2):
            tmp = s[i]
            s[i] = s[len(s)-1-i]
            s[len(s)-1-i] = tmp
        return ''.join(s)
```
思路三
```
class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        return ''.join([s[i] for i in range(len(s)-1, -1, -1)])
```

[LeetCode 344. Reverse String](https://leetcode.com/problems/reverse-string/description/)
