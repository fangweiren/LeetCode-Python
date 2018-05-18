### 题意
Given a List of words, return the words that can be typed using letters of alphabet on only one row's of American keyboard like the image below.  
给定一个单词列表，只返回可以使用在键盘同一行的字母打印出来的单词。键盘如下图所示。

![500. Keyboard Row](https://github.com/fangweiren/LeetCode-Python/blob/master/screenshots/keyboard.png?raw=true)

Example 1:
```
Input: ["Hello", "Alaska", "Dad", "Peace"]
Output: ["Alaska", "Dad"]
```
Note:
- You may use one character in the keyboard more than once.
- 你可以重复使用键盘上同一字符。
- You may assume the input string will only contain letters of alphabet.
- 你可以假设输入的字符串将只包含字母。

### 思路
本题考察 Python 中 set 的用法，如果一个字符串的所有字母都在一个字符串中，即一个集合是另一个集合的子集。

关系运算符 >、>=、<、<= 作用于集合时表示集合之间的包含关系，而不是集合中元素的大小关系。
```python
>>> x = { 1, 2, 3 }
>>> y = { 1, 2, 5 }
>>> z = { 1, 2, 3, 4 }
>>> x < y
False
>>> x < z
True
>>> y < z
False
>>> x.issubset(y)   # 测试是否为子集
False
>>> x.issubset(z)
True
>>> 


class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        res = []
        rows = [set('qwertyuiop'), set('asdfghjkl'), set('zxcvbnm')]
        for word in words:
            for row in rows:
                if set(word.lower()) <= row:
                    res.append(word)
        return res
```
[LeetCode 500. Keyboard Row](https://leetcode.com/problems/keyboard-row/description/)
