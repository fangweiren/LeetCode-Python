题意  
Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.  
给定一个字符串，找到它的第一个不重复的字符，并返回它的索引。如果不存在，则返回 -1。

Examples:
```
s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
```
Note: You may assume the string contain only lowercase letters.  
注意事项：您可以假定该字符串只包含小写字母。

思路  
遍历两次，第一次用字典或列表记录每个字符的出现的次数，第二次判断字符是否==1返回其索引值。

```
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        if len(ransomNote) > len(magazine):
            return False
        letters = {}
        for i in magazine:
            letters[i] = letters[i] + 1 if i in letters else 1
        for i in ransomNote:
            if i not in letters:
                return False
            letters[i] -= 1
            if letters[i] < 0:
                return False
        return True


# 用列表实现
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        letters = [0] * 26
        for i in s:
            letters[ord(i) - 97] += 1
        for ind in xrange(len(s)):
            if letters[ord(s[ind]) - 97] == 1:
                return ind
        return -1
```

LeetCode 387. First Unique Character in a String](https://leetcode.com/problems/first-unique-character-in-a-string/description/)
