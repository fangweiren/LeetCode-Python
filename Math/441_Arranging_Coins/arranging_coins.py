class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        k = 0
        while k * (k+1) / 2 <= n:
            k += 1
        return k-1
