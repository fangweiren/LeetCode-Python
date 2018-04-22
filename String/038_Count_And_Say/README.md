### 题意
The count-and-say sequence is the sequence of integers with the first five terms as following:  
报数序列是指一个整数序列，按照其中的整数的顺序进行报数，得到下一个数。其前五项如下：
```python
1.     1
2.     11
3.     21
4.     1211
5.     111221
```
1 is read off as "one 1" or 11.  
1 被读作  "one 1"  ("一个一") , 即 11。

11 is read off as "two 1s" or 21.  
11 被读作 "two 1s" ("两个一"）, 即 21。

21 is read off as "one 2, then one 1" or 1211.  
21 被读作 "one 2",  "one 1" （"一个二" ,  "一个一") , 即 1211。

Given an integer n, generate the nth term of the count-and-say sequence.  
给定一个正整数 n ，输出报数序列的第 n 项。

Note: Each term of the sequence of integers will be represented as a string.  
注意：整数顺序将表示为一个字符串。

Example 1:
```python
Input: 1
Output: "1"
```
Example 2:
```python
Input: 4
Output: "1211"
```
### 思路
根据题目描述的过程写代码，完全遵照规则写就行了。
```python
class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        s = '1'
        for i in range(n-1):
            temp = []
            count = 1
            for j in range(1,len(s)):
                if s[j-1] == s[j]:
                    count += 1
                else:
                    temp.append(str(count))
                    temp.append(s[j-1])
                    count = 1
            temp.append(str(count))
            temp.append(s[-1])
            s = ''.join(temp)
        return s
```
