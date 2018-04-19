题意  
Write a function that takes a string as input and reverse only the vowels of a string.  
编写一个函数，以字符串作为输入，反转该字符串中的元音字母。

Example 1:  
Given s = "hello", return "holle".

Example 2:  
Given s = "leetcode", return "leotcede".

Note:  
The vowels does not include the letter "y".

思路  
维护两个指针分别从字符串头和尾扫描，每次交换两个指针扫到的元音字母，于是只需遍历一遍字符串就可以完成元音字母逆序。

```
class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowel = 'aeiouAEIOU'
        s = list(s)
        i, j = 0, len(s)-1
        while i < j:
            while s[i] not in vowel and i < j:
                i += 1
            while s[j] not in vowel and i < j:
                j -= 1
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1
        return ''.join(s)
```

[LeetCode 345. Reverse Vowels of a String](https://leetcode.com/problems/reverse-vowels-of-a-string/description/)
