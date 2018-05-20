### 题意
Given an integer, write an algorithm to convert it to hexadecimal. For negative integer, two’s complement method is used.  
给定一个整数，编写一个算法将这个数转换为十六进制数。对于负整数，我们通常使用 补码运算 方法。

Note:

- 1.All letters in hexadecimal (a-f) must be in lowercase.
- 十六进制中所有字母(a-f)都必须是小写。
- 2.The hexadecimal string must not contain extra leading 0s. If the number is zero, it is represented by a single zero character '0'; otherwise, the first character in the hexadecimal string will not be the zero character.  
- 十六进制字符串中不能包含多余的前导零。如果要转化的数为0，那么以单个字符'0'来表示；对于其他情况，十六进制字符串中的第一个字符将不会是0字符。
- 3.The given number is guaranteed to fit within the range of a 32-bit signed integer.  
- 给定的数确保在32位有符号整数范围内。
- 4.You must not use any method provided by the library which converts/formats the number to hex directly.  
- 不能使用任何由库提供的将数字直接转换或格式化为十六进制的方法。

Example 1:
```
Input:
26

Output:
"1a"
```
Example 2:
```
Input:
-1

Output:
"ffffffff"
```

### 思路
进制转换。
```python
class Solution(object):
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        ans = []
        hexs = '0123456789abcdef'
        if num < 0: num += 0x100000000
        while num:
            ans.append(hexs[num % 16])
            num /= 16
        return ''.join(ans[::-1]) if ans else '0'


**********************************************************


class Solution(object):
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return '0'
        mp = '0123456789abcdef'
        ans = ''
        for _ in range(8):
            n = num & 15   # bin(15) == 1111，提取 num 最后四位
            c = mp[n]
            ans = c + ans
            num = num >> 4
        return ans.lstrip('0')  #strip leading zeroes
```
[LeetCode 405. Convert a Number to Hexadecimal](https://leetcode.com/problems/convert-a-number-to-hexadecimal/description/)
