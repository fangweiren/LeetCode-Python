### 题意
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.  
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。

An input string is valid if:  
有效字符串需满足：

1.Open brackets must be closed by the same type of brackets.  
1.左括号必须用相同类型的右括号闭合。

2.Open brackets must be closed in the correct order.  
左括号必须以正确的顺序闭合。

Note that an empty string is also considered valid.  
注意空字符串可被认为是有效字符串。

Example 1:
```python
Input: "()"
Output: true
```
Example 2:
```python
Input: "()[]{}"
Output: true
```
Example 3:
```python
Input: "(]"
Output: false
```
Example 4:
```python
Input: "([)]"
Output: false
```
Example 5:
```python
Input: "{[]}"
Output: true
```
### 思路
用栈来操作，将所有的字符依次入栈，当栈顶的括号和正要入栈的括号匹配时将栈顶的括号弹出且不入栈，否则入栈新的括号。最后，只有当栈里没有括号时，才表明输入是有效的。
```python
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        dict = { '}':'{', ']':'[', ')':'(' }
        for char in s:
            if char in dict.values():
                stack.append(char)
            elif char in dict.keys():
                if stack == [] or dict[char] != stack.pop():
                    return False
            else:
                return False
        return stack == []
```
[LeetCode 20. Valid Parentheses](https://leetcode.com/problems/valid-parentheses/description/)
