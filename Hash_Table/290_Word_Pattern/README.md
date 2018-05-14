### 题意
Given a pattern and a string str, find if str follows the same pattern.  
给定一种 pattern(模式) 和一个字符串 str ，判断 str 是否遵循这种模式。

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str.  
这里的 遵循 指完全匹配，例如在pattern里的每个字母和字符串 str 中的每个非空单词存在双向单映射关系。

Examples:
```
pattern = "abba", str = "dog cat cat dog" should return true.
pattern = "abba", str = "dog cat cat fish" should return false.
pattern = "aaaa", str = "dog cat cat dog" should return false.
pattern = "abba", str = "dog dog dog dog" should return false.
```
Notes:  
You may assume pattern contains only lowercase letters, and str contains lowercase letters separated by a single space.  
你可以假设 pattern 只包含小写字母，str 包含了由单个空格分开的小写单词。 

### 思路
利用 zip 函数遍历，建立字符与单词的映射关系，当出现违背映射关系的情况时，可直接返回 False。另外，字典中的不同字符不能映射到相同的 word，所以也要做这方面的检查。
```python
class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        dict1 = {}
        words = str.split(' ')
        if len(pattern) != len(words):
            return False
        for patt, word in zip(pattern, words):
            if patt not in dict1:
                if word in dict1.values():
                    return False
                dict1[patt] = word
            else:
                if dict1[patt] == word:
                    pass
                else:
                    return False
        return True
```
[LeetCode 290. Word Pattern](https://leetcode.com/problems/word-pattern/description/)
