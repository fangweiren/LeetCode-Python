题意  
写一个程序来判断一个数字是否“happy”

所谓happy number，是被这样的过程定义的数字：初始时有一个正整数，用该整数每位数字的平方之和代替这个整数，重复该过程直至数字变为1（之后不再变化），或者陷入一个无尽的循环但该循环不包括1。那些能终止于1的数字就称为happy number。

比如：19就是一个 happy number，因为

    1**2+9**2=82 
    8**2+2**2=68 
    6**2+8**2=100 
    1**2+0**2+0**2=1

思路  
按照“happy number”的定义，直接循环计算各位平方和，观察是否收敛到1，若是则是happy number。为了判断循环是否开始重复，要用一个字典（dict）或集合（set）来保存已经出现的数字，dict的效率更高。
<pre><code>
class Solution:
    # @param {integer} n
    # @return {boolean}
    def isHappy(self, n):
        val = set()
        while n not in val:
            val.add(n)
            newn = 0
            while n != 0:
                newn += (n % 10) * (n % 10)
                n /= 10
            n = newn
            if n == 1:
                return True
        return False
</code></pre>
