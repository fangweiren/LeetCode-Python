题意  
Given an array of characters, compress it in-place.  
给定一组字符，使用原地算法将其压缩。

The length after compression must always be smaller than or equal to the original array.  
压缩后的长度必须始终小于或等于原数组长度。

Every element of the array should be a character (not int) of length 1.  
数组的每个元素应该是长度为1 的字符（不是 int 整数类型）。

After you are done modifying the input array in-place, return the new length of the array.  
在完成原地修改输入数组后，返回数组的新长度。

Follow up:  
进阶：
Could you solve it using only O(1) extra space?  
你能否仅使用O(1) 空间解决问题？

Example 1:
```python
Input:
["a","a","b","b","c","c","c"]

Output:
Return 6, and the first 6 characters of the input array should be: ["a","2","b","2","c","3"]

Explanation:
"aa" is replaced by "a2". "bb" is replaced by "b2". "ccc" is replaced by "c3".
```
Example 2:
```python
Input:
["a"]

Output:
Return 1, and the first 1 characters of the input array should be: ["a"]

Explanation:
Nothing is replaced.
```
Example 3:
```python
Input:
["a","b","b","b","b","b","b","b","b","b","b","b","b"]

Output:
Return 4, and the first 4 characters of the input array should be: ["a","b","1","2"].

Explanation:
Since the character "a" does not repeat, it is not compressed. "bbbbbbbbbbbb" is replaced by "b12".
Notice each digit has it's own entry in the array.
```
Note:  
All characters have an ASCII value in [35, 126].  
1 <= len(chars) <= 1000.

思路  
```
class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        anchor = write = 0
        for read, c in enumerate(chars):
            if read + 1 == len(chars) or chars[read + 1] != c:
                chars[write] = chars[anchor]
                write += 1
                if read > anchor:
                    for digit in str(read - anchor + 1):
                        chars[write] = digit
                        write += 1
                anchor = read + 1
        return write
```
[LeetCode 443. String Compression](https://leetcode.com/problems/string-compression/description/)
