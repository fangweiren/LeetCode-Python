### 题意
Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.  
给定一个字符串 s 和一个非空字符串 p，找到 s 中所有是 p 的字母异位词的子串，返回这些子串的起始索引。

Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.  
字符串只包含小写英文字母，并且字符串 s 和 p 的长度都不超过 20100。

The order of output does not matter.  
输出的顺序并不重要。

Example 1:
```
Input:
s: "cbaebabacd" p: "abc"

Output:
[0, 6]

Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
起始索引等于 0 的子串是 "cba", 它是 "abc" 的字母异位词。
The substring with start index = 6 is "bac", which is an anagram of "abc".
```
Example 2:
```
Input:
s: "abab" p: "ab"

Output:
[0, 1, 2]

Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".
```

### 思路
在 s 中保持一个长度为 len(p) 窗口，然后向右滑动直到完成。时间复杂度是 O(len(s))。
```python
class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        from collections import Counter
        
        res = []
        pCounter = Counter(p)
        sCounter = Counter(s[:len(p)-1])
        for i in range(len(p)-1, len(s)):
            sCounter[s[i]] += 1                 # 加入一个新的字符
            if sCounter == pCounter:
                res.append(i-len(p)+1)          # 追加起始索引
            sCounter[s[i-len(p)+1]] -= 1        # 旧字符计数减 1
            if sCounter[s[i-len(p)+1]] == 0:    # 如果为 0，则删除
                del sCounter[s[i-len(p)+1]]
        return res
注: Counter 类型拥有字典类型的函数接口，并且对于不存在于 Counter 对象中的键返回 0 而不是引发一个 TypeError。
```
[LeetCode 438. Find All Anagrams in a String](https://leetcode.com/problems/find-all-anagrams-in-a-string/description/)
