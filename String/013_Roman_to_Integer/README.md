### 题意
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.  
罗马数字包含以下七种字符：I， V， X， L，C，D 和 M。
```python
Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
```
For example, two is written as II in Roman numeral, just two one's added together. Twelve is written as, XII, which is simply X + II. The number twenty seven is written as XXVII, which is XX + V + II.  
例如， 罗马数字 2 写做 II ，即为两个并列的 1。12 写做 XII ，即为 X + II 。 27 写做  XXVII, 即为 XX + V + II 。

Roman numerals are usually written largest to smallest from left to right.  
通常情况下，罗马数字中小的数字在大的数字的右边。

However, the numeral for four is not IIII. Instead, the number four is written as IV.  
但也存在特例，例如 4 不写做 IIII，而是 IV。

Because the one is before the five we subtract it making four.  
数字 1 在数字 5 的左边，所表示的数等于大数 5 减小数 1 得到的数值 4 。

The same principle applies to the number nine, which is written as IX.  
同样地，数字 9 表示为 IX。

There are six instances where subtraction is used:  
这个特殊的规则只适用于以下六种情况：
```python
I can be placed before V (5) and X (10) to make 4 and 9.
I 可以放在 V (5) 和 X (10) 的左边，来表示 4 和 9。
X can be placed before L (50) and C (100) to make 40 and 90.
X 可以放在 L (50) 和 C (100) 的左边，来表示 40 和 90。
C can be placed before D (500) and M (1000) to make 400 and 900.
C 可以放在 D (500) 和 M (1000) 的左边，来表示 400 和 900。
```
Given a roman numeral, convert it to an integer. Input is guaranteed to be within the range from 1 to 3999.  
给定一个罗马数字，将其转换成整数。输入确保在 1 到 3999 的范围内。

Example 1:
```python
Input: "III"
Output: 3
```
Example 2:
```python
Input: "IV"
Output: 4
```
Example 3:
```python
Input: "IX"
Output: 9
```
Example 4:
```python
Input: "LVIII"
Output: 58
Explanation: C = 100, L = 50, XXX = 30 and III = 3.
```
Example 5:
```python
Input: "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
```


### 思路
罗马数字是阿拉伯数字传入之前使用的一种数码。罗马数字采用七个罗马字母作数字、即 I(1)、X(10)、C(100)、M(1000)、V(5)、L(50)、D(500)。

记数的方法:  
1.相同的数字连写，所表示的数等于这些数字相加得到的数，如 Ⅲ=3；  
2.小的数字在大的数字的右边，所表示的数等于这些数字相加得到的数，如 Ⅷ=8、Ⅻ=12；  
3.小的数字（限于 Ⅰ、X 和 C）在大的数字的左边，所表示的数等于大数减小数得到的数，如 Ⅳ=4、Ⅸ=9；  
4.在一个数的上面画一条横线，表示这个数增值 1,000 倍。
```python
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        sum = 0
        convert = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        len_s = len(s)
        for i in range(len_s - 1):
            current = convert[s[i]]
            next = convert[s[i+1]]
            if current >= next:
                sum += current
            else:
                sum -= current
        return sum + convert[s[-1]]
```
[LeetCode 13. Roman to Integer](https://leetcode.com/problems/roman-to-integer/description/)
