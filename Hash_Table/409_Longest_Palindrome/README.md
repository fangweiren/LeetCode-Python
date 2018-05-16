### 题意
Given a string which consists of lowercase or uppercase letters, find the length of the longest palindromes that can be built with those letters.  
给定一个包含大写字母和小写字母的字符串，找到通过这些字母构造成的最长的回文串。

This is case sensitive, for example "Aa" is not considered a palindrome here.  
在构造过程中，请注意区分大小写。比如 "Aa" 不能当做一个回文字符串。

Note:  
Assume the length of given string will not exceed 1,010.  
假设字符串的长度不会超过 1010。

Example:
```
Input:
"abccccdd"

Output:
7

Explanation:
One longest palindrome that can be built is "dccaccd", whose length is 7.
我们可以构造的最长的回文串是"dccaccd", 它的长度是 7。
```

### 思路
这题我们不关心最长的 Palindrome 是什么，而关心其长度。我们可以通过字典来统计每个字母出现的次数。  
如果一个字符有偶数个，则可以为最长 Palindrome 贡献所有的字符。  
如果一个字符有奇数个，则可以为最长 Palindrome 贡献所有字符数 -1 个字符。  
最长 Palindrome 最中间可以有字符也可以没有字符，取决于是否含有字符数为奇数的字符。中间的字符可以是“字符数为奇数的字符”中的任意一个。

```python
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = {}
        res = 0
        for c in s:
            d[c] = d[c] + 1 if c in d else 1
        for times in d.values():
            if times % 2 == 0:
               res += times
            else:
                res += times - 1
        return res+1 if res < len(s) else res
```
[LeetCode 409. Longest Palindrome](https://leetcode.com/problems/longest-palindrome/description/)
