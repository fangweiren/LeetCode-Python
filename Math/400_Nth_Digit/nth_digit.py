class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        digit = 1   # 确定是哪一位
        base = 9    # 每位的数的个数
        ith = 1     # 起始值
        while n > base * digit:
            n = n - base * digit
            digit += 1
            ith += base
            base *= 10
        num = ith + (n - 1) / digit
        ind = (n - 1) % digit
        print num, ind
        return int(str(num)[ind])
