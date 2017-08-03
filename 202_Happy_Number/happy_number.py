class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        c = set()
        while n not in c:
            c.add(n)
            n = sum([int(x) ** 2 for x in str(n)])
        return n == 1
