题意  
Given two strings s and t, write a function to determine if t is an anagram of s.  
给定两个字符串 s 和 t，编写函数判断 t 是否为 s 的 anagram (字谜游戏，由颠倒字母顺序而构成的字[短语])。

For example,  
s = "anagram", t = "nagaram", return true.  
s = "rat", t = "car", return false.

Note:  
You may assume the string contains only lowercase alphabets.  
您可以假定该字符串只包含小写字母。

Follow up:  
What if the inputs contain unicode characters? How would you adapt your solution to such case?  
如果输入包含unicode字符会怎么样？ 你会如何适应这种情况？

思路  
统计两个字符串中不同字符出现的次数，只有当两者出现的字符相同且出现的次数相同，那么它们是“anagram”。

```
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        dict1, dict2 = {}, {}
        for i in s:
            dict1[i] = dict1.get(i, 0) + 1
        for i in t:
            dict2[i] = dict2.get(i, 0) + 1
        return dict1 == dict2
```

思路二  
两个字符串若是 “anagram”，则它们只是顺序不一样的相同字符的组合，那么将它们排序后比较是否相等即可。

```
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return sorted(s) == sorted(t)
```

[242. Valid Anagram [easy] (Python)](https://blog.csdn.net/coder_orz/article/details/51406015)
