class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        return num & (num-1) == 0 and bin(num).count('0') % 2 == 1
