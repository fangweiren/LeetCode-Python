题意  
Given an arbitrary ransom note string and another string containing letters from all the magazines, write a function that will return true if the ransom note can be constructed from the magazines ; otherwise, it will return false.  
给定一个赎金信 (ransom) 字符串和一个杂志(magazine)字符串，判断第一个字符串ransom能不能由第二个字符串magazines里面的字符构成。如果可以构成，返回 true ；否则返回 false。

Each letter in the magazine string can only be used once in your ransom note.  
为了不暴露赎金信字迹，要从杂志上搜索各个需要的字母，组成单词来表达意思

Note:  
You may assume that both strings contain only lowercase letters.  
你可以假设两个字符串均只含有小写字母。

canConstruct("a", "b") -> false  
canConstruct("aa", "ab") -> false  
canConstruct("aa", "aab") -> true  

思路  
计算两个字符串每个字母出现的次数再比较即可。可以用数组或字典保存每个字母出现的次数，对于两个字符串分别用加法和减法统计字母出现次数。
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
```
思路二：  
使用集合
```
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        for i in set(ransomNote):
            if ransomNote.count(i) > magazine.count(i):
                return False
        return True
```

[LeetCode 383. Ransom Note](https://leetcode.com/problems/ransom-note/description/)
