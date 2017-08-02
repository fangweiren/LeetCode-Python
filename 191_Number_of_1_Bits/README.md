题意  
编写函数接收一个无符号整数，返回其二进制形式中包含的1的个数（也叫做汉明权重）

例如  
32位整数'11'的二进制表示为：00000000000000000000000000001011，因此函数应当返回3

思路一  
利用n & (n-1)的trick。简单的说，运算n = n & (n-1)可以将n最低位的1变成0。循环进行该运算，循环次数就是n的二进制表示中1的个数。
![](https://github.com/fangweiren/leetcode/blob/master/screenshots/1234.jpg?raw=true)

思路二：  
通过移位操作，每次向右移动一位，一位一位的判定是否是数字1。
![](https://github.com/fangweiren/leetcode/blob/master/screenshots/2234.jpg?raw=true)
class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        while n:
            count += n & 1
            n >>= 1
        return count

思路三：  
将输入的数表示成二进制的字符串，数一下有多少个1即可。
class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        return bin(n).count('1')
