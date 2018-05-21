class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        xor = x ^ y
        n = 0
        while xor:
            n += 1
            xor = xor & (xor - 1)
        return n
