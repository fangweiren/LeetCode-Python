题意：  
Given two strings s and t, determine if they are isomorphic.  
给定两个字符串 s 和 t，判断它们是否是同构的。  
Two strings are isomorphic if the characters in s can be replaced to get t.  
如果字符串 s 可以通过字符替换的方式得到字符串 t，那么 s 和 t 是同构的。  
All occurrences of a character must be replaced with another character while preserving the order of characters.  
字符的每一次出现都必须被其对应字符所替换，同时还需要保证原始顺序不发生改变。  
No two characters may map to the same character but a character may map to itself.  
两个字符不能映射到同一个字符，但是字符可以映射到其本身。

```
class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        d1 = {}
        d2 = {}
        for i, val in enumerate(s):
            d1[val] = d1.get(val, []) + [i]
        for i, val in enumerate(t):
            d2[val] = d2.get(val, []) + [i]
        return sorted(d1.values()) == sorted(d2.values())
```

[LeetCode 205. Isomorphic Strings](https://leetcode.com/problems/isomorphic-strings/description/)
